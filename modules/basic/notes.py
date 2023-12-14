import os


class Lib_note():
    def __init__(self) -> None:
        pass

    def search_note(self, name_file):
        try:
            folder = 'datas'
            file_name = f'{name_file}.txt'
            print(f'{file_name} TESTE')

            file_note = os.path.join(folder, file_name)
            return file_note
        except:
            pass

    def read_file(self, name_file:str):
        try:
            file = self.search_note(name_file)

            with open(file, 'r') as f:
                text = f.read()
                print(text)
                return text
        except:
            pass
        

    def save_note(self, name_file, text):
        try:
            file = self.search_note(name_file) 
        
            print(f'texto:{text}')
            with open(file, 'w') as f:
                f.write(text)
        except:
            pass
