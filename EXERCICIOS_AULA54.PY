numero = input(' Digite um numero: ')

if '.' in numero or ',' in numero:
    print(' Não é numero inteiro') 

horario = input(' Que horas são? ')

horario_int = int(horario)

if horario_int < 12 :
    print(' Bom dia!')
elif horario_int >= 12 and horario_int < 18 :
    print(' Boa tarde!')
elif horario_int >= 18 and horario_int  <=23:
     print(' Boa noite!')
else:
    print(' Horario inexistente: \\n')

nome = input(' Digite seu nome: ')
tamanho_nome = len(nome)
if tamanho_nome > 1 :
    if tamanho_nome <= 4:
        print(" Seu nome é curto ")
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print(' Seu nome é normal')
    else:
        print(" Seu nome é grande.")
else:
    print(" Digite mais de uma letra ")