from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") #digunakan untuk memberitahu passlib apa algoritma hash yang ingin kita gunakan. pada kasus ini kita menggunakan bcrypt.


def hash(password: str):
    return pwd_context.hash(password)


def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)