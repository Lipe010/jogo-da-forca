while True:
    numero1 = input(' Digite um numero: ')
    numero2 = input(' Digite outro numero: ')
    operador = input(' Digite um operador (+-*/): ')

    numeros_validos = None
    num_float1 = 0
    num_float2 = 0
    try:
        num_float1 = float(numero1)
        num_float2 = float(numero2)
        numeros_validos = True
    except:
        ...
    if numeros_validos is None:
        print(' Um ou ambos numeros invalídos!')
        continue
    
    operadores_permitidos = '*+-/'
    
    if operador not in operadores_permitidos:
        print(' Seu operador é invalido')
        continue

    print(' Realizando sua conta, confira o resultado: ')

    if operador == '*':
       print(f'{num_float1} * {num_float2} = ', num_float1 * num_float2)
    elif operador == '/':
       print(f'{num_float1} / {num_float2} = ',num_float1 / num_float2)
    elif operador == '+':
        print(f'{num_float1} + {num_float2} = ',num_float1 + num_float2)
    elif operador == '-':
       print(f'{num_float1} - {num_float2} = ',num_float1 - num_float2)
        

    sair = input(' Você quer sair ? [s]sim ou [n] para não: ').lower().startswith('s')
    print(' Você saiu!')

    if sair is True:
       break