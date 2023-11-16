import PySimpleGUI as sg
import sqlite3 as sql

sg.theme("DarkBlue4")

conn = sql.connect("db.sqlite3")

cursor = conn.cursor()

cursor.execute("create table if not exists users (nome varchar(255), telefone varchar(255)); ")

layout = [   

    [sg.Text("Nome")],
    [sg.Input(key="nome")],
    [sg.Text("Telefone")],
    [sg.Input(key="fone")],
    [sg.Button("Salvar")],
    [sg.Button("Pesquisar por Nome")],
    [sg.Button("Deletar")]

    ]

window = sg.Window("Tela de Gestão", layout=layout)

while True:
    events, values = window.read()

    if events == "Salvar":

        if len(values["nome"]) > 0:
            if len(values["fone"]) > 0:
                cursor.execute(f"insert into users (nome, telefone) values (?, ?);",(values['nome'], values['fone']))
                conn.commit()

    if events == "Pesquisar por Nome":
        lista = list(cursor.execute("select * from users where nome = ? limit 5", (values["nome"],)))

        lista_str = ''
        for i,a in lista:
            lista_str += i+","+a+"\n\n"


        sg.popup(lista_str)

    if events == "Deletar":
        cursor.execute("delete from users where nome = ? ;", (values["nome"],))

    if events == sg.WIN_CLOSED:
        break
