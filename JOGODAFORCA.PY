import os

palavra_secreta = 'inter'

letras_acertadas = ''

numero_tentativas = 0
while True:
    letra_dig = input(' Digite uma letra: ')
    numero_tentativas += 1
    print(' Seu numero de tentativas atual é,', numero_tentativas)

    if len(letra_dig) > 1:
        input(' Digite apenas uma letra! ')
        continue

    if letra_dig in palavra_secreta:
        letras_acertadas += letra_dig

    palavra_formada = ''    
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
           palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    
    print(' Palavra formada,', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print(' Parabéns você ganhou!!!!')
        print(' A palavra secreta era,', palavra_secreta)
        print(f' Você terminou o jogo com {numero_tentativas}, tentativas. ')
        letras_acertadas = ''
        numero_tentativas = 0