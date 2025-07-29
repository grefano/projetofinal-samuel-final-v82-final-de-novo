from Menu import *
from Menu_end import menu_end

def adicionar():
    print('adicionar')
def buscar():
    print('buscar')
def listar():
    print('listar')
def remover():
    print('remover')

def handle_end():
    menu_end.run()

menu_main = Menu('Menu Principal', handle_end)
menu_main.add_option('adicionar', adicionar)
menu_main.add_option('buscar', buscar)
menu_main.add_option('listar', listar)
menu_main.add_option('remover', remover)
