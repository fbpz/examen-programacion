import funciones as fn
trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]

sueldos=[]

while True:
    print("******MENU*******")
    print("1. asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadísticas")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")

    opcion=int(input("ingrese una opcion: "))
    if opcion==1:
        fn.asignar_sueldos(trabajadores,sueldos)
    elif opcion==2:
        fn.clasificar_sueldos(sueldos)
    elif opcion==3:
        fn.estadisticas_sueldos(sueldos)
    elif opcion==4:
        fn.reporte_de_sueldos(sueldos)
    elif opcion==5:
        print("saliendo...")
        print("FERNANDA BELEN PEÑA ZUÑIGA 001V_A")
        break







