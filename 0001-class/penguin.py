from fish import Fish
from bird import Bird

class Penguin(Fish, Bird):
    def meow(self) -> None:
        print(f'{self._name} can''t meow')

    def chick(self) -> None:
        print(f'{self._name} chick')