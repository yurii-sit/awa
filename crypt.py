from cryptography.fernet import Fernet

ORIGIN_FILENAME = 'w_default.conf'
KEY_FILE = 'crypto.key'

def write_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as key_file:
        key_file.write(key)

def load_key():
    return open(KEY_FILE, 'rb').read()

def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, 'rb') as file:
            file_data = file.read()

    encrypted_data = f.encrypt(file_data)
    
    with open(filename, 'wb') as file:
        file.write(encrypted_data)            

def decrypt(filename, key):

    f = Fernet(key)
    with open(filename, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename, 'wb') as file:
        file.write(decrypted_data)

key = load_key()
file = ORIGIN_FILENAME
#encrypt(file, key)
#decrypt(file, key)