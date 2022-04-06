import random

print('###############################')
print('BEM VINDO AO JOGO DE ADVINHAÇÃO')
print('###############################')

numero_secreto = random.randrange(1,101)
total_de_tentativas = 0
pontos= 1000

print('Qual nivel de dificuldade')
print('(1)Facil (2)Médio (3)Dificil')

nivel = int(input('Defina o nivel: '))

if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5


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
        print('Você acertou e fez {} pontos!'.format(pontos))
        break
    else:
        if(maior):
            print('Você errou o seu chute foi maior do que o numero secreto.')
        elif(menor):
            print('Você errou o seu chute foi menor do que o numero secreto.')
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos    

    rodada = rodada + 1

print('fim do jogo')