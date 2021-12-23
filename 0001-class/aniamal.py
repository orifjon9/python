class Animal:
    _name = ''

    def __init__(self, name:str) -> None:
        self._name = name

    def setName(self, name:str) -> None:
        self._name = name