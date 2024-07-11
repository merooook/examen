import random
import csv

#en el repaso del profe hernán puso un fn, q es?

with open ('archivo_examen.csv','w',newline=' ') as archivo: #donde iba el delimiteeeer=','
    print("a")

trabajadores=["juan pérez", "maría garcía", "carlos lópez", "ana martínez", "pedro rodríguez", "laura hernández", "miguel sánchez", "isabel gómez", "francisco díaz", "elena fernández"]

sueldos_trabajadores= {}

def sueldos_aleatorios():
    sueldos_trabajadores=random.randint(300000,2500000)
    for trabajador in trabajadores : {trabajador : 0 for trabajador in trabajadores}
    print(trabajador, sueldos_trabajadores)

def clasificacion_sueldos():
    menores=sueldos_trabajadores<8000000
    mayores=sueldos_trabajadores>2000000
    entre=sueldos_trabajadores>800000 and sueldos_trabajadores<2000000
    print=len(menores)
    print(menores)
    print=len(entre)
    print(entre)
    print=len(mayores)
    print(mayores)
    total=menores+mayores+entre
    print("total: $",total)

def datos_sueldos():
    mayor=max(sueldos_trabajadores)
    menor=min(sueldos_trabajadores)
    prom=mayor*menor/2
    print(mayor)
    print(menor)
    print(prom)
    print("???media geométrica???")

def reporte_sueldos():
    salud=sueldos_trabajadores*7/100
    afp=sueldos_trabajadores*12/100
    liquido=sueldos_trabajadores-salud-afp
    print(trabajadores,sueldos_trabajadores)
    print(trabajadores,salud)
    print(trabajadores,afp)
    print(trabajadores,liquido)


while True:
    print("********menú********")
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadísticas")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")
    op=int(input("ingrese una opción: "))

    if op==1:
        for trabajador in sueldos_trabajadores : {trabajador : 0 for trabajador in trabajadores}
        sueldos_aleatorios()
    elif op==2:
        clasificacion_sueldos()
    elif op==3:
        datos_sueldos()
    elif op==4:
        reporte_sueldos()
    elif op==5:
        print("Finalizando programa...")
        print("Desarrollado por Meritxell Arroyo")
        print("21.494.190-2")
        break