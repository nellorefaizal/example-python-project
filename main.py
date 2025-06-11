
class Dog:
    legs=4
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def speak(self):
        print(f'{self.name} says:Barak!..')



class smalldog(Dog):
    def speak(self):
        print(f'{self.name} says:cant Barak!..')
    def WhatIsYourAge(self):
        print(f'{self.name} says: my smalldog age is {self.age} years')

class TinyDog(smalldog):
    pass



dog=Dog("fif",5)
dog.speak()
#dog.WhatIsYourAge()


smalldog=smalldog('kuky',2)
smalldog.speak()
smalldog.WhatIsYourAge()

TinyDog=TinyDog('TINY',1)
TinyDog.speak()

TinyDog.WhatIsYourAge()