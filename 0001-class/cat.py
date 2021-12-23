from aniamal import Animal;

class Cat(Animal):
    def meow(self)-> None:
        print(f'{self._name}: meow')