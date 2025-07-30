"""
X json, X tratar input,  qr code

menu que permite voltar etapas em uma opção

"""



from InputNav import InputNav
from input import Input

from Menu_main import menu_main

nav = InputNav()
nav.add_input(Input('prompt 1'))
nav.add_input(Input('prompt 2'))
nav.add_input(Input('prompt 3'))
nav.add_input(Input('prompt 4'))
nav.add_input(Input('prompt 5'))

while True:

    menu_main.run()

