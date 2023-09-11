import asyncio

from utils.db_api.models import Botset
from utils.db_api.database import create_db


async def add_data():
    list_temp = [(
        'test_bot',  # index_bot = "Индекс бота, для понимания что за бот"
        'Тестовый бот',  # name_index_bot = "Название бота"
        '1822028335:AAEWlibgrVoekBhntcZpOn5IMdXxpl0EG4k',  # bot_token = "Токен бота"
        '632593626:TEST:sandbox_i50754732224',  # provider_token = "Платежный токен"
        16500,  # amount = "Сумма"
        21000,  # suggested = "Чаевые"
        'https://telegra.ph/file/9a54c4392f481e487d20e.jpg',  # url = "URL картинки"
        -1001598180481,  # chat_id_manage = "Номер чата с присыланием оповещений об оплате"
        '- підтримує благодійні проекти на платформі, тому здійснюючи оплату — Ви погоджуєтесь, що сума пожертвування '
        'за майстер-клас не підлягає поверненню.',  # text_start = "Текст при старте"
        'Оплата',  # button_price = "Название кнопки оплата"
        'Як знайти гроші на свою ідею',  # invoice_title = "Текст платежного заголовка"
        'Про те, як знайти $ на благо ідею або бізнес: без боргів, кредитів і повернення інвестицій — з платформою '
        'RazomGO.com. Від творця платформи Алекси Айшпур\n\n165 грн - майстер-клас 1,5 години\n375 грн - майстер-клас '
        '+ онлайн розбір ідеї\nОплата LiqPay',  # invoice_description = "Текст платежного описания"
        'Время',  # text_time = "Название времени"
        'Телефон',  # text_phone = "Название телефона"
        'Имейл',  # text_mail = "Название почты"
        'Ник в телеграмме',  # text_nickname = "Текст ник в телеграмме, если пусто, то ссылки не будет"
        'Название',  # text_title = "Текст Название"
        'Привилегия',  # text_privelegy = "Текст Привилегия"
        'Сумма оплаты',  # text_payment_summa = "Текст Сумма оплаты"
        'грн.',  # text_currency = "Валюта сокращенно"
        'Вітаємо!',  # text_hi = "Текст приветствия"
        'Ваша оплата на суму',  # text_info_1 = "Текст Ваша оплата на сумму"
        'пройшла успішно!',  # text_info_2 = "Текст прошла успешно"
        'RazomGo',  # name_source = "Название ресурса/компании"
        'http://razomgo.com/',  # url_source = "URL ресурса/компании"
        'Менеджер',  # text_manager = "Текст Менеджер"
        'найближчим часом з Вами зв’яжеться!',  # text_call_you = "Текст о том, что свяжутся"
        'Гарного дня ☀️',  # text_by = "Текст прощания"
        'Публічна оферта',  # text_public_offer = "Текст Публичная аферта"
        'https://razomgo.ua/charity',  # url_public_offer = "URL Публичной афферты"
        'Майстер-клас 1,5 години',  # text_invoice_light_manage = "Текст названия базового пакета в оповещении для
        # менеджера"
        'Ви обрали тариф просто прослухати майстер-класс',  # text_info_tarif_light = "Текст для клиента о выборе
        # базового тарифа"
        'Майстер-клас + онлайн розбір ідеї',  # text_invoice_medium_manage = "Текст названия расширенного пакета
        # в оповещении для менеджера"
        'Ви обрали тариф із консультацією',  # text_info_tarif_medium = "Текст для клиента о выборе стандартного
        # тарифа"
        'Оферта',  # text_offer = "Текст Аферта"
        'Имя',  # text_name = "Текст Имя"
        'Дата',  # text_date = "Текст Дата"
        10000000,    # max_amount = "Максимальная сумма"
    ), (
        'prod_bot',  # index_bot = "Индекс бота, для понимания что за бот"
        'Рабочий бот',  # name_index_bot = "Название бота"
        '1833328468:AAHvVzzCz50hcpOIXsaIoBX3dbBH-0IzlKw',  # bot_token = "Токен бота"
        '635983722:LIVE:i93339316042',  # provider_token = "Платежный токен"
        16500,  # amount = "Сумма"
        21000,  # suggested = "Чаевые"
        'https://telegra.ph/file/9a54c4392f481e487d20e.jpg',  # url = "URL картинки"
        -510903291,  # chat_id_manage = "Номер чата с присыланием оповещений об оплате"
        '- підтримує благодійні проекти на платформі, тому здійснюючи оплату — Ви погоджуєтесь, що сума пожертвування '
        'за майстер-клас не підлягає поверненню.',  # text_start = "Текст при старте"
        'Оплата',  # button_price = "Название кнопки оплата"
        'Як знайти гроші на свою ідею',  # invoice_title = "Текст платежного заголовка"
        'Про те, як знайти $ на благо ідею або бізнес: без боргів, кредитів і повернення інвестицій — з платформою '
        'RazomGO.com. Від творця платформи Алекси Айшпур\n\n165 грн - майстер-клас 1,5 години\n375 грн - '
        'майстер-клас + онлайн розбір ідеї\nОплата LiqPay',  # invoice_description = "Текст платежного описания"
        'Время',  # text_time = "Название времени"
        'Телефон',  # text_phone = "Название телефона"
        'Имейл',  # text_mail = "Название почты"
        'Ник в телеграмме',  # text_nickname = "Текст ник в телеграмме, если пусто, то ссылки не будет"
        'Название',  # text_title = "Текст Название"
        'Привилегия',  # text_privelegy = "Текст Привилегия"
        'Сумма оплаты',  # text_payment_summa = "Текст Сумма оплаты"
        'грн.',  # text_currency = "Валюта сокращенно"
        'Вітаємо!',  # text_hi = "Текст приветствия"
        'Ваша оплата на суму',  # text_info_1 = "Текст Ваша оплата на сумму"
        'пройшла успішно!',  # text_info_2 = "Текст прошла успешно"
        'RazomGO',  # name_source = "Название ресурса/компании, если нет, то нет оповещения, что  свяжутся"
        'https://razomgo.com/',  # url_source = "URL ресурса/компании"
        'Менеджер',  # text_manager = "Текст Менеджер"
        'найближчим часом з Вами зв’яжеться!',  # text_call_you = "Текст о том, что свяжутся"
        'Гарного дня ☀️',  # text_by = "Текст прощания"
        'Публічна оферта',  # text_public_offer = "Текст Публичная аферта"
        'https://razomgo.com/charity',  # url_public_offer = "URL Публичной афферты"
        'Майстер-клас 1,5 години',  # text_invoice_light_manage = "Текст названия базового пакета в оповещении для
        # менеджера"
        'Ви обрали тариф просто прослухати майстер-класс️',  # text_info_tarif_light = "Текст для клиента о выборе
        # базового тарифа"
        'Майстер-клас + онлайн розбір ідеї',  # text_invoice_medium_manage = "Текст названия расширенного пакета в
        # оповещении для менеджера"
        'Ви обрали тариф із консультацією',  # text_info_tarif_medium = "Текст для клиента о выборе стандартного тарифа"
        'Оферта',  # text_offer = "Текст Аферта"
        'Имя',  # text_name = "Текст Имя"
        'Дата',  # text_date = "Текст Дата"
        10000000,  # max_amount = "Максимальная сумма"
    )]
    for i in list_temp[:]:
        if (await Botset.select('index_bot').where(Botset.index_bot == i[0]).gino.scalar()) == i[0]:
            ...
        else:
            await Botset(index_bot=i[0],
                         name_index_bot=i[1],
                         bot_token=i[2],
                         provider_token=i[3],
                         amount=i[4],
                         suggested=i[5],
                         url=i[6],
                         chat_id_manage=i[7],
                         text_start=i[8],
                         button_price=i[9],
                         invoice_title=i[10],
                         invoice_description=i[11],
                         text_time=i[12],
                         text_phone=i[13],
                         text_mail=i[14],
                         text_nickname=i[15],
                         text_title=i[16],
                         text_privelegy=i[17],
                         text_payment_summa=i[18],
                         text_currency=i[19],
                         text_hi=i[20],
                         text_info_1=i[21],
                         text_info_2=i[22],
                         name_source=i[23],
                         url_source=i[24],
                         text_manager=i[25],
                         text_call_you=i[26],
                         text_by=i[27],
                         text_public_offer=i[28],
                         url_public_offer=i[29],
                         text_invoice_light_manage=i[30],
                         text_info_tarif_light=i[31],
                         text_invoice_medium_manage=i[32],
                         text_info_tarif_medium=i[33],
                         text_offer=i[34],
                         text_name=i[35],
                         text_date=i[36],
                         max_amount=i[37]).create()


def start_bd():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(create_db())
    loop.run_until_complete(add_data())
