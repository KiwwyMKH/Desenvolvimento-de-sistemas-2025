class Conta:
    def __init__(self, titular, saldo):
        self.__titular= titular
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo

    @property 
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self,nome):
        self.__titular = nome


