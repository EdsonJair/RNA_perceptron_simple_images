import cv2 as cv
import numpy as np
import random

cero_one = cv.imread('cero_1.jpg', 0)
cero_two = cv.imread('cero_2.jpg', 0)
cero_tree = cv.imread('cero_3.jpg', 0)
cero_four = cv.imread('cero_4.jpg', 0)
cero_five = cv.imread('cero_5.jpg', 0)

one_one = cv.imread('uno_1.jpg', 0)
one_two = cv.imread('uno_2.jpg', 0)
one_tree = cv.imread('uno_3.jpg', 0)
one_four = cv.imread('uno_4.jpg', 0)
one_five = cv.imread('uno_5.jpg', 0)

two_one = cv.imread('dos_1.jpg', 0)
two_two = cv.imread('dos_2.jpg', 0)
two_tree = cv.imread('dos_3.jpg', 0)
two_four = cv.imread('dos_4.jpg', 0)
two_five = cv.imread('dos_5.jpg', 0)

tree_one = cv.imread('tres_1.jpg', 0)
tree_two = cv.imread('tres_2.jpg', 0)
tree_tree = cv.imread('tres_3.jpg', 0)
tree_four = cv.imread('tres_4.jpg', 0)
tree_five = cv.imread('tres_5.jpg', 0)


train_images = [cero_one, cero_two, cero_tree, cero_four, cero_five,
                        two_one,two_two,two_tree,two_four, two_five,one_one,one_two,one_tree,one_four,one_five,
                        tree_one, tree_two, tree_tree, tree_four, tree_five]

bipolar_images = []
for i in train_images:
    vector_imagen=np.ravel(i)
    bipolar_images.append(vector_imagen)
print(np.shape(bipolar_images))
valor_esperado=[1,1,1,1,1,1,-1,1,-1,1,-1,1,-1,1,-1,-1,-1,-1,-1,-1]
print(len(valor_esperado))
#ASIGNACION DE VIAS A LOS PATRONES DE ENTRADA
entradas_vias=[]
print("VECTOR DE ENTRADA AGREGANDO  VIAS")

for i in range(len(bipolar_images)):
    vias = []
    vias= [1]
    for j in range(len( bipolar_images[i])):
        vias.append(int(bipolar_images[i][j]))
    entradas_vias.append(vias)
    print(entradas_vias[i])
print(np.shape(entradas_vias))
print("VALOR ESPERADO")
print(valor_esperado)
#ARREGLO DE LA MATRIZ "ALEATORIA"
alpha=1
value=0
vector_pesos=[]
##matriz de pesos aleatoria
for x in range(len(entradas_vias[0])):
    value=round(random.uniform(-200,200))
    vector_pesos.append(value)
matriz_pesos=np.array(vector_pesos).reshape(len(entradas_vias[0]),1)
salida=0
salida_final=0
correcto=False
i=0
errores=[]
print("MATRIZ DE PESOS INICIAL")
print(matriz_pesos)
while(correcto!=True):
    for j in range(len(entradas_vias[i])):
            salida=entradas_vias[i][j]*vector_pesos[j]
            salida_final=salida_final+salida

    if(salida_final>=0):
        salida_final=1
    else:
        salida_final=-1
    error=valor_esperado[i]-salida_final
    if (error==0):
        errores.append(error)
        if(i==len(entradas_vias)-1):
            print("MATRIZ PESOS FINAL")
            print(matriz_pesos)
            print("Errores")
            print(errores)
            correcto=True
        i = i + 1

    else:
        for k in range(len(entradas_vias[i])):
            vector_pesos[k]=vector_pesos[k]+(alpha*error)*entradas_vias[i][k]
        errores.append(error)
        matriz_pesos = np.array(vector_pesos).reshape(len(entradas_vias[i]),1)
        i=0