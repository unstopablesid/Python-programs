
a=2
b=3
def gmean():
    print(gmean,(a*b)/(a+b))

#def average(a=9,b=9):
    #print("The average is ",(a+b)/2)



def average(*numbers):
    sum=0
    for i in numbers:
        sum= sum + i
    print("average is: ",sum/len(numbers))