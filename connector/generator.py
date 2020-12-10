import random as rd, string

# Sample dictionaries
usuario_tipos = ['j', 'c', 's']
numbers = ['1','2','3','4','5','6','7','8','9','.']
idiomas = ['Spanish', 'English', 'German', 'French', 'Portuguese', 'Chinese']
paises = ['Spain', 'US', 'Germany', 'France', 'Portugal', 'China']
bools = [True, False]
contractTypes = ['tipo1','tipo2','tipo3']
itemTypes = ['Escenario', 'Audio', '3Dmodel']

def rand_num(max):
    return rd.randint(0, max)

def rand_str(strings, size):
    return ''.join(rd.choice(string) for x in range(size))

def rand_bool():
    return rd.choice(bools)

def get_usuario():
    return rand_str(string.ascii_letters, 30)

def get_usuario_tipo():
    return rand_str(usuario_tipos, 1)

def get_ip():
    return rand_str(numbers, 15)

def get_locacion():
    return rand_str(paises, 1)

def get_idioma():
    return rand_str(idiomas, 1)

def get_nombre():
    return rand_str(string.ascii_letters, 35)

def get_contract():
    return rand_str(contractTypes, 1)

def get_item():
    return rand_str(itemTypes, 1)