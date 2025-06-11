
class Shapes:
    width=5
    hight=5
    printchar='1'


    def printRow(self,i):
        raise NotImplementedError("it will be implemented in child class")
    def print(self):
        for i in range(self.hight):
            self.printRow(i)

class square(Shapes):
    def printRow(self, i):
        print(self.printchar * self.width)

class triangle(Shapes):
    def printRow(self, i):
        print(self.printchar * (i+1))


class symmetricTriangle(Shapes):
    hight=5
    width=2*hight
    def printRow(self, i):
        trianglewidth=i*2+1
        padding= int((self.width-trianglewidth)/2)
        print(' '* padding + self.printchar* trianglewidth)
square=square()
square.print()



triangle=triangle()
triangle.print()

symmetricTriangle=symmetricTriangle()

symmetricTriangle.print()