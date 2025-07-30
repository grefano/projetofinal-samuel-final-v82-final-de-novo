from Obra import Obra

def tratar_input_base(_str: str):
    _str = _str.strip()
    _str = _str.lower()
    return _str

def tratar_input_int(_str: str):
    for letra in "abcdefghijklmnopqrstuvwxyz ":
        _str = _str.replace(letra, "")
    
    try:
        result = int(_str)
    except:
        return -1
    return result

class Input():
    def __init__(self, _prompt, _tratar=tratar_input_base, _validar=None):
        self.prompt = _prompt
        self.tratar = _tratar
        self.validar = _validar

    def get(self):
        valido = False
        while True:
            _input = input(self.prompt)
            if _input == '-1':
                return -1
            _input = self.tratar(_input)
            print(_input == 0)
            

            if self.validar:
                valido = self.validar(_input)
            else:
                valido = True

            if valido:
                break
            else:
                print(f"'{_input}' não é um valor válido, tente novamente")
                
        return _input

def get_input(_prompt: str, _tratar = tratar_input_base, _validar = None):
    valido = False
    while True:
        _input = input(_prompt)
        _input = _tratar(_input)
        print(_input == 0)
        

        if _validar:
            valido = _validar(_input)
        else:
            valido = True

        if valido:
            break
        else:
            print(f"'{_input}' não é um valor válido, tente novamente")
            
    return _input

def validate_input_dimensao(_input):
    return _input > 0


def validate_input_obra_id(_input):
    return _input >= 0 and _input <= 1000

def input_obra():
    return Obra(
        -1,
        get_input('Autor:', tratar_input_base),
        get_input('Nome:', tratar_input_base),
        get_input('Material:', tratar_input_base),
        get_input('Superficie:', tratar_input_base),
        get_input('Largura:', tratar_input_int, validate_input_dimensao),
        get_input('Comprimento:', tratar_input_int, validate_input_dimensao),
        get_input('Preco:', tratar_input_int)
    )