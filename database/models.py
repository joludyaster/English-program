from sqlalchemy import Column, Integer, String, Sequence, JSON, ARRAY, Boolean, Date, \
    Time, DateTime, Text
from sqlalchemy import sql
from utils.db_api.database import db


class Botset(db.Model):
    __tablename__ = 'alla_bots_botset'
    query: sql.Select

    index_bot = Column(String(10))
    name_index_bot = Column(String(20))
    bot_token = Column(String(50))
    provider_token = Column(String(50))
    amount = Column(Integer)
    suggested = Column(Integer)
    max_amount = Column(Integer)
    url = Column(String(200))
    chat_id_manage = Column(Integer)
    text_start = Column(Text)
    button_price = Column(String(25))
    invoice_title = Column(String(100))
    invoice_description = Column(Text)
    text_time = Column(String(25))
    text_phone = Column(String(25))
    text_mail = Column(String(25))
    text_nickname = Column(String(25))
    text_title = Column(String(25))
    text_privelegy = Column(String(25))
    text_payment_summa = Column(String(25))
    text_currency = Column(String(10))
    text_hi = Column(String(20))
    text_info_1 = Column(String(50))
    text_info_2 = Column(String(50))
    name_source = Column(String(20))
    url_source = Column(String(200))
    text_manager = Column(String(20))
    text_call_you = Column(String(100))
    text_by = Column(String(20))
    text_public_offer = Column(String(30))
    url_public_offer = Column(String(200))
    text_invoice_light_manage = Column(String(50))
    text_info_tarif_light = Column(String(100))
    text_invoice_medium_manage = Column(String(50))
    text_info_tarif_medium = Column(String(100))
    text_offer = Column(String(15))
    text_name = Column(String(15))
    text_date = Column(String(15))
