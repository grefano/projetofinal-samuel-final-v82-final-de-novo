class Obra():
    def __init__(self, _id: int, _autor: str, _nome: str, _material: str, _superficie: str, _largura: float, _comprimento: float, _preco: float):
        self.id = _id
        self.autor = _autor
        self.nome = _nome
        self.material = _material
        self.superficie = _superficie
        self.largura = _largura
        self.comprimento = _comprimento
        self.preco = _preco

    def to_dict(self):
        return {
            "id": self.id,
            "autor": self.autor,
            "nome": self.nome,
            "material": self.material,
            "superficie": self.superficie,
            "largura": self.largura,
            "comprimento": self.comprimento,
            "preco": self.preco,
        }   