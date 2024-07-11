import statistics 
import random
import csv


def asignar_sueldos(trabajadores,sueldos):
    for i in trabajadores:
        sueldo= random.randint(300000,2500000)
        sueldos.append({

            i:sueldo
        })

    print(sueldos)
    return
    
def clasificar_sueldos(sueldos):
    if not sueldos:
        print("debe ingresar sueldos")
    else:
        for diccionario in sueldos:
            for trabajador, sueldo in diccionario.items():
                if sueldo<800000:
                    print(f"el trabajador{trabajador} tiene un sueldo de {sueldo} y es menor a $800000 ")
                if sueldo >800000:
                    print(f"el trabajador{trabajador} tiene un sueldo de {sueldo} y es mayor a $800000")    
                if sueldo >2000000:
                    print(f"el trabajador{trabajador} tiene un sueldo de {sueldo} y es mayor a 2000000")   
    return

def estadisticas_sueldos(sueldos):
    if not sueldos:
        print("debe entregar sueldos")
    else:
        lista=[]
        for diccionario in sueldos:
            for trabajador, sueldo in diccionario.items():
                lista.append(sueldo)
        menor=min(lista)
        mayor=max(lista)
        promedio=sum(lista) / len(lista)
        media_geometrica=statistics.geometric_mean(lista)


        print("sueldo menor: ", menor)
        print("sueldo mayor: ",mayor)
        print("promedio de sueldos: ",promedio)
        print("media geometrica: ", media_geometrica)
        return        
    
def reporte_de_sueldos(sueldos):
    if not sueldos:
        print("debe entregar sueldos")
        return
    else:
        
        with open("reporte_de_sueldos.csv","w",newline="") as archivo:
            escritor=csv.writer(archivo)
            escritor.writerow(["nombre trabajador","sueldo base","descuentos salud","sueldo liquido"])
            for diccionario in sueldos:
                for trabajador, sueldo in diccionario.items():
                    descuento_afp=sueldo*0.12
                    descuento_salud=sueldo*0.07
                    sueldo_liquido=sueldo-descuento_afp-descuento_salud
                    escritor.writerow([trabajador,sueldo,descuento_afp,descuento_salud,sueldo_liquido,""])
        print("se imprimieron correctamente los sueldos ")
        return