# Matplotlib [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de matplotlib
import numpy as np
import matplotlib.pyplot as plt
from numpy.random.mtrand import sample


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    print("Scatter Plot")

    # NOTA: aproveche los ejemplos "scatter_plot" de clase

    # Alumnos: Se desea graficar la función tanh para el siguiente
    # intervalor de valores de "X"
    x = np.arange(-np.pi, np.pi, 0.1)
    # Función y = tanh(x) --> tangente hiperbólica
    y = np.tanh(x)
    # Definir tamaño figura
    fig = plt.figure()  
    # Definir cuantos gráficos tendrá
    ax = fig.add_subplot()
    # Graficar con plot en mi gráfico "ax"
    ax.plot(x, y)
    plt.show()  
    
#def scatter_plot():

#    x = np.arange(-np.pi, np.pi, 0.1)
#    y = np.tanh(x) 
#    fig = plt.figure()
#    fig.suptitle('Line vs Scatter', fontsize=16)
#    ax1 = fig.add_subplot(1, 2, 1)
#    ax2 = fig.add_subplot(1, 2, 2)

#    ax1.plot(x, y, c='darkcyan')
#    ax1.set_facecolor('whitesmoke')
#    ax1.grid('solid')
#    ax2.scatter(x, y, c='darkcyan')
#    ax2.set_facecolor('whitesmoke')
#    ax2.grid('solid')
#    plt.show()
   
    x = np.arange(-np.pi, np.pi, 0.1)
    y = np.tanh(x)
    plt.scatter(x,y,marker="x",color='r',label="tanh(x)")
    
    plt.legend()
    plt.show()

    

    # Graficar la función utilizando "scatter"
    # utilizando "x" e "y"

    # Colocar la leyenda y el label con el nombre de la función

    # Elegir un marker a elección

    # Crear acá su gráfico

print("terminamos")