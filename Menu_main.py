from Menu import *
from Menu_end import menu_end
from Obra import Obra
from input import *

from random import randint

def ler_obras():
    with open('obras.json', 'r') as file:
        data = json.load(file)
    return data

def obra_file_ler(_id):
    data = ler_obras()

    for obra in data:
        if obra['id'] == _id:
            return obra
        
    raise FileNotFoundError



def obra_file_escrever(_obra_nova: Obra):
    data = ler_obras()
    for obra in data:
        try:
            if obra['id'] == _obra_nova['id']:
                raise Exception('Obra já existe')
        except:
            continue
    
    data.append(_obra_nova.to_dict())
    with open('obras.json', 'w') as file:
        json.dump(data, file, indent=2)

    return True

def remover():
    id = get_input('id: ', tratar_input_int, validate_input_obra_id)

    data = ler_obras()
    for i in range(len(data)):
        if data[i]['id'] == id:
            data.pop(i)
            with open('obras.json', 'w') as file:
                json.dump(data, file, indent=2)
            return True
    
    

    print('Obra não encontrada')
        
def adicionar():
    data = ler_obras()
    id_valido = False
    while not id_valido:
        id = randint(0, 1000)
        achou = False
        for obra in data:
            if obra['id'] == id:
                achou = True
        if not achou:
            id_valido = True

    
    obra_cliente = input_obra()
    obra_cliente.id = id

    obra_file_escrever(obra_cliente)


def buscar():
    id = get_input('id: ', tratar_input_int, validate_input_obra_id)
    try:
        obra = obra_file_ler(id)
        for key, val in obra.items():
            print(f'{key}: {val}')
    except:
        print('Obra não encontrada')
def listar():
    with open('obras.json', 'r') as file:
        data = json.load(file)
    for obra in data:
        print(obra)

def handle_end():
    menu_end.run()

menu_main = Menu('Menu Principal', handle_end)
menu_main.add_option('Adicionar', adicionar)
menu_main.add_option('Buscar', buscar)
menu_main.add_option('Listar', listar)
menu_main.add_option('Remover', remover)
