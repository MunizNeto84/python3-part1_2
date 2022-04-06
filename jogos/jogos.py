import forca
import advinhacao

def jogar():
    print('###############################')
    print('##### Escolha o seu jogo ######')
    print('###############################')

    print('(1)Forca (2)Advinhação')

    jogo = int(input('Qual jogo: '))

    if(jogo == 1):
        print('Jogando forca')
        forca.jogar()
    elif(jogo == 2):
        print('Jogando advinhação') 
        advinhacao.jogar()  

    print('fim do jogo')

if(__name__ == '__main__'):
    jogar()