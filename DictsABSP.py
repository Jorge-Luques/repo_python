
# Ejemplos de Automate Boring the Stuff
import pprint
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

def AddOrViewBirthdays(bdays):
    while True:
        print('Enter a name: (blank to quit)')
        name = input()
        if name == '':
            break
        if name in birthdays:
            print(birthdays[name] + ' is the birthday of ' + name)
        else:
            print('I do not have birthday information for ' + name)
            print('What is their birthday?')
            bday = input()
            birthdays[name] = bday
            print('Birthday database updated.')

#AddOrViewBirthdays(birthdays)
for v in birthdays.values():
    print(v)
    
for i in birthdays.items():
    print(i)

print("Tenemos dos formas de imprimir todos los datos del diccionario:")
print("1- pasando los items a una lista a imprimir por consola")
print(list(birthdays.items()))
print("2- usando la bibiliteca pprint para imprimir el diccionario completo")
pprint.pprint(birthdays)
