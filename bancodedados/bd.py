from bancodedados import connect
from classes.classess import buscarpersona
from classes import classess


import random


def bancod(self):
    cursor = connect.con.cursor()
    sql = 'SELECT * FROM jogo'
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    connect.con.close()
    for result in results:
        print(result)


def cadastro():
    raca = 'Humano'
    nome = input('Digite seu nome: ')
    sexo = input('Masculino ou Feminino: ')
    classe = input('Mago\n'
                   'Guerreiro\n'
                   'Assassino\n'
                   'Escolha Uma Classe: ')
    nivel = 1
    subnivel = 5
    cursor = connect.con.cursor()
    sql = f'INSERT INTO jogo (Nome,Sexo,Raça,Classe,Nivel,SubNivel) VALUES ("{nome}","{sexo}"' \
          f',"{raca}","{classe}", "{nivel}","{subnivel}")'
    cursor.execute(sql)
    connect.con.commit()
    userid = cursor.lastrowid
    cursor.close()
    connect.con.close()

    print('Foi Cadastrado o novo usuario de ID:', userid)


def update(id):
    cursor = connect.con.cursor()
    n = random.randint(1, 3)
    print(f'Você subiu {n} SubNiveis')

    sql_sub = f'UPDATE jogo SET Sub = Sub + "{n}" WHERE ID = "{id}"'

    cursor.execute(sql_sub)


def perde_subnivel(id):
    cursor = connect.con.cursor()
    n = random.randint(1, 3)
    print(f'Você Perdeu {n} SubNiveis')

    sql = f'UPDATE jogo SET Sub = Sub - {n} WHERE ID = {id}'

    cursor.execute(sql)


def update_nivel(id):
    global resultado
    cursor = connect.con.cursor()
    sql_select = f'SELECT * FROM jogo WHERE ID = {id}'
    cursor.execute(sql_select)
    resultados = cursor.fetchall()

    for resultado in resultados:
        resultado = list(resultado)
    if resultado[6] >= 10:
        sql = f'UPDATE jogo SET Nivel = Nivel + {1}, Sub = {1} WHERE ID = {resultado[0]}'
        cursor.execute(sql)
        print('Voce subiu de nivel')
    elif resultado[6] == 0:
        sql = f'UPDATE jogo SET Nivel = Nivel - {1}, Sub = {5} WHERE ID = {resultado[0]}'
        cursor.execute(sql)
        print('Voce Caiu de nivel')
    connect.con.commit()

    cursor.close()
    connect.con.close()


'''def cai_nivel():
    if resultado[6] == 0:
        sql = f'UPDATE jogo SET Nivel = Nivel - {1}, Sub = {5} WHERE ID = {resultado[0]}'
        cursor.execute(sql)
        connect.con.commit()
        cursor.close()
        connect.con.close()
        print('Voce Caiu de nivel')'''








