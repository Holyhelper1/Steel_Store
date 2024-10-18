from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

# Генерация приватного ключа
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Сохранение приватного ключа в файл
with open("certs/jwt-private.pem", "wb") as f:
    f.write(
        private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
    )

# Генерация публичного ключа из приватного
public_key = private_key.public_key()

# Сохранение публичного ключа в файл
with open("certs/jwt-public.pem", "wb") as f:
    f.write(
        public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
    )

print("RSA ключи успешно созданы и сохранены.")