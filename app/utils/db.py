
import pymysql
from app import Config

def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password=Config.DB_PASSWORD,
        database='complaint_system',
        cursorclass=pymysql.cursors.DictCursor
    )
