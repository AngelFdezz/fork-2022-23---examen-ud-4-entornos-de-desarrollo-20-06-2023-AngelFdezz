"""
Clase Gato.
:author: Jaime Rabasco Ronda.
"""
class Gato:
    '''
    Clase principal Gato
    :author: Angel Fernández
    '''

    def __init__(self):
        '''
        Constructor clase Gato
        '''
        self.maulla = 'Miau'

    def maullar(self):
        '''

        :return: maulla
        '''
        print(self.maulla)

g = Gato()
g.maullar()
