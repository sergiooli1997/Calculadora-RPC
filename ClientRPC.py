import xmlrpc.client
import datetime
s = xmlrpc.client.ServerProxy('http://localhost:8000')

print("Selecciona una operacion")
print("1.- Suma")
print("2.- Resta")
print("3.- Multiplicacion")
print("4.- Division")
opc = int(input())
print("Primer numero")
num1 = int(input())
print("Segundo numero")
num2 = int(input())
if opc == 1:
    print('{} + {} = {}'.format(num1, num2, s.add(num1, num2)))
if opc == 2:
    print('{} - {} = {}'.format(num1, num2, s.res(num1, num2)))
if opc == 3:
    print('{} * {} = {}'.format(num1, num2, s.mul(num1, num2)))
if opc == 4:
    print('{} / {} = {}'.format(num1, num2, s.div(num1, num2)))
