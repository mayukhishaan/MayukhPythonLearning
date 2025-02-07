C = 50
H = 30
D = input('enter a comma separated sequence that contains only numbers: ')
D= list(D.split(','))
print(D)
printer = []
for x in D:
    Q = round(((2*C*int(x))/H)**.5)
    printer.append(Q)
print(printer)