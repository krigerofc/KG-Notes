import customtkinter
import os
from modules.lc_uk import ly
from modules.basic import notes

ly = ly.Lock()
notes = notes.Lib_note()

class Tela():
    def __init__(self, name:str):
        self.name = name
        self.elements = 0

    # Destroi o frame da anotação
    def remove_frame(self, janela, nome_arquivo):
        notes.remove_save(nome_arquivo)
        self.elements -= 1
        janela.destroy()

        folder_save_notes  = 'datas'
        nome_arquivo = f'{nome_arquivo}.txt'

        os.remove(os.path.join(folder_save_notes , nome_arquivo))

    def remove_window(self, name):
        remove_crypto = customtkinter.CTk()
        remove_crypto.title('Cryptography')

        largura = 400
        altura = 400
        x = (remove_crypto.winfo_screenwidth() - largura) // 2
        y = (remove_crypto.winfo_screenheight() - altura) // 2
        remove_crypto.geometry(f"{largura}x{altura}+{x+400}+{y-35}")
        remove_crypto.resizable(False,False)
        remove_crypto.iconbitmap(os.path.join(os.path.dirname(__file__), 'assets', 'post.ico'))
        
        def quit_fix():
            remove_crypto.withdraw()
            remove_crypto.quit()

        remove_crypto.protocol("WM_DELETE_WINDOW", quit_fix)
        font = customtkinter.CTkFont(family='title', size=40, weight='bold')

        frame_crypto = customtkinter.CTkFrame(remove_crypto, width=250, height=150, border_color='black')
        frame_crypto.configure(border_width=2, corner_radius=30)  
        frame_crypto.anchor('center')
        frame_crypto.pack(pady=120)

        label_crypto = customtkinter.CTkLabel(frame_crypto, text='Key', font=('title',30))
        label_crypto.configure(
                text_color='gray',
                font=('desc', 20),
                )
        label_crypto.place(relx=0.5, rely=0.2, anchor='center')


        key_value = customtkinter.CTkEntry(frame_crypto, placeholder_text="Key value", width=200, corner_radius=30)
        key_value.anchor('center')
        key_value.place(relx=0.5, rely=0.5, anchor='center')


        button_decrypted = customtkinter.CTkButton(frame_crypto, text='decrypted', width=5, height=30, corner_radius=20, command=lambda:check(key_value.get()))
        button_decrypted.pack_propagate(0)
        button_decrypted.configure(
                            border_width=2,
                            border_color='black',
                            text_color='black',
                            font=('title', 20)
                                )
        button_decrypted.place(relx=0.5, rely=0.8, anchor='center')

        def check(key):
            
            verifc = ly.remove_crypto(name, key)
            if verifc:
                remove_crypto.withdraw()
                remove_crypto.quit()
                self.new_window(name)
            else:
                pass

        remove_crypto.mainloop()

    def crypto_window(self):
        crypto_window = customtkinter.CTk()
        crypto_window.title('Cryptography')

        largura = 400
        altura = 400
        x = (crypto_window.winfo_screenwidth() - largura) // 2
        y = (crypto_window.winfo_screenheight() - altura) // 2
        crypto_window.geometry(f"{largura}x{altura}+{x+400}+{y-35}")
        crypto_window.resizable(False,False)
        crypto_window.iconbitmap(os.path.join(os.path.dirname(__file__), 'assets', 'post.ico'))
        
        def quit_fix():
            crypto_window.withdraw()
            crypto_window.quit()

        crypto_window.protocol("WM_DELETE_WINDOW", quit_fix)
        font = customtkinter.CTkFont(family='title', size=40, weight='bold')

        frame_crypto = customtkinter.CTkFrame(crypto_window, width=250, height=150, border_color='black')
        frame_crypto.configure(border_width=2, corner_radius=30)  
        frame_crypto.anchor('center')
        frame_crypto.pack(pady=120)

        label_crypto = customtkinter.CTkLabel(frame_crypto, text='Insert your note name', font=('title',30))
        label_crypto.configure(
                text_color='gray',
                font=('desc', 20),
                )
        label_crypto.place(relx=0.5, rely=0.2, anchor='center')


        name_file = customtkinter.CTkEntry(frame_crypto, placeholder_text="Note name", corner_radius=30)
        name_file.anchor('center')
        name_file.place(relx=0.5, rely=0.5, anchor='center')


        button_crypto = customtkinter.CTkButton(frame_crypto, text='encrypt', width=5, height=30, corner_radius=20, command=lambda:check(name_file.get()))
        button_crypto.pack_propagate(0)
        button_crypto.configure(
                            border_width=2,
                            border_color='black',
                            text_color='black',
                            font=('title', 20)
                                )
        button_crypto.place(relx=0.5, rely=0.8, anchor='center')

        def check(name):
            nota = notes.check(name)
            if nota:
                frame_crypto.configure(width=380, height=200)

                name_file.destroy()
                button_crypto.destroy()
                
                label_crypto.configure(text='Key:')
                label_crypto.place(relx=0.5, rely=0.2, anchor='center')

                text_box = customtkinter.CTkTextbox(master=frame_crypto, width=360, height=80, corner_radius=20)
                text_box.place(relx=0.5, rely=0.6, anchor='center')

                chave = ly.make_crypto(name)

                text_box.insert("0.0", chave)
            else:
                pass

        crypto_window.mainloop()
        
    # Cria a janela do arquivo aberto
    def new_window(self, name_file:str):
        janela_nota = customtkinter.CTk()
        janela_nota.title(name_file)

        largura = 600
        altura = 600
        x = (janela_nota.winfo_screenwidth() - largura) // 2
        y = (janela_nota.winfo_screenheight() - altura) // 2
        janela_nota.geometry(f"{largura}x{altura}+{x+500}+{y-35}")
        janela_nota.resizable(False,False)
        janela_nota.iconbitmap(os.path.join(os.path.dirname(__file__), 'assets', 'post.ico'))
        
        def quit_fix():
            janela_nota.withdraw()
            janela_nota.quit()

        janela_nota.protocol("WM_DELETE_WINDOW", quit_fix)
        #text box
        text_box = customtkinter.CTkTextbox(master=janela_nota, width=570, height=500, corner_radius=20)
        text_box.pack(pady=20 ,padx=20)
        text = notes.read_file(name_file)
        text_box.insert("0.0", f'{text}')

        #nav bar note
        nav_bar_note = customtkinter.CTkFrame(janela_nota, width=570, height=40, corner_radius=30, border_width=2, border_color='black')
        nav_bar_note.anchor('center')
        nav_bar_note.pack()
        nav_bar_note.pack_propagate(0)

        #save note
        def get_text():
            texto_salvo = text_box.get('0.0', 'end').strip()
            return texto_salvo
            

        save_note = customtkinter.CTkButton(nav_bar_note, text='SAVE', width=5, height=30, corner_radius=20, command=lambda:notes.save_note(name_file, text=get_text()))
        save_note.pack_propagate(0)
        save_note.configure(
                            border_width=2,
                            border_color='black',
                            text_color='black',
                            font=('title', 20)
                            )
        save_note.place(x=476, y=4.5)

        quit_note = customtkinter.CTkButton(nav_bar_note, text='QUIT', width=5, height=30, corner_radius=20, command=lambda:quit_fix())
        quit_note.pack_propagate(0)
        quit_note.configure(
                            border_width=2,
                            border_color='black',
                            text_color='black',
                            font=('title', 20)
                            )
        quit_note.place(x=10, y=4.5)
        janela_nota.mainloop()
        

    # Cria o frame que mostra as notas
    def frame_note(self, master, name='', file=False):
        if file == False:
            dialog = customtkinter.CTkInputDialog(text='Note name:', title='Note name')
            dialog.iconbitmap(os.path.join(os.path.dirname(__file__), 'assets', 'post.ico'))

            name = dialog.get_input()

        folder_save_notes = 'datas'

        if self.elements <= 3 and len(os.listdir(folder_save_notes)) <= 4:
            try:
                if file == False:
                    with open (os.path.join(folder_save_notes, f'{name.lower()}.txt'), 'x'):
                        pass              
                self.elements += 1

                frame_note = customtkinter.CTkFrame(master, width=370, height=100, border_color='black')
                frame_note.configure(border_width=2, corner_radius=30)  
                frame_note.anchor('center')
                frame_note.pack(pady=20)

                title_frame = customtkinter.CTkLabel(frame_note, text=name.lower(), font=('title',30))
                title_frame.place(x=20, y=10)

                Remove_button = customtkinter.CTkButton(frame_note, text='Remove', width=10, height=30, corner_radius=20, command=lambda:self.remove_frame(frame_note, name))
                Remove_button.pack_propagate(0)
                Remove_button.configure(
                                text_color='black',
                                font=('title', 20),
                                border_width=2,
                                border_color='black',
                                )
                Remove_button.place(x=250, y=15)

                note = customtkinter.CTkLabel(frame_note, text='Insert your notes here', font=('title',30))
                note.configure(
                    text_color='gray',
                    font=('desc', 20),
                )
                note.place(x=20, y=50)

                def safe():
                    if notes.check_in_save(name):
                        self.remove_window(name)
                    else:
                        self.new_window(name)

                open_button = customtkinter.CTkButton(frame_note, text='Open', width=10, height=30, corner_radius=20, command=lambda:safe())
                open_button.pack_propagate(0)
                open_button.configure(
                                text_color='black',
                                font=('title', 20),
                                border_width=2,
                                border_color='black',
                                )
                open_button.place(x=270, y=55)
            except:
                pass
        else:
            pass

    # Cria a janela do app
    def run(self):
        window = customtkinter.CTk()
        window.title(self.name)

        largura = 400
        altura = 670
        x = (window.winfo_screenwidth() - largura) // 2
        y = (window.winfo_screenheight() - altura) // 2
        window.geometry(f"{largura}x{altura}+{x}+{y}")
        window.resizable(False,False)

        window.iconbitmap(os.path.join(os.path.dirname(__file__), 'assets', 'post.ico'))
        
        def quit_fix():
            window.quit()

        window.protocol("WM_DELETE_WINDOW", quit_fix)


        # Barra
        font = customtkinter.CTkFont(family='title', size=40, weight='bold')
        
        nav_bar = customtkinter.CTkFrame(window, width=400, height=40, corner_radius=30, border_width=2, border_color='black')
        nav_bar.anchor('center')
        nav_bar.pack()
        nav_bar.pack_propagate(0)
    
        make_note = customtkinter.CTkButton(nav_bar, text='+', width=5, height=30, corner_radius=20, command=lambda:self.frame_note(window))
        make_note.pack_propagate(0)
        make_note.configure(
                              border_width=2,
                              border_color='black',
                              text_color='black',
                              font=('title', 20)
                              )
        make_note.place(x=10, y=4.5)

        def prt():
            print('opa')

        #tools_button = customtkinter.Ctk
        cryptography_button = customtkinter.CTkButton(nav_bar, text='Cryptography', width=5, height=30, corner_radius=20, command=lambda:self.crypto_window())
        cryptography_button.pack_propagate(0)
        cryptography_button.configure(
                                border_width=2,
                                border_color='black',
                                text_color='black',
                                font=('title', 20)
                              )
        cryptography_button.place(x=239, y=4.5)

        folder_files = os.listdir('datas')
        for file in folder_files:
            if file != 'save.txt':
                self.frame_note(window, name=file[:-4], file=True)
        

        window.mainloop()

