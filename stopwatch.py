import time
print("Presionar Enter para iniciar el stopwatch")
print("Presionar Ctrl+C para finalizar")

while True:
    try:
        input()
        start_time = time.time()
        print("Stopwatch iniciado")
    except:
        print("Stopwatch finalizado")
        end_time = time.time()
        print("Tiempo total: ",round(end_time - start_time,2), "segundos")
        break