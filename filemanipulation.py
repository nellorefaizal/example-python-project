
import json
#f=open('a.text','r')

#f=open('a.text','w')
#f.write("hello")
#f.write("i am faizal")
#f.close()

#f=open('a.text','a')
#f.write("some thing forget to write\n")
#f.close()
#f.write('ïs the something are there')
#f.close()

#f=open('a.text','r')
#text =f.read()
#f.close()

#with open('a.text','a') as f:
#    f.write("something else\n")
#    f.close()

mydic={'a':'apple','b':'ball'}

with open('a.json','w') as f:
    f.write(json.dumps(mydic))

with open('a.json','r') as f:
    jsondata= f.read()

unpacked=json.loads(jsondata)
print(unpacked)
print(type(unpacked))

