import tkinter as tk
import sqlite3
import pandas as pd

# conexao = sqlite3.connect('banco_clientes.db')
#
# c = conexao.cursor()
#
# c.execute('''CREATE TABLE cliente (
#     nome text,
#     sobrenome text,
#     email text,
#     telefone text
#     )
# ''')
# conexao.commit()
#
# conexao.close()

def cadastrar_cliente():
    conexao = sqlite3.connect('banco_clientes.db')

    c = conexao.cursor()

    c.execute(" INSERT INTO cliente VALUES(:nome, :sobrenome, :email, :telefone)",
        {
            'nome':entry_nome.get(),
            'sobrenome':entry_sobrenome.get(),
            'email':entry_email.get(),
            'telefone':entry_telefone.get()
        }
        )
    conexao.commit()

    conexao.close()

    entry_nome.delete(0,"end")
    entry_sobrenome.delete(0, "end")
    entry_email.delete(0, "end")
    entry_telefone.delete(0, "end")


def exporta_clientes():
    conexao = sqlite3.connect('banco_clientes.db')

    c = conexao.cursor()

    c.execute("SELECT *, oid FROM cliente")
    clientes_cadastros = c.fetchall()
    clientes_cadastros = pd.DataFrame(clientes_cadastros, columns=['nome', 'sobrenome', 'email', 'telefone', 'Id_banco'])
    clientes_cadastros.to_excel('banco_clientes.xlsx')
    conexao.commit()

    conexao.close()

janela = tk.Tk()
janela.title("ferramenta de Cadastro de Clientes")

# Labels:

label_nome = tk.Label(janela, text='Nome')
label_nome.grid(row=0, column=0, padx=10, pady=10)

label_sobrenome = tk.Label(janela, text='Sobrenome')
label_sobrenome.grid(row=1, column=0, padx=10, pady=10)

label_email = tk.Label(janela, text='E-mail')
label_email.grid(row=2, column=0, padx=10, pady=10)

label_telefone = tk.Label(janela, text='Telefone')
label_telefone.grid(row=3, column=0, padx=10, pady=10)

# Entrys:

entry_nome = tk.Entry(janela, text='Nome', width=30)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

entry_sobrenome = tk.Entry(janela, text='Sobrenome', width=30)
entry_sobrenome.grid(row=1, column=1, padx=10, pady=10)

entry_email = tk.Entry(janela, text='E-mail', width=30)
entry_email.grid(row=2, column=1, padx=10, pady=10)

entry_telefone = tk.Entry(janela, text='Telefone', width=30)
entry_telefone.grid(row=3, column=1, padx=10, pady=10)

#Botões:

botao_cadastrar = tk.Button(janela, text='Cadastrar Cliente', command=cadastrar_cliente)
botao_cadastrar.grid(row=4, column=0, padx=10, pady=10, columnspan=2, ipadx=80)

botao_exportar = tk.Button(janela, text='Exportar Base de Cliente', command=exporta_clientes)
botao_exportar.grid(row=5, column=0, padx=10, pady=10,  columnspan=2, ipadx=80)

janela.mainloop()
