
from operator import index


def jogar():
    print('###############################')
    print('BEM VINDO AO JOGO DE ADVINHAÇÃO')
    print('###############################')
    print('fim do jogo')

    palavra_secreta = 'banana'
    enforcou = False
    acertou = False

    
    while(not enforcou and not acertou):
        chute = input('Qual letra?')
        chute = chute.strip()
        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper):
                print('Encontrei a letra {} na posição {}.'.format(letra, index))  
            index = index + 1    

    print('Fim do jogo')


if(__name__ == '__main__'):
    jogar()    