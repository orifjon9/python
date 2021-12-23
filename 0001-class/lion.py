from cat import Cat

class Lion(Cat):
    def roar(self) -> None:
        print(f'{self._name} roar')
