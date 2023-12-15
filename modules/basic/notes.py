import os


class Lib_note():
    def __init__(self) -> None:
        pass

    def erro_name(self, text):
        import ctypes

        ctypes.windll.user32.MessageBoxW(0, text, "Alert", 1)


    def search_note(self, name_file):
        folder = 'datas'
        file_name = f'{name_file}.txt'

        file_note = os.path.join(folder, file_name)
        return file_note


    def read_file(self, name_file:str):
        file = self.search_note(name_file)

        with open(file, 'r') as f:
            text = f.read()
            return text


    def save_note(self, name_file, text):
        file = self.search_note(name_file) 
    
        with open(file, 'w') as f:
            f.write(text)


    def check(self, name_file):
        folder_files = os.listdir('datas')

        note_name = f'{name_file}.txt'
        notes = []

        for file in folder_files:
            notes.append(file[:])
        
        if note_name in notes:
            return True
    

    def check_in_save(self, name):
        lista_save = []
        file = self.search_note('save')

        with open(file, 'r') as arquivo:
            for linha in arquivo:
                lista_save.append(linha[:])

        if name in lista_save:
            return True
        else:
            return False
                

    def remove_save(self, name):
        file = self.search_note('save')

        with open(file, 'r') as arquivo:
            linhas = arquivo.readlines()

        with open(file , 'w') as arquivo_modificado:
            for linha in linhas:
                nova_linha = linha.replace(name.strip(), '')  # Remove espaços extras ao redor da palavra
                if nova_linha.strip():  # Verifica se a linha não está vazia após a remoção
                    arquivo_modificado.write(nova_linha)
        



