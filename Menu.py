from input import *
import os
import json

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
            print(f'   {str(o+1)} - {self.titles[o]}')
        print('\n')

    def validate_input_selection(self, _sel):
        print(_sel)
        return not(_sel < 0 or _sel > len(self.titles)-1)

    def run(self):
        self.show()
        sel = get_input('digite uma opção: ', tratar_input_int, self.validate_input_selection)
        print('\n')
        self.functions[sel]()
        print('\n')
        if self.handle_end:
            self.handle_end()

