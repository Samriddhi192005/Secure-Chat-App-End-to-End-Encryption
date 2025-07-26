from cryptography.fernet import Fernet

# Fix a shared key for both server and clients
key = b'nYvpU2mPQxEaFUF1Ifa7KakTj2rBNJKAI9ShR7HKrDY='  # 👈 this is your static key
cipher = Fernet(key)

def encrypt_message(message):
    return cipher.encrypt(message.encode()).decode()

def decrypt_message(encrypted_message):
    return cipher.decrypt(encrypted_message.encode()).decode()
