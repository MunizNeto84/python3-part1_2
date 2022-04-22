
from operator import index


def jogar():
    print('###############################')
    print('BEM VINDO AO JOGO DE ADVINHAÇÃO')
    print('###############################')
    print('fim do jogo')

    palavra_secreta = 'palavrer'.upper()
    letras_acertadas = ['_' for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)
    
    while(not enforcou and not acertou):
        chute = input('Qual letra? ')
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra   
                index += 1
        else:
            erros += 1  

        enforcou = erros == 6
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print('vc ganhou')
    else:
        print('vc perdeu!!')    
    
    print('fim do jogo')


if(__name__ == '__main__'):
    jogar()    