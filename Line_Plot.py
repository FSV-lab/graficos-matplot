
#importamos la libreria y con as abreviamos por convesion a 'plt'
import matplotlib.pyplot as plt

#Definimos la variable 'x' por los años la longevidad por 'y' utilizando listas
#pais_1 
x = [2016,2017,2018,2019,2020,2021]
y = [45,46,47,48,50,51]

#pais_2
x2 =[2016,2017,2018,2019,2020,2021]
y2 = [45,46,47,48,50,51]

#Hacemos plot de x,y se aplican atributos como el tipo o estilo de la linea ,el color de la linea  
plt.plot(x,y,marker='o',linestyle='--',color='g')

#añadiendo nombre  los ejes
plt.xlabel('Años')
plt.ylabel('Población ,(M)')
plt.title('Años vs Población')

#mostrar plt
plt.show()