import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

def regresion(x,y):
    promedio_x= sum(x) / len(x)
    promedio_y = sum(y) / len(y)
    xMenosPromedio = [] 
    yMenosPromedio = [] 
    xMenosXCuadrado = []

    for valor in x:
        resta = valor - promedio_x
        xMenosPromedio.append(resta)

    for valor in y:
        resta = valor - promedio_y
        yMenosPromedio.append(resta)

    for valor in x:
        resultado = (valor - promedio_x)**2
        xMenosXCuadrado.append(resultado);

    sumaCuadradosX = sum(xMenosXCuadrado)

    # Multiplicar el resultado de x menos el promedio de x y y menos el promedio de y
    multiplicacionXyY = list(np.multiply(xMenosPromedio,yMenosPromedio)) 
    sumaResultadoMultiplicacion = sum(multiplicacionXyY)

    w1 = sumaResultadoMultiplicacion / sumaCuadradosX 

    # y = w0 +w1x
    # obtener w0
    w0 = -1*w1*promedio_x + promedio_y
    # obtener linea de regresion
    linea_regresion = []
    regresion_x = []
    rango_regresion = 11
    # for valor_x in range(1,rango_regresion):
        # valor_y = w0 + w1*valor_x
        # regresion_x.append(valor_x)
        # linea_regresion.append(valor_y)

    # print("linea regresión: ",linea_regresion)
    valor_x = float(input('Ingresar valor x: '))
    valor_y = w0 + w1*valor_x
    print("Valor y: ",valor_y)
    # Graficar
    # plt.plot(x, y, label="Data")
    # plt.plot(regresion_x, linea_regresion, label="Linear Regression")
    # plt.legend()
    # plt.show()


def regresion_paraY(x,y):
    promedio_x= sum(x) / len(x)
    promedio_y = sum(y) / len(y)
    xMenosPromedio = [] 
    yMenosPromedio = [] 
    xMenosXCuadrado = []

    for valor in x:
        resta = valor - promedio_x
        xMenosPromedio.append(resta)

    for valor in y:
        resta = valor - promedio_y
        yMenosPromedio.append(resta)

    for valor in x:
        resultado = (valor - promedio_x)**2
        xMenosXCuadrado.append(resultado);

    sumaCuadradosX = sum(xMenosXCuadrado)

    # Multiplicar el resultado de x menos el promedio de x y y menos el promedio de y
    multiplicacionXyY = list(np.multiply(xMenosPromedio,yMenosPromedio)) 
    sumaResultadoMultiplicacion = sum(multiplicacionXyY)

    w1 = sumaResultadoMultiplicacion / sumaCuadradosX 

    # y = w0 +w1x
    # obtener w0
    w0 = -1*w1*promedio_x + promedio_y
    # obtener linea de regresion
    linea_regresion = []
    regresion_x = []
    rango_regresion = 11
    # for valor_x in range(1,rango_regresion):
        # valor_y = w0 + w1*valor_x
        # regresion_x.append(valor_x)
        # linea_regresion.append(valor_y)

    # print("linea regresión: ",linea_regresion)
    valor_x = float(input('Ingresar valor y: '))
    valor_y = w0 + w1*valor_x
    print("Valor y: ",valor_y)


if __name__ == "__main__":
    df = pd.read_excel('data.xlsx')
    x_column =  df['x']
    y_column =  df['y']
    regresion(x_column,y_column)
    regresion_paraY(y_column,x_column)
