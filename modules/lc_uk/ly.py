from cryptography.fernet import Fernet
from modules.basic import notes

notes = notes.Lib_note()

class Lock():
    def __init__(self) -> None:
        pass

    def make_crypto(self, name):
        if notes.check('save'):
            if notes.check_in_save(name):
                return 'File Already Modified'
            else:
                file_path = notes.search_note(name)
                file_save = notes.search_note('save')

                key = Fernet.generate_key()
                fernet = Fernet(key)

                with open(file_path, 'rb') as original_file:
                    original = original_file.read()

                encrypted = fernet.encrypt(original)

                with open(file_path, 'wb') as encrypted_file:
                    encrypted_file.write(encrypted)

                with open(file_save, 'a') as file:
                    file.write(f'\n{name}')

                return key
        else:
            file_path = notes.search_note(name)
            file_save = notes.search_note('save')

            key = Fernet.generate_key()
            fernet = Fernet(key)

            with open(file_path, 'rb') as original_file:
                original = original_file.read()

            encrypted = fernet.encrypt(original)

            with open(file_path, 'wb') as encrypted_file:
                encrypted_file.write(encrypted)

            with open(file_save, 'a') as file:
                file.write(f'\n{name}')

            return key
    
            notes.save_note('save', name)

    def remove_crypto(self, name, key):
        try:
            file = notes.search_note(name)

            id = 0
            key = key
            fernet = Fernet(key)
            
            with open(file, 'rb') as enc_file:
                encrypted = enc_file.read()
                id += 1

            decrypted = fernet.decrypt(encrypted)

            with open(file, 'wb') as dec_file:
                dec_file.write(decrypted)
                id += 1

            if id == 2:
                return True
            else:
                return False
                
        except:
            return False




