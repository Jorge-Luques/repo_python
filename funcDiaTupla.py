def cargarFecha():
    dia = int(input("Ingresar dia: "))
    mes = int(input("Ingresar mes: "))
    anio = int(input("Ingresar año: "))
    fecha = (dia,mes,anio)
    return fecha

def mostrarFecha(fecha):
    print(fecha[0], fecha[1], fecha[2], sep="/")

date = cargarFecha()
mostrarFecha(date)
