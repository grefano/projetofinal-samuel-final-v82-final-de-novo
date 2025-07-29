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

def get_input(_prompt: str, _tratar = None, _validar = None):
        valido = False
        while True:
            _input = input(_prompt)
            print(f"input antes de ser tratado {_input}")
            _input = _tratar(_input)
            print(f"input depois de ser tratado {_input}")
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
