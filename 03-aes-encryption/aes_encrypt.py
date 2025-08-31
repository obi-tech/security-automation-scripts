from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Encrypt a message
text = input("Enter text to encrypt: ").encode()
cipher_text = cipher_suite.encrypt(text)

# Decrypt the message
plain_text = cipher_suite.decrypt(cipher_text)

print(f"Key: {key.decode()}")
print(f"Encrypted: {cipher_text.decode()}")
print(f"Decrypted: {plain_text.decode()}")
