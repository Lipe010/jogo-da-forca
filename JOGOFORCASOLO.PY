import os

palavra_secreta ='programador'
letras_acertadas = ''
numero_tentativas = 0
letras_passadas = ''
tentativas_restantes = 0
palavra_atual = '_' * len(palavra_secreta)

while numero_tentativas < 10:
    tentativas_restantes = 10 - numero_tentativas
    
    print(f'Tente adivinhar a palavra {palavra_atual}'
          f' Você pode errar {tentativas_restantes} letras antes de se enforcar!')
    print(f' Letras que vc ja errou: {letras_passadas}')
    letra_digitada = input(' Digite uma letra: ')
    
    if len(letra_digitada) > 1:
        print(' Digite apenas uma letra')
        print(' Isso contou como erro')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
    else:
        print(' Você errou!')
        letras_passadas += letra_digitada
        numero_tentativas += 1
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada +=letra_secreta
        else:
            palavra_formada += '_'
    palavra_atual = palavra_formada
    
    os.system('cls')
    
    if palavra_formada == palavra_secreta:
        os.system('cls')
        print(' PARABÉNS VOCÊ GANHOUU!!! '
            f'A PALAVRA ERA {palavra_secreta}')
        letras_acertadas = ''
        numero_tentativas = 0
        letras_passadas = ''
        tentativas_restantes = 0
        palavra_atual = '_' * len(palavra_secreta)

else:
    input(' Você perdeu! ')