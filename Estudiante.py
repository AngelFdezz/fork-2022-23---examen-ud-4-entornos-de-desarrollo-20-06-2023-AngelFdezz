"""
Clase Estudiante base para el Examen Convocatoria Ordinaria de la UD4
:author: Angel Fernández
Refactorización
Extrae una superclase con los campos
	nombre
	apellidos
	nif

"""


class Persona:
    '''
    Clase principal Persona
    :author:  Angel Fernández
    '''
    apellidos = "Apellidos";
    nombre = "Nombre";
    nif = "11111111Z";

class Estudiante(Persona):
    '''
    Clase derivada de Persona llamada Estudiante
    :author:  Angel Fernández
    '''
    curso = "Primaria";

    def __init__(self):
        pass;

    def __init__(self, nif, curso, nombre, apellidos):
        '''
        Contructor clase Estudiante con 4 parámetros
        :param nif: nif del estudiante
        :param curso: curso del estudiante
        :param nombre: nombre del estudiante
        :param apellidos: apellidos del estudiante
        '''
        self.nif = nif;
        self.curso = curso;
        self.nombre = nombre;
        self.apellidos = apellidos;

    @property
    def nif(self):
        '''
        :return: nif
        '''
        return self.__nif

    @nif.setter
    def nif(self, value):
        '''

        :param value: valor nif
        :return: valor nif
        '''
        self.__nif = value

    @property
    def curso(self):
        '''

        :return: curso
        '''
        return self.__curso

    @curso.setter
    def curso(self, value):
        '''

        :param value: valor curso
        :return: valor curso
        '''
        self.__curso = value

    @property
    def nombre(self):
        '''

        :return: nombre
        '''
        return self.__nombre

    @nombre.setter
    def nombre(self, value: int):
        '''

        :param value: valor nombre
        :return: valor nombre
        '''
        self.__nombre = value

    @property
    def apellidos(self):
        '''

        :return: apellidos
        '''
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, value):
        '''

        :param value: valor apellidos
        :return: valor apellidos
        '''
        self.__apellidos = value

