def tratar_input_base(_str: str):
    _str = _str.strip()
    _str = _str.lower()

def tratar_input_int(_str: str):
    for letra in "abcdefghijklmnopqrstuvwxyz ":
        _str = _str.replace(letra, "")
    
    try:
        result = int(_str)
    except:
        return -1
    return result
