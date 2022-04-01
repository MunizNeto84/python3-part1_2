import random

print('###############################')
print('BEM VINDO AO JOGO DE ADVINHAÇÃO')
print('###############################')

numero_secreto = random.randrange(1,101)
total_de_tentativas = 3


for rodada in range (1, total_de_tentativas + 1):
    print('tentativa {} de {}'.format(rodada, total_de_tentativas))
    chute_str = input('Digite um numero de 1 a 100: ')
    print('Você digitou ', chute_str)
    chute = int(chute_str)
    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(chute <1 or chute >= 100):
        print ("você deve digitar um numero entre 1 a 100")
        continue

    if (acertou):
        print('Você acertou')
        break
    else:
        if(maior):
            print('Você errou o seu chute foi maior do que o nuemro secreto.')
        elif(menor):
            print('Você errou o seu chute foi menor do que o nuemro secreto.')

    rodada = rodada + 1

print('fim do jogo')