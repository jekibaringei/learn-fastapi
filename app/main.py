from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .database import engine
from .routers import post, users, auth, vote
from .config import settings


'''
SETUP API
1. Buat Environment
2. Install Framework FastAPI
pip install "fastapi[all]" <- akan menginstall semua packages yang tersedia walaupun tidak dibutuhkan
pada proses penginstalan fastapi packages pydantic juga ikut terinstall
3. Install psycopg2-binary untuk menghubungkan kode python dengan postgresql
4. Install SqlAlchemy
5. Install Passlib dan Bcrypt untuk melakukan hashing password.
6. Membuat JWT Token Authentication
Install python-jose dan cryptography


DATABASE MIGRATIONS
using Alembic -> pip install alembic

menggunakannya diterminal
alembic init --nama directory--
contoh: alembic init alembic
setelah itu akan muncul folder dengan nama alembic, konfigurasi env.py
jika sudah ketik ini diterminal untuk merevisi database
alembic revision -m "create posts table", edit manual pada func upgrade dan downgrade

cek untuk melihat database terbaru
untuk informasi lengkap ketik ini diterminal
alembic --help
'''

# models.Base.metadata.create_all(bind=engine) // since we have alembic we dont need this



app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": "favorite foods", "content": "I like pizza", "id": 2}]

# def find_post(id):
#     for p in my_posts:
#         if p['id'] == id:
#             return p


app.include_router(post.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "welcome to my api!!"}



