from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2 #sebagai dokumentasi saja karena sudah memiliki sqlalchemy untuk terhubung kedalam DB
from psycopg2.extras import RealDictCursor  #sebagai dokumentasi saja karena sudah memiliki sqlalchemy untuk terhubung kedalam DB
import time  #sebagai dokumentasi saja karena sudah memiliki sqlalchemy untuk terhubung kedalam DB
from .config import settings

# SQLALCHEMY_DATABASE_URL = "postgres://<username>:<password>@<ip-address/hostname>/<database_name>"
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}" #ini dapat disembunyikan pada environment variabel

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




# koneksi ke dalam database
# pengguna while loop digunakan ketika salah memasukan koneksi maka program akan terus menampilkan error dan tidak akan melanjutkan ke kode yang berikutnya sampai koneksi diperbaiki
 #sebagai dokumentasi saja karena sudah memiliki sqlalchemy untuk terhubung kedalam DB
# while True:

#     try:
#         # kondisi ketika koneksi database berhasil
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='kunci_sukses123', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was succesfull")
#         break
#     except Exception as error:
#         # kondisi ketika gagal terkoneksi ke database
#         print("Connecting to database failed")
#         print("Error: ", error)
#         time.sleep(2)

