import random
from classes.recursos import Personagem
from bancodedados import connect
# from projeto.testes.bancodedados.bd import perde_subnivel, update_nivel


class Assassino(Personagem):
    def __init__(self, nome, nivel, ataque, subnivel):
        super().__init__(nome, nivel, ataque, subnivel)
        if self.nivel <= 10:
            self._vida = self.nivel * (7 + self.nivel)
        else:
            self._vida = self.nivel * (9 + self.nivel)
        self.ataque = ataque
        self.defesa = self.nivel * 3
        self.agilidade = self.nivel * 6
        self.nivel = nivel
        self.subnivel = subnivel
        self.critico = 0.5 * self.nivel

    def perfil(self, **kwargs):
        print('----------Perfil----------')
        print(f'Titulo:{self.titulos} |Classe: Assassino')
        print('----------Atributos----------')
        print(f'Ataque: {self.ataque} |Defesa: {self.defesa}')
        print(f'Agilidade: {self.agilidade} | Critico : {self.critico:.2f}%')

    def detalhes(self, **kwargs):
        self.classe = 'Assassino'
        print(f'Classe: {self.classe}')
        print(f'Nome: {self.nome} | Nvl: {self.nivel}')
        print(f'SubNivel:  {self.subnivel}')
        print(f'Vida: {self.vida:.1f}')

    def defesa_base(self, ataque):
        defesa = ataque - (self.defesa / 100) * ataque
        if defesa >= self._vida:
            self.vida = 0
            print()
            print(f'Você levou {defesa:.2f} de dano')
            print()
            print('Você foi derrotado!')
            print()
            #perde_subnivel(result[0])
            #update_nivel(result[0])
            self.detalhes()

        else:
            self.vida -= defesa
            print()
            print(f'Você levou {defesa:.2f} de dano')
            print()
            self.detalhes()
            self.perfil()


class Mago(Personagem):

    def __init__(self, nome, nivel, ataque, subnivel):
        super().__init__(nome, nivel, ataque, subnivel)
        if self.nivel <= 10:
            self._vida = self.nivel * (6 + self.nivel)
        else:
            self._vida = self.nivel * (10 + self.nivel)
        self.ataque = ataque
        self.defesa = 4 * self.nivel
        self.agilidade = 2 * self.nivel
        self.nome = nome
        self.nivel = nivel
        self.subnivel = subnivel
        self.critico = 0.7 * self.nivel

    @property
    def vida(self):

        return self._vida

    @vida.setter
    def vida(self, valor):
        self._vida = valor

    def perfil(self, **kwargs):
        print('----------Perfil----------')
        print(f'Titulo:{self.titulos} | Classe: Mago')
        print('----------Atributos----------')
        print(f'Ataque: {self.ataque} | Defesa: {self.defesa}')
        print(f'Agilidade: {self.agilidade} | Critico : {self.critico:.2f}%')

    def detalhes(self):
        self.classe = 'Mago'

        print(f'Classe: {self.classe}')
        print(f'Nome: {self.nome} | Nvl: {self.nivel}')
        print(f'SubNivel:  {self.subnivel}')
        print(f'Vida: {self.vida:.1f}')

    def defesa_base(self, ataque):
        defesa = ataque - (self.defesa / 100) * ataque
        if defesa >= self._vida:
            self.vida = 0
            print()
            print(f'Você levou {defesa:.2f} de dano')
            print()
            print('Você foi derrotado!')
            print()
            self.detalhes()

        else:
            self.vida -= defesa
            print()
            print(f'Você levou {defesa:.2f} de dano')
            print()
            self.detalhes()
            self.perfil()


class Guerreiro(Personagem):

    def __init__(self, nome, nivel, ataque, subnivel):
        super().__init__(nome, nivel, ataque, subnivel)
        if self.nivel <= 10:
            self._vida = self.nivel * (9 + self.nivel)
        else:
            self._vida = self.nivel * (16 + self.nivel)
        self.ataque = ataque
        self.defesa = self.nivel * 6
        self.agilidade = self.nivel * 2.75
        self.nivel = nivel
        self.subnivel = subnivel
        self.critico = 0.3 * self.nivel

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, valor):
        self._vida = valor

    def perfil(self, **kwargs):
        print('----------Perfil----------')
        print(f'Titulo:{self.titulos} | Classe: Guerreiro')
        print('----------Atributos----------')
        print(f'Ataque: {self.ataque}   | Defesa: {self.defesa}')
        print(f'Agilidade: {self.agilidade} | Critico : {self.critico:.2f}%')

    def detalhes(self, **kwargs):
        self.classe = 'Guerreiro'

        print(f'Classe: {self.classe}')
        print(f'Nome: {self.nome} | Nvl: {self.nivel}')
        print(f'SubNivel:  {self.subnivel}')
        print(f'Vida: {self.vida:.1f}')

    def defesa_base(self, ataque):
        defesa = ataque - (self.defesa / 100) * ataque
        if defesa >= self._vida:
            self.vida = 0
            print()
            print(f'Você levou {defesa:.2f} de dano')
            print()
            print('Você foi derrotado!')
            print()
            #perde_subnivel(result[0])
            #update_nivel(result[0])
            self.detalhes()
        else:
            self.vida -= defesa
            print()
            print(f'Você levou {defesa:.2f} de dano')
            print()
            self.detalhes()
            self.perfil()


result = []
pers = None
atk = 0
user = None
critico = 0

def buscarpersona(idd):
    global pers, result, atk, user, critico

    user = idd
    cursor = connect.con.cursor()
    sql = f'SELECT * FROM jogo WHERE ID = {user}'
    cursor.execute(sql)
    resultados = cursor.fetchall()
    if not user in sql:
        cursor.close()
        connect.con.close()
        print('Nada a informar')
    elif not user.isdigit():
        cursor.close()
        connect.con.close()
        print('Nada a informar')
    # cursor.close()
    # connect.con.close()
    for result in resultados:
        result = list(result)

    if result[4] == 'Mago':
        critico = 0.7 * result[5]
        atk = 7 * result[5]
        pers = Mago(result[1], result[5], atk, result[6])
        pers.detalhes()
        pers.perfil()
    elif result[4] == 'Guerreiro':
        critico = 0.3 * result[5]
        atk = 4 * result[5]
        pers = Guerreiro(result[1], result[5], atk, result[6])
        pers.detalhes()
        pers.perfil()
    elif result[4] == 'Assassino':
        critico = 0.5 * result[5]
        atk = 5 * result[5]

        pers = Assassino(result[1], result[5], atk, result[6])
        pers.detalhes()
        pers.perfil()
