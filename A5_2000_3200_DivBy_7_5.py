list = list(range(2000,3201))
printer = []
for x in list:
    if x%7 == 0 and x%5 != 0:
        printer.append(x)
print(printer)