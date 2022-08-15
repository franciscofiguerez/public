#Paradoja de Montyhall
import random
import collections
import pandas as pd
import matplotlib.pyplot as plt

#veces que lanzamos el experimento
iteraciones=1000

#variables
ganasincambiar=0
ganacambiando=0
arr_ganasincambiar=[]
arr_ganacambiando=[]



for vecesjuego in range(0,iteraciones):


    #3 puertas y una de ellas es la que tiene el premio
    puertas=[0,0,0]
    n = random.randint(0,2)
    puertas[n]=1
    puertas

    #Eleccion del jugador 
    puertaseleccion=[0,0,0]
    n = random.randint(0,2)
    puertaseleccion[n]=1
    puertaseleccion

    #enseñamos una puerta que no ha seleecionado el jugador y que no tiene premio
    for i in range (0,3):
        if puertas[i]==0 and puertaseleccion[i]==0:        
            puertas.pop(i)
            puertaseleccion.pop(i)
            break


    #if(collections.Counter(puertas) == collections.Counter(puertaseleccion)):
    if(puertas==puertaseleccion):
        ganasincambiar=ganasincambiar+1
    else:
        ganacambiando=ganacambiando+1

    arr_ganasincambiar.append(ganasincambiar)
    arr_ganacambiando.append(ganacambiando)

print('*************************************************************')
print('Iteraciones: '+str(iteraciones))
print('Veces ganado sin cambiar de puerta: '+str(ganasincambiar))
print('Veces ganado cambiando de puerta: '+str(ganacambiando))
print('*************************************************************')

d = {'Cambiando':arr_ganacambiando,'Sin Cambiar':arr_ganasincambiar}
df = pd.DataFrame(d)

df.plot()
plt.show()
