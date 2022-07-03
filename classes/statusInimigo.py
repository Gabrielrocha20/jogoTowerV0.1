from classes.recursos import Inimigo
from classes import classess

import random


class MagoInimigo(Inimigo):
    def __init__(self, nivel, ataque):
        super().__init__(nivel, ataque)
        if nivel == 1:
            self.nivel = random.randint(nivel, nivel + 2)
        else:
            self.nivel = random.randint(nivel - 2, nivel + 2)
        self.classe = None
        self.agilidade = random.randint(1, 3) * self.nivel
        self.ataqueI = ataque
        self.defesaI = random.randint(3, 5) * self.nivel
        self._vida = self.nivel * (random.randint(4, 9) + self.nivel)
        self._raca = self.raca
        self.media = (self.ataqueI + self.agilidade + self.defesaI) / (3 * self.nivel)
        if self.nivel >= 10:
            self.titulo = f'Chefe dos {self._raca}' if self.media > 4.5 else ''
        else:
            self.titulo = ''

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, valor):
        self._vida = valor

    def perfil_inimigo(self, classe, **kwargs):
        self.classe = classe
        print('-' * 8 + 'Perfil' + '-' * 8)
        print(f'Titulo: {self.titulo}')
        print(f'Raça: {self._raca} |', end=' ')
        print(f'Classe: {self.classe}')
        print('-' * 8 + 'Atributos' + '-' * 8)
        print(f'Ataque: {self.ataqueI} | Defesa: {self.defesaI}')
        print(f'Agilidade: {self.agilidade}')

    def detalhes_inimigo(self, **kwargs):
        if 'Chefe' in self.titulo:
            print(f'Nome: Cretus | NvL: {self.nivel}')
        else:
            print(f'Nome: {self.titulo} {self._raca} | NvL: {self.nivel}')
        print(f'Vida: {self._vida:.0f}')

    def defesa_base_inimi(self, ataque):
        defesa = ataque - (self.defesaI / 100) * ataque
        crit = classess.atk * 2
        if defesa >= self.vida:
            if ataque == crit:
                print('Voce causou Dano Critico')
            print(f'Você causou {defesa:.0f} de dano')
            print()
            self.vida = 0
            print('Você derrotou o inimigo')
            print()
            self.detalhes_inimigo()
        else:
            self.vida -= defesa
            if ataque == crit:
                print('Voce causou Dano Critico')
            print(f'Você causou {defesa:.0f} de dano')
            print()
            self.detalhes_inimigo()
            self.perfil_inimigo('Mago')


class AssassinoInimigo(Inimigo):
    def __init__(self, nivel, ataque):
        super().__init__(nivel, ataque)
        if nivel == 2:
            self.nivel = random.randint(nivel, nivel + 2)
        else:
            self.nivel = random.randint(nivel - 2, nivel + 2)
        self.classe = None
        self.agilidade = random.randint(5, 8) * self.nivel
        self.ataqueI = ataque
        self.defesaI = random.randint(2, 4) * self.nivel
        self._vida = self.nivel * (random.randint(4, 9) + self.nivel)
        self._raca = self.raca
        self.media = (self.ataqueI + self.agilidade + self.defesaI) / (3 * self.nivel)
        if self.nivel >= 10:
            self.titulo = f'Chefe dos {self._raca}' if self.media > 4.5 else ''
        else:
            self.titulo = ''

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, valor):
        self._vida = valor

    def perfil_inimigo(self, classe, **kwargs):
        self.classe = classe
        print('-' * 8 + 'Perfil' + '-' * 8)
        print(f'Titulo: {self.titulo}')
        print(f'Raça: {self._raca} |', end=' ')
        print(f'Classe: {self.classe}')
        print('-' * 8 + 'Atributos' + '-' * 8)
        print(f'Ataque: {self.ataqueI} | Defesa: {self.defesaI}')
        print(f'Agilidade: {self.agilidade}')

    def detalhes_inimigo(self, **kwargs):
        if 'Chefe' in self.titulo:
            print(f'Nome: Cretus | NvL: {self.nivel}')
        else:
            print(f'Nome: {self.titulo} {self._raca} | NvL: {self.nivel}')
        print(f'Vida: {self._vida:.0f}')

    def defesa_base_inimi(self, ataque):
        defesa = ataque - (self.defesaI / 100) * ataque
        crit = classess.atk * 2
        if defesa >= self.vida:
            if ataque == crit:
                print('Voce causou Dano Critico')
            self.vida = 0
            print(f'Você causou {defesa:.0f} de dano')
            print()
            print('Você derrotou o inimigo')
            print()
            self.detalhes_inimigo()
        else:
            if ataque == crit:
                print('Voce causou Dano Critico')
            self.vida -= defesa
            print(f'Você causou {defesa:.0f} de dano')
            print()
            self.detalhes_inimigo()
            self.perfil_inimigo('Assassino')


