import psycopg2
from data.config import DATABASE, PGUSER, PGPASSWORD, ip, PGPORT, POSTGRES_URI


def bot_token(index_bot):
    conn = psycopg2.connect(dbname=DATABASE, user=PGUSER, password=PGPASSWORD, host=ip)
    cursor = conn.cursor()
    cursor.execute("SELECT bot_token FROM alla_bots_botset WHERE index_bot = %(index)s",
                   {'index': index_bot})
    token = (cursor.fetchone())[0]
    cursor.close()
    conn.close()
    return token
