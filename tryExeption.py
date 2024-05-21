class Calculator:
    def add(self,a,b):
        return a+b
    def minus(self,a,b):
        return a-b
    def mult(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b
    def proc(self,a,b):
        return a%b
    @staticmethod
    def money():
        print('babki goni:')
    
cal=Calculator()

class B(Calculator):
    pass

g = B()

def Input():
    x=int(input("first number: "))
    y=int(input("second number: "))
    return x,y

znak=input("viberite(+,-,*,/,%)")

if znak in ["+","-","*","/","%"]:
    num1,num2=Input()

    if znak=="+":
        print("result: ",g.add(num1,num2) ,'гони бабки 100$')
    if znak == '-':
        print("result: ",g.minus(num1,num2), 'гони бабки 100$')
    if znak == '*':
        print("result: ",g.mult(num1,num2), 'гони бабки 100$')
    if  znak == '/':
        print("result: ",g.div(num1,num2), 'гони бабки 100$')
    if znak == '%':
        print('result:', g.proc(num1),'гони бабки 100$')