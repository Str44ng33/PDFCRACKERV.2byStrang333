import os
import tkinter as tk
from tkinter import filedialog, scrolledtext
from tkinter.ttk import Progressbar, Style
import pikepdf
from PIL import Image, ImageTk

def create_interface():
    def browse_pdf():
        pdf_file_path.set(filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")], initialdir=os.path.join(script_dir, 'PDFs')))

    def browse_wordlist():
        wordlist_file_path.set(filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")], initialdir=os.path.join(script_dir, 'Wordlists')))

    def start_cracking():
        pdf_path = pdf_file_path.get()
        wordlist_path = wordlist_file_path.get()
        
        if not pdf_path or not wordlist_path:
            status_text.insert(tk.END, "Erro: Por favor, selecione o arquivo PDF e a lista de senhas.\n")
            return

        if not os.path.exists(pdf_path):
            status_text.insert(tk.END, f"Erro: Arquivo PDF {pdf_path} não encontrado.\n")
            return

        if not os.path.exists(wordlist_path):
            status_text.insert(tk.END, f"Erro: Arquivo de senhas {wordlist_path} não encontrado.\n")
            return

        with open(wordlist_path, "r") as wordlist_file:
            passwords = wordlist_file.read().splitlines()
        
        progress_bar['maximum'] = len(passwords)
        status_text.delete(1.0, tk.END)

        for i, password in enumerate(passwords):
            try:
                with pikepdf.open(pdf_path, password=password):
                    status_text.insert(tk.END, f"Senha encontrada: {password}\n", 'success')
                    return
            except pikepdf.PasswordError:
                progress_bar['value'] = i + 1
                root.update_idletasks()
                status_text.insert(tk.END, f"Tentando senha: {password}\n")
                status_text.see(tk.END)
            except Exception as e:
                status_text.insert(tk.END, f"Erro: {str(e)}\n")
                return

        status_text.insert(tk.END, "Falha: Não foi possível encontrar a senha.\n")

    root = tk.Tk()
    root.title("PDF Cracker")
    root.geometry("800x600")
    root.config(bg='#0d0d0d')

    script_dir = os.path.dirname(__file__)

    icon_image = tk.PhotoImage(file=os.path.join(script_dir, 'pngtree-red-skull-head-png-image_6563601.png'))
    root.iconphoto(True, icon_image)

    style = Style()
    style.configure('TButton',
                    background='#ff0000',
                    foreground='white',
                    font=('Roboto', 10),
                    borderwidth=2,
                    focusthickness=2,
                    focuscolor='none',
                    padding=6)
    style.map('TButton',
              background=[('active', '#e60000')])
    style.configure('TEntry',
                    background='#1e1e1e',
                    foreground='white',
                    font=('Roboto', 10),
                    padding=6)
    style.configure('TLabel',
                    background='#0d0d0d',
                    foreground='white',
                    font=('Roboto', 12))

    pdf_file_path = tk.StringVar()
    wordlist_file_path = tk.StringVar()

    image_path = os.path.join(script_dir, 'Untitled.png')
    image = Image.open(image_path)
    image = image.resize((200, 200), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    
    image_label = tk.Label(root, image=photo, bg='#0d0d0d')
    image_label.photo = photo
    image_label.grid(row=0, column=0, columnspan=3, pady=20, padx=10)

    tk.Label(root, text="Arquivo PDF:", bg='#0d0d0d', fg='white').grid(row=1, column=0, padx=15, pady=10, sticky='w')
    pdf_entry = tk.Entry(root, textvariable=pdf_file_path, width=70)
    pdf_entry.grid(row=1, column=1, padx=15, pady=10, sticky='ew')
    tk.Button(root, text="Procurar", command=browse_pdf).grid(row=1, column=2, padx=15, pady=10)

    tk.Label(root, text="Lista de Senhas:", bg='#0d0d0d', fg='white').grid(row=2, column=0, padx=15, pady=10, sticky='w')
    wordlist_entry = tk.Entry(root, textvariable=wordlist_file_path, width=70)
    wordlist_entry.grid(row=2, column=1, padx=15, pady=10, sticky='ew')
    tk.Button(root, text="Procurar", command=browse_wordlist).grid(row=2, column=2, padx=15, pady=10)

    tk.Button(root, text="Iniciar", command=start_cracking).grid(row=3, column=0, columnspan=3, pady=20)

    progress_bar = Progressbar(root, orient='horizontal', length=750, mode='determinate', style='red.Horizontal.TProgressbar')
    progress_bar.grid(row=4, column=0, columnspan=3, pady=10)

    status_text = scrolledtext.ScrolledText(root, width=80, height=15, bg='#1e1e1e', fg='white', font=('Roboto', 10), borderwidth=2, relief='flat')
    status_text.grid(row=5, column=0, columnspan=3, pady=10)

    style.configure('red.Horizontal.TProgressbar',
                    troughcolor='#555555',
                    background='#ff0000',
                    thickness=20)

    status_text.tag_configure('success', foreground='green')

    tk.Label(root, text="Feito por: https://github.com/Str44ng33 | Matheus 802 CMM", bg='#0d0d0d', fg='white', font=('Roboto', 16)).grid(row=6, column=0, columnspan=3, pady=15)

    root.grid_rowconfigure(5, weight=1)
    root.grid_columnconfigure(1, weight=1)

    root.mainloop()

create_interface()
