from input import *
import os
class Menu():
    def __init__(self, _title: str | None, _handle_end):
        self.title = _title
        self.functions = []
        self.titles = []
        self.handle_end = _handle_end
    
    def add_option(self, _title: str, _function):
        self.titles.append(_title)
        self.functions.append(_function)

    def show(self):
        if self.title:
            print('\n' + '-'*10 + self.title + '-'*10)
        for o in range(len(self.titles)):
            print(f'   {str(o)} - {self.titles[o]}')

    def get_selection(self, _prompt: str):
        valido = False
        while True:
            sel = tratar_input_int( input(_prompt) )
            valido = not(sel < 0 or sel > len(self.titles)-1)
            if valido:
                break
            else:
                print(f"'{sel}' não é um valor válido, tente novamente")
                
        return sel
    
    def run(self):
        self.show()
        sel = self.get_selection('digite uma opção: ')
        print('\n')
        self.functions[sel]()
        print('\n')
        if self.handle_end:
            self.handle_end()

