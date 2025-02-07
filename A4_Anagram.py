def anagram(string1,string2):
    string1 = sorted(list(string1))
    string2 = sorted(list(string2))
    if string1 == string2:
        print('True')
    else:
        print('False')

a = input("Enter a string: ")
b = input("Enter a string: ")

print(anagram(a,b))





