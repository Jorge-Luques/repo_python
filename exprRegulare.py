import re

#Coincidir con un número entero positivo de una o más cifras:
def hayNumeroPositivo(cadena):
    patron = r"\d+"  # Buscar uno o más dígitos
    resultado = re.search(patron, cadena)
    if resultado:
        entero = int(resultado.group())
        print(f"El entero es {entero}")
    else:
        print("No se encontró ningún entero en la cadena.")

#Coincidir con una dirección de correo electrónico:
def hayMailValido(cadena):
    patron = r"\b[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,}\b"  # Expresión regular para correo electrónico
    resultado = re.search(patron, cadena)
    if resultado:
        email = resultado.group()
        print(f"La dirección de correo electrónico es {email}")
    else:
        print("No se encontró ninguna dirección de correo electrónico en la cadena.")

#Coincidir con una URL:
def hayWebCorrecta(cadena):
    patron = r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+" # Expresión regular para URL (acepta http o https)
    resultado = re.search(patron, cadena)
    if resultado:
        url = resultado.group()
        print(f"La URL es {url}")
    else:
        print("No se encontró ninguna URL en la cadena.")

#Coincidir con un número de teléfono en formato internacional:
def hayTelInternacCorrecto(cadena):
    patron = r"\+\d{1,3}-\d{1,3}-\d{1,4}-\d{1,4}" # Expresión regular para número de teléfono en formato internacional
    resultado = re.search(patron, cadena)
    if resultado:
        telefono = resultado.group()
        print(f"El número de teléfono es {telefono}")
    else:
        print("No se encontró ningún número de teléfono en la cadena.")

   # main 
cadena = "El número es 12345"
hayNumeroPositivo(cadena)
cadena = "Mi correo es usuario@gmail.com"
hayMailValido(cadena)
cadena = "Visite mi sitio web: https://www.ejemplo.com"
hayWebCorrecta(cadena)
cadena = "Mi número de teléfono es +1-555-555-5555"
hayTelInternacCorrecto(cadena)