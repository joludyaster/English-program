from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging
import datetime
from aiogram import executor
from aiogram.types import ContentType
from utils.db_api.add_to_database import start_bd
from utils.db_api.database import create_datab
from utils.db_api.db_command import bot_token
from utils.db_api.models import Botset

index_bot = 'prod_bot'

create_datab()
start_bd()


bot = Bot(token=bot_token(index_bot=index_bot), parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands="start")
async def send_message(message: types.Message):
    values = (await Botset.select('url_source', 'name_source', 'text_start', 'url_public_offer', 'text_offer',
                                  'button_price', 'amount', 'invoice_title', 'invoice_description', 'provider_token',
                                  'url', 'suggested').where(Botset.index_bot == index_bot).gino.all())[0]
    await message.answer(
        text=f"<a href='{values[0]}'>{values[1]}</a> {values[2]} \n"
             f"<a href='{values[3]}'>{values[4]}</a>",
        disable_web_page_preview=True)
    print(values[9])
    print(type(values[9]))
    await bot.send_invoice(message.chat.id,
                           title=values[7],
                           description=values[8],
                           provider_token=values[9],
                           currency='uah',
                           photo_height=512,
                           photo_width=512,
                           photo_url=values[10],
                           is_flexible=False,
                           prices=[types.LabeledPrice(label=values[5], amount=values[6])],
                           payload=values[7],
                           need_name=True,
                           need_email=True,
                           need_phone_number=True,
                           max_tip_amount=values[11],
                           suggested_tip_amounts=[values[11]])


@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def process_successful_payment(message: types.Message):
    time = datetime.datetime.now()
    pmnt = message.successful_payment.to_python()
    data = pmnt["order_info"]
    info = []
    values = (await Botset.select('text_time', 'text_date', 'text_name', 'text_phone', 'text_mail', 'text_nickname',
                                  'amount', 'suggested', 'chat_id_manage', 'text_title', 'text_privelegy',
                                  'text_payment_summa', 'text_currency', 'text_hi', 'text_info_1', 'text_info_2',
                                  'text_manager', 'url', 'name_source', 'text_call_you', 'text_by',
                                  'url_public_offer', 'text_public_offer', 'text_invoice_light_manage',
                                  'text_info_tarif_light', 'text_invoice_medium_manage',
                                  'text_info_tarif_medium').where(Botset.index_bot == index_bot).gino.all())[0]
    data_and_time = (f"<b>{values[0]}</b>: {time.strftime('%H:%M')}",
                     f"<b>{values[1]}</b>: {time.strftime('%d-%m-%Y')}")
    replace = {"name": values[2],
               "phone_number": values[3],
               "email": values[4]}
    for item in data.keys():
        info.append(f"<b>{replace[item]}</b>: {data[item]}")
    info.append(f"<b>{values[5]}</b>: <a href='tg://user?id={message.from_user.id}'>{message.from_user.full_name}</a>")
    if int(values[6]) <= message.successful_payment.total_amount < (int(values[6]) + int(values[7])):
        text_for_manage = values[23]
        text_for_user = values[24]
    elif (int(values[6]) + int(values[7])) <= message.successful_payment.total_amount:
        text_for_manage = values[25]
        text_for_user = values[26]
    else:
        text_for_manage = '   '
        text_for_user = '   '

    await bot.send_message(
        chat_id=values[8],
        text="<b>{}</b>: {}\n<b>{}</b>: {}\n\n{}\n\n{}\n\n<b>{}</b>: {},{} {}".format(
            values[9], pmnt["invoice_payload"], values[10], text_for_manage, "\n".join(data_and_time), "\n".join(info),
            values[11], str(pmnt["total_amount"])[:-2], str(pmnt["total_amount"])[-2:], values[12]))
    try:
        await bot.send_message(
            chat_id=message.chat.id,
            text=f"{values[13]}\n"
                 f"{values[14]} {str(pmnt['total_amount'])[:-2]},{str(pmnt['total_amount'])[-2:]} {values[12]} "
                 f"{values[15]}\n\n{text_for_user}️\n\n{values[16]} <a href='{values[17]}'>{values[18]}</a> "
                 f"{values[19]}\n{values[20]}\n\n<a href='{values[21]}'>{values[22]}</a>",
            disable_web_page_preview=True
        )
    except Exception as err:
        logging.exception(err)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
