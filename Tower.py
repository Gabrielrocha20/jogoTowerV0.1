from classes.classess import buscarpersona
from classes import classess, statusInimigo
from classes.statusInimigo import gerar_inimigo
from bancodedados.bd import cadastro, update_nivel, update, perde_subnivel
import time
import random


start_game = input('Cadastro[1] Logar[2] Digite o numero que quer: ')
if start_game == '1':
    cadastro()

elif start_game == '2':
    idd = input('Digite o ID do seu Personagem: ')
    buscarpersona(idd)
    print()
    print()
    ini = input('Um inimigo surge a sua frente, você deseja lutar?[s/n]')
    print()
    print()
    if ini == 's':
        gerar_inimigo()
        round_1 = 0
        while round_1 <= 30:
            if classess.pers.vida == 0:
                print('Você Morreu!!!!!!!!')
                perde_subnivel(idd)
                update_nivel(idd)
                break
            elif statusInimigo.inimi.vida == 0:
                print('Inimigo Derrotado!')
                update(idd)
                update_nivel(idd)

                break
            if round_1 % 2 == 1:
                time.sleep(1)
                print('Vez do inimigo atacar ')
                time.sleep(2)
                if classess.result[4] == 'Mago':
                    classess.pers.defesa_base(statusInimigo.atk_ini)
                    print()
                    print()
                if classess.result[4] == 'Assassino':
                    classess.pers.defesa_base(statusInimigo.atk_ini)
                    print()
                    print()
                if classess.result[4] == 'Guerreiro':
                    classess.pers.defesa_base(statusInimigo.atk_ini)
                    print()
                    print()
            else:
                if statusInimigo.classe_aleatoria == 'Mago':
                    luta = input('Sua vez de atacar digite "s" para atacar e "n" para fugir: ')
                    if luta == 's':
                        critico = classess.critico
                        chance = random.randint(0, 500)
                        if chance <= critico * 10:
                            atk = classess.atk * 2.0

                        else:
                            atk = classess.atk
                        statusInimigo.inimi.defesa_base_inimi(atk)
                        print()
                        print()
                    else:
                        print('Voce foge da luta pois previu que nao poderia ganhar')
                        break
                elif statusInimigo.classe_aleatoria == 'Assassino':
                    luta = input('Sua vez de atacar digite "s" para atacar e "n" para fugir: ')
                    print()
                    print()
                    if luta == 's':
                        critico = classess.critico
                        chance = random.randint(0, 500)
                        if chance <= critico * 10:
                            atk = classess.atk * 2.0

                        else:
                            atk = classess.atk
                        statusInimigo.inimi.defesa_base_inimi(atk)
                        print()
                        print()
                    else:
                        print('Voce foge da luta pois previu que nao poderia ganhar')
                        break
                elif statusInimigo.classe_aleatoria == 'Guerreiro':
                    luta = input('Sua vez de atacar digite "s" para atacar e "n" para fugir: ')
                    print()
                    print()
                    if luta == 's':
                        critico = classess.critico
                        chance = random.randint(0, 500)
                        if chance <= critico * 10:
                            atk = classess.atk * 2.0

                        else:
                            atk = classess.atk
                        statusInimigo.inimi.defesa_base_inimi(atk)
                        print()
                        print()
                    else:
                        print('Voce foge da luta pois previu que nao poderia ganhar')
                        break
            round_1 += 1