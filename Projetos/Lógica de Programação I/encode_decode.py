import tkinter as tk
from tkinter import ttk, messagebox

# Encode Text Function
def encode_text(text: str, key: str) -> str:
    # Reverse key
    key = key[::-1]
    encode_text = ''
    key_index = 0
    '''
    Encode text receive (ascii num of text) + (ascii num of key) on limited range (33, 126)
    '''
    for letter in text:
        encode_text += chr(((ord(letter) + ord(key[key_index])) % 127) + 33)
        key_index += 1
        if key_index >= len(key):
            key_index = 0

    return encode_text

# Decode Text Function
def decode_text(text: str, key: str) -> str:
    # Reverse key
    key = key[::-1]
    decode_text = ''
    key_index = 0
    '''
    Decode text receive (ascii num of text) - (ascii num of key) on limited range (33, 126)
    '''
    for letter in text:
        decode_text += chr(((ord(letter) - ord(key[key_index])) - 33) % 127)
        key_index += 1
        if key_index >= len(key):
            key_index = 0

    return decode_text


# Class Window Interface
class Window(tk.LabelFrame):
    def __init__(self, parent) -> None:
        self.parent = parent
        super(Window, self).__init__(parent)
        self.menu = tk.Menu(self.winfo_toplevel())

        # Frames
        self.main_frame = ttk.Frame()
        self.encode_frame = ttk.Frame()
        self.decode_frame = ttk.Frame()

        self.main_screen()

    # Forget all frames
    def forget_all(self):
        self.main_frame.pack_forget()
        self.encode_frame.pack_forget()
        self.decode_frame.pack_forget()

    # Screen of encode
    def encode_screen(self):
        self.forget_all()
        self.encode_frame.pack()

        # Label Title
        ttk.Label(self.encode_frame, text='Codificador', font='Raleway').grid(
            row=0, column=0, padx=10, pady=5)

        # Label Key
        ttk.Label(self.encode_frame, text='Chave').grid(
            row=1, column=0, pady=5, sticky='w')

        # Entry Key
        self.key_encode = ttk.Entry(
            self.encode_frame, cursor='xterm', width=40)
        self.key_encode.grid(row=2, column=0, columnspan=2, pady=2, sticky='w')

        # Label Text
        ttk.Label(self.encode_frame, text='Texto:').grid(
            row=3, column=0, pady=5, sticky='w')

        # Tex Box + Scrollbar Text
        self.sb_encode = tk.Scrollbar(self.encode_frame, orient='vertical')
        self.sb_encode.grid(row=4, column=1, sticky="wns")
        self.lb_encode = tk.Text(self.encode_frame,
                                 yscrollcommand=self.sb_encode.set, width=30, wrap=tk.WORD, border=0.5)

        self.lb_encode.tag_configure('bold', font=('Arial', 12, 'bold'))
        self.lb_encode.tag_add("center", 1.0, "end")
        self.lb_encode.tag_add("left", 1.0, "end")
        self.lb_encode.configure(height=15)
        self.lb_encode.grid(row=4, column=0, pady=5, sticky="e")
        self.sb_encode.config(command=self.lb_encode.yview, width=20)
        self.lb_encode['bg'] = '#f6f6f6'

        # Button Back
        ttk.Button(self.encode_frame, text='Voltar ao Início', cursor='hand2',
                   command=self.main_screen).grid(row=5, column=0, sticky='w')

        # Button Encode
        ttk.Button(self.encode_frame, text='Codificar Texto', cursor='hand2', command=self.encode).grid(
            row=5, column=0, sticky='e', pady=5)

    # Screen of decode
    def decode_screen(self):
        self.forget_all()
        self.decode_frame.pack()

        # Label Title
        ttk.Label(self.decode_frame, text='Decodificador', font='Raleway').grid(
            row=0, column=0, padx=10, pady=5)

        # Label Key
        ttk.Label(self.decode_frame, text='Chave').grid(
            row=1, column=0, pady=5, sticky='w')

        # Entry Key
        self.key_decode = ttk.Entry(
            self.decode_frame, cursor='xterm', width=40)
        self.key_decode.grid(row=2, column=0, columnspan=2, pady=2, sticky='w')

        # Label Text
        ttk.Label(self.decode_frame, text='Texto:').grid(
            row=3, column=0, padx=10, pady=5, sticky='w')

        # Tex Box + Scrollbar Text
        self.sb_decode = tk.Scrollbar(self.decode_frame, orient='vertical')
        self.sb_decode.grid(row=4, column=1, sticky="wns")
        self.lb_decode = tk.Text(self.decode_frame,
                                 yscrollcommand=self.sb_decode.set, width=30, wrap=tk.WORD, border=0.5)

        self.lb_decode.tag_configure('bold', font=('Arial', 12, 'bold'))
        self.lb_decode.tag_add("left", 1.0, "end")
        self.lb_decode.configure(height=15)
        self.lb_decode.grid(row=4, column=0, pady=5, sticky="e")
        self.sb_decode.config(command=self.lb_decode.yview, width=20)
        self.lb_decode['bg'] = '#f6f6f6'

        # Button Back
        ttk.Button(self.decode_frame, text='Voltar ao Início', cursor='hand2',
                   command=self.main_screen).grid(row=5, column=0, sticky='w')

        # Button Encode
        ttk.Button(self.decode_frame, text='Decodificar Texto', cursor='hand2', command=self.decode).grid(
            row=5, column=0, sticky='e', pady=10)

    # Main Screen
    def main_screen(self):
        self.forget_all()
        self.main_frame.pack()
        # Label Title
        ttk.Label(self.main_frame, text='Início', font='Raleway').grid(
            row=0, column=0, pady=5)
        ttk.Label(self.main_frame, text='Selecione uma das opções abaixo:').grid(
            row=1, column=0, pady=50)

        # Button Encode
        ttk.Button(self.main_frame, text='Codificar', cursor='hand2',
                   command=self.encode_screen).grid(row=2, column=0, sticky='n', pady=10)

        # Button Decode
        ttk.Button(self.main_frame, text='Decodificar', cursor='hand2',
                   command=self.decode_screen).grid(row=3, column=0, sticky='n', pady=10)

        # Button Quit
        ttk.Button(self.main_frame, text='Sair', cursor='hand2',
                   command=quit).grid(row=4, column=0, sticky='n', pady=10)

    # Manages Encode text and show
    # Call encode function and call open new window
    def encode(self):
        if (self.key_encode.get() == ''):
            messagebox.showerror(
                title='Erro', message='A chave não pode estar vazia')
            return
        else:
            encode_txt = encode_text(self.lb_encode.get(
                "1.0", tk.END).strip(), self.key_encode.get())
            try:
                self.new_root.winfo_exists()
                return
            except:
                pass

            self.open_new_window('Codificação', encode_txt)

    # Manages decode text and show
    # Call decode function and call open new window
    def decode(self):
        if (self.key_decode.get() == ''):
            messagebox.showerror(
                title='Erro', message='A chave não pode estar vazia')
            return
        else:
            decode_txt = decode_text(self.lb_decode.get(
                "1.0", tk.END).strip(), self.key_decode.get())
            try:
                self.new_root.winfo_exists()
                return
            except:
                pass

            self.open_new_window('Decodificação', decode_txt)

    # Open new window to show text (encoded or decoded)
    def open_new_window(self, mode, text):
        new_window = tk.Toplevel(root)

        new_window.title('Resultado')
        new_window.geometry(
            f'350x310+{SET_WINDOW_POSITION_X + 310}+{SET_WINDOW_POSITION_Y}')
        new_window.minsize(350, 310)
        new_window.maxsize(350, 310)
        new_window.iconbitmap(
            './Projetos/Lógica de Programação I/images/icon.ico')

        ttk.Label(new_window, text=f'Resultado da {mode}:',
                  font='Raleway').grid(row=0, column=0, columnspan=2, pady=10)

        # Tex Box + Scrollbar Text
        sb = tk.Scrollbar(new_window, orient='vertical')
        sb.grid(row=1, column=1, sticky="wns")
        lb = tk.Text(new_window,
                     yscrollcommand=sb.set, width=37, wrap=tk.WORD, border=0.5)

        lb.tag_configure('bold', font=('Arial', 12, 'bold'))
        lb.tag_add("left", 1.0, "end")
        lb.delete("1.0", tk.END)
        lb.insert(tk.END, text)
        lb.configure(height=15, state='disabled')
        lb.grid(row=1, column=0, pady=5, padx=10, sticky="e")
        sb.config(command=lb.yview, width=20)
        lb['bg'] = '#f6f6f6'

# Calculate a center of window to show it
def center_window(width=300, height=200):
    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)

    return int(x), int(y)


SET_WINDOW_POSITION_X = 0
SET_WINDOW_POSITION_Y = 0

if __name__ == '__main__':
    root = tk.Tk()
    SET_WINDOW_POSITION_X, SET_WINDOW_POSITION_Y = center_window(300, 420)
    window = Window(root)
    root.title('(Des)Encrypt')
    root.geometry(f'300x420+{SET_WINDOW_POSITION_X}+{SET_WINDOW_POSITION_Y}')
    root.minsize(300, 420)
    root.maxsize(300, 420)
    root.iconbitmap('./Projetos/Lógica de Programação I/images/icon.ico')
    root.mainloop()
