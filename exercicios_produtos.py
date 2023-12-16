from dados_package import produtos

import copy

produtos_10 = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)
]
print('\n',"'Produtos originais'", *produtos, sep='\n')
print('\n',"'produtos_10'",*produtos_10, sep='\n')

produtos_por_nome = sorted(
    copy.deepcopy(produtos_10 ),
    key= lambda p:p['nome']
)
print('\n','"produtos_por_nome"',*produtos_por_nome, sep='\n')

produtos_por_preco = sorted(
    copy.deepcopy(produtos_10 ),
    key= lambda p:p['preco']
)
print('\n',"'produtos_por_preco'",*produtos_por_preco,sep='\n')