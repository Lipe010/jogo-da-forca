name = 'Filipe'
it_name = 0
novonome = "*"
while it_name < len(name):    
    new_word = (name[it_name])
    novonome += f'{new_word}*'
    it_name += 1

print(novonome)  