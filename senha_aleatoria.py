import random
import string

import tkinter as tk

def gerar_senha():
    tamanho = int(tamanho_entry.get())
    caracteres = ''

    if letras_var.get():
        caracteres += string.ascii_letters

    if numeros_var.get():
        caracteres += string.digits

    if simbolos_var.get():
        caracteres += string.punctuation
    

    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    senha_entry.delete(0, tk.END)
    senha_entry.insert(0, senha)

janela = tk.Tk()
janela.title('Password generator by @johnfrontdev')
janela.geometry('400x250')
tamanho_label = tk.Label(janela, text='Comprimento:', font=("Arial", 13))
tamanho_label.pack()

tamanho_entry = tk.Entry(janela)
tamanho_entry.pack()

letras_var = tk.BooleanVar()
letras_checkbutton = tk.Checkbutton(janela, text='Letras', font=("Arial", 13), variable=letras_var)
letras_checkbutton.pack()

numeros_var = tk.BooleanVar()
numeros_checkbutton = tk.Checkbutton(janela, text='Números', font=("Arial", 13), variable=numeros_var)
numeros_checkbutton.pack()

simbolos_var = tk.BooleanVar()
simbolos_checkbutton = tk.Checkbutton(janela, text='Símbolos', font=("Arial", 13), variable=simbolos_var)
simbolos_checkbutton.pack()

gerar_button = tk.Button(janela, text='Gerar senha', font=("Arial", 13), command=gerar_senha)
gerar_button.pack()

senha_label = tk.Label(janela, text='Senha:', font=("Arial", 13))
senha_label.pack()

senha_entry = tk.Entry(janela, width=30, font=("Arial", 16))
senha_entry.pack()

janela.mainloop()
