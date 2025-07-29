#   menu que aparece no final de alguma operação

from Menu import *

def voltar_menu_principal():
    # comi o cu de quem ta lendo
    pass

def finalizar():
    os._exit(0)


menu_end = Menu(None, None)
menu_end.add_option('Voltar ao menu principal', voltar_menu_principal)
menu_end.add_option('Finalizar aplicação', finalizar)