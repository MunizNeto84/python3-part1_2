print('###############################')
print('BEM VINDO AO JOGO DE ADVINHAÇÃO')
print('###############################')

numero_secreto = 42
chute_str = input('Digite o seu numero? ')


print('Você digitou ', chute_str)
chute = int(chute_str)
acertou = numero_secreto == chute
maior = chute > numero_secreto
menor = chute < numero_secreto

if (acertou):
    print('Você acertou')
else:
    if(maior):
        int('Você errou o seu chute foi maior do que o nuemro secreto.')
    elif(menor):
        print('Você errou o seu chute foi menor do que o nuemro secreto.')

print('fim do jogo')        
    