class Guerreiroinimigo(Inimigo):
    def __init__(self, nivel, ataque):
        super().__init__(nivel, ataque)
        if nivel == 1:
            self.nivel = random.randint(nivel, nivel + 2)
        else:
            self.nivel = random.randint(nivel - 2, nivel + 2)
        self.classe = None
        self.agilidade = random.randint(2, 4) * self.nivel
        self.ataqueI = ataque + nivel
        self.defesaI = random.randint(4, 7) * self.nivel
        self._vida = self.nivel * (random.randint(4, 9) + self.nivel)
        self._raca = self.raca
        self.media = (self.ataqueI + self.agilidade + self.defesaI) / (3 * self.nivel)
        if self.nivel >= 10:
            self.titulo = f'Chefe dos {self._raca}' if self.media > 4.5 else ''
        else:
            self.titulo = ''
    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, valor):
        self._vida = valor

    def perfil_inimigo(self, classe, **kwargs):
        self.classe = classe
        print('-' * 8 + 'Perfil' + '-' * 8)
        print(f'Titulo: {self.titulo}')
        print(f'Raça: {self._raca} |', end=' ')
        print(f'Classe: {self.classe}')
        print('-' * 8 + 'Atributos' + '-' * 8)
        print(f'Ataque: {self.ataqueI} | Defesa: {self.defesaI}')
        print(f'Agilidade: {self.agilidade}')
        print(f'')

    def detalhes_inimigo(self, **kwargs):
        if 'Chefe' in self.titulo:
            print(f'Nome: Cretus | NvL: {self.nivel}')
        else:
            print(f'Nome: {self.titulo} {self._raca} | NvL: {self.nivel}')
        print(f'Vida: {self._vida:.0f}')

    def defesa_base_inimi(self, ataque):
        defesa = ataque - (self.defesaI / 100) * ataque
        crit = classess.atk * 2
        if defesa >= self.vida:
            if ataque == crit:
                print('Voce causou Dano Critico')
            print(f'Você causou {defesa:.0f} de dano')
            print()
            self.vida = 0
            print('Você derrotou o inimigo')
            print()
            self.detalhes_inimigo()
        else:
            if ataque == crit:
                print('Voce causou Dano Critico')
            self.vida -= defesa
            print(f'Você causou {defesa:.0f} de dano')
            print()
            self.detalhes_inimigo()
            self.perfil_inimigo('Guerreiro')


classe_aleatoria = random.choice(['Assassino', 'Mago', 'Guerreiro'])
atk_ini = 0
inimi = None


def gerar_inimigo():
    global atk_ini, inimi
    nv = classess.result[5]
    if classe_aleatoria == 'Assassino':
        atk_ini = random.randint(4, 6) * nv
        inimi = AssassinoInimigo(nv, atk_ini)
        inimi.detalhes_inimigo()
        inimi.perfil_inimigo('Assassino')
    elif classe_aleatoria == 'Mago':
        atk_ini = random.randint(4, 9) * nv
        inimi = MagoInimigo(nv, atk_ini)
        inimi.detalhes_inimigo()
        inimi.perfil_inimigo('Mago')
    elif classe_aleatoria == 'Guerreiro':
        atk_ini = random.randint(4, 6) * nv
        inimi = Guerreiroinimigo(nv, atk_ini)
        inimi.detalhes_inimigo()
        inimi.perfil_inimigo('Guerreiro')
