# Gerador de Senhas Aleatórias em Python

Este é um projeto em Python que tem como objetivo gerar senhas aleatórias e seguras para os usuários. O programa utiliza uma variedade de caracteres, incluindo letras maiúsculas e minúsculas, números e símbolos, para criar senhas fortes e difíceis de serem adivinhadas. Foi meu primeiro projeto em Python e me ajudou a praticar o uso de strings, números aleatórios e estruturas de repetição.



## Aqui está o código com comentários explicando cada linha:

import random  # Importa o módulo random para gerar números aleatórios.
import string  # Importa o módulo string para obter caracteres ASCII.

import tkinter as tk  # Importa o módulo tkinter para criar a interface gráfica.

def gerar_senha():
    tamanho = int(tamanho_entry.get())  # Obtém o comprimento da senha a partir do widget Entry.
    caracteres = ''  # Inicializa uma string vazia para armazenar os caracteres que serão usados na senha.

    if letras_var.get():  # Verifica se a variável BooleanVar letras_var é verdadeira.
        caracteres += string.ascii_letters  # Adiciona as letras maiúsculas e minúsculas à string de caracteres.

    if numeros_var.get():  # Verifica se a variável BooleanVar numeros_var é verdadeira.
        caracteres += string.digits  # Adiciona os dígitos numéricos à string de caracteres.

    if simbolos_var.get():  # Verifica se a variável BooleanVar simbolos_var é verdadeira.
        caracteres += string.punctuation  # Adiciona os símbolos de pontuação à string de caracteres.

    senha = ''.join(random.choice(caracteres) for i in range(tamanho))  # Gera uma senha aleatória com os caracteres selecionados.
    senha_entry.delete(0, tk.END)  # Limpa o widget Entry da senha anterior.
    senha_entry.insert(0, senha)  # Insere a nova senha no widget Entry.

janela = tk.Tk()  # Cria uma nova janela principal.
janela.title('Gerador de Senha')  # Define o título da janela.
janela.geometry('300x200')  # Define as dimensões da janela.

tamanho_label = tk.Label(janela, text='Comprimento da senha:')  # Cria um rótulo para o comprimento da senha.
tamanho_label.pack()  # Adiciona o rótulo à janela.

tamanho_entry = tk.Entry(janela)  # Cria um widget Entry para inserir o comprimento da senha.
tamanho_entry.pack()  # Adiciona o widget Entry à janela.

letras_var = tk.BooleanVar()  # Cria uma variável BooleanVar para as letras.
letras_checkbutton = tk.Checkbutton(janela, text='Letras', variable=letras_var)  # Cria um botão de seleção para as letras.
letras_checkbutton.pack()  # Adiciona o botão de seleção à janela.

numeros_var = tk.BooleanVar()  # Cria uma variável BooleanVar para os números.
numeros_checkbutton = tk.Checkbutton(janela, text='Números', variable=numeros_var)  # Cria um botão de seleção para os números.
numeros_checkbutton.pack()  # Adiciona o botão de seleção à janela.

simbolos_var = tk.BooleanVar()  # Cria uma variável BooleanVar para os símbolos.
simbolos_checkbutton = tk.Checkbutton(janela, text='Símbolos', variable=simbolos_var)  # Cria um botão de seleção para os símbolos.
simbolos_checkbutton.pack()  # Adiciona o botão de seleção à janela.

gerar_button = tk.Button(janela, text='Gerar Senha', command=gerar_senha)  # Cria um botão para gerar a senha.
gerar_button.pack()  # Adiciona o botão à janela.

senha_label = tk.Label(janela, text='Senha:')  # Cria um rótulo para a senha gerada.
senha_label.pack()  # Adiciona o rótulo à janela.

senha_entry = tk.Entry(janela)  # Cria um widget Entry para exibir a senha gerada.
senha_entry.pack()  # Adiciona o widget Entry à janela.

janela.mainloop()  # Inicia o loop principal da interface gráfica.

