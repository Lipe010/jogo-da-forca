def soma(x, y):
    return x + y
 
def multiplica(x, y):
    return x * y    

def executa(function, x):
    def atrasa(y):
        return function(x,y)
    return atrasa

multiplica_por_5 = executa(multiplica,5)
soma_mais_10 = executa(soma,10)
print(multiplica_por_5(6))
print(soma_mais_10(7))
