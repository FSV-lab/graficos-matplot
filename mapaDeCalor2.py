import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

# Generar datos conocidos (puntos dispersos)
np.random.seed(42)  # Fijar la semilla para reproducibilidad
x = np.random.uniform(0, 10, 50)  # Coordenadas X
y = np.random.uniform(0, 10, 50)  # Coordenadas Y
z = np.sin(x) + np.cos(y)         # Valores asociados a cada punto (fórmula arbitraria)

# Crear una cuadrícula regular donde interpolar los datos
xi = np.linspace(0, 10, 100)  # Rango de X interpolado
yi = np.linspace(0, 10, 100)  # Rango de Y interpolado
xi, yi = np.meshgrid(xi, yi)  # Crear malla 2D (grilla)

# Interpolación cúbica (con relleno para valores NaN)
zi = griddata((x, y), z, (xi, yi), method='cubic')
if np.any(np.isnan(zi)):
    print("Advertencia: La interpolación contiene valores NaN. Rellenando con método 'nearest'.")
    zi = griddata((x, y), z, (xi, yi), method='nearest')

# Visualizar el mapa de calor
plt.figure(figsize=(8, 6))
contour = plt.contourf(xi, yi, zi, levels=20, cmap="viridis", alpha=0.8)  # Mapa de calor suavizado
plt.colorbar(contour, label="Valor Interpolado")  # Barra de color
plt.scatter(x, y, c=z, cmap="viridis", edgecolors='k', label="Datos conocidos")  # Puntos conocidos
plt.title("Mapa de Calor con Interpolación Cúbica")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
