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
        
    print('obra não encontrada')
    return data



def obra_file_escrever(_obra_nova: Obra):
    data = ler_obras()
    for obra in data:
        print(obra)
        try:
            if obra['id'] == _obra_nova['id']:
                raise Exception('Obra já existe')
        except:
            continue
    
    data.append(_obra_nova.to_dict())
    with open('obras.json', 'w') as file:
        json.dump(data, file, indent=2)

    return True
        
def adicionar():
    print('adicionar')
    data = ler_obras()
    print(data)
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
    print('buscar')

def listar():
    with open('obras.json', 'r') as file:
        data = json.load(file)
    for obra in data:
        print(obra)

def remover():
    print('remover')

def handle_end():
    menu_end.run()

menu_main = Menu('Menu Principal', handle_end)
menu_main.add_option('Adicionar', adicionar)
menu_main.add_option('Buscar', buscar)
menu_main.add_option('Listar', listar)
menu_main.add_option('Remover', remover)
