# Casos
print("Este programa juega FuzzBizz con 'n' elementos y valores 'a' y 'b'")
n=int(input("n: "))
a=int(input("Valor de Fizz: "))
b=int(input("Valor de Buzz: "))
for i in range (1,n+1):
    if(i%(a*b)==0):
        print("FizzBuzz")
    elif(i%a==0):
        print("Fizz")
    elif(i%b==0):
        print("Buzz")
    else:
        print (i)