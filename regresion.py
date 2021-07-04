import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def regresion(x,y,valor=None):
    xMenosPromedio = obtenerLista(x)
    yMenosPromedio = obtenerLista(y)
    xMenosXCuadrado = obtenerCuadrado(x)
    promedio_x = sum(x) / len(x)
    promedio_y = sum(y) / len(y)
    sumaCuadradosX = sum(xMenosXCuadrado)
    multiplicacionXyY = list(np.multiply(xMenosPromedio,yMenosPromedio)) 
    sumaResultadoMultiplicacion = sum(multiplicacionXyY)
    w1 = sumaResultadoMultiplicacion / sumaCuadradosX 
    w0 = -1*w1*promedio_x + promedio_y
    if valor:
        print(obtenerValorRegresion(valor,w0,w1))
    else:
        obtenerLineaRegresion(x,y,11,w0,w1)
    
def obtenerLineaRegresion(x,y,rango_regresion,w0,w1):
    linea_regresion = []
    regresion_x = []
    for valor_x in range(1,rango_regresion):
        valor_y = w0 + w1*valor_x
        regresion_x.append(valor_x)
        linea_regresion.append(valor_y)
    graficar(x,y,regresion_x,linea_regresion)

def obtenerValorRegresion(valor,w0,w1):
    y = w0 + w1*valor
    return y

def graficar(x,y,regresion_x,regresion_y):
    plt.plot(x, y, label="Data")
    plt.plot(regresion_x, regresion_y, label="Linear Regression")
    plt.legend()
    plt.show()

def obtenerLista(lista):
    iMenosPromedio = []
    promedio = sum(lista) / len(lista)
    for i in lista:
        resta = i - promedio
        iMenosPromedio.append(resta)
    return iMenosPromedio     

def obtenerCuadrado(lista):
    iMenosICuadrado = []
    promedio = sum(lista) / len(lista)
    for i in lista:
        resultado = (i - promedio)**2
        iMenosICuadrado.append(resultado)
    return iMenosICuadrado

if __name__ == "__main__":
    df = pd.read_excel('data.xlsx')
    x_column =  df['x']
    y_column =  df['y']
    valorX = float(input("Ingrese el valor de x: "))
    regresion(x_column,y_column,valorX)
    valorY = float(input("Ingrese el valor de y: "))
    regresion(y_column,x_column,valorY)

