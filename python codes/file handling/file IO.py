
# READING A FILE
# f= open('file handling/hi.txt','r')
# print(f)
# text = f.read()
# print()
# f.close() 

#WRITING A FILE
f = open('file handling/hi.txt','w')
f.write('i am student')
f.close()

with open('file handling/hi.txt','a'):
    f.write("i am using with")
