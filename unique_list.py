
class uniqueList(list):
    def __init__(self,message):
        super().__init__()
        self.message=message

    def append(self,item):
        if item in self:
            return
        super().append(item)


uniqueList=uniqueList(message="some thing else")
uniqueList.append(3)
uniqueList.append(3)
uniqueList.append(4)
uniqueList.append('a')
uniqueList.append('b')
uniqueList.append('c')
print(uniqueList)
print(uniqueList.message)