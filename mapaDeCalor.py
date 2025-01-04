import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# Generar datos simulados (temperaturas en °C)
x = np.linspace(0, 100, 100)
y = np.linspace(0, 100, 100)
x, y = np.meshgrid(x, y)
temperature = 20 + 10 * np.sin(x / 10) * np.cos(y / 10)  # Simulación de patrones de temperatura

# Crear un colormap estilo clima
cmap = ListedColormap(["blue", "cyan", "green", "yellow", "orange", "red"])

# Crear el mapa de calor estilo clima
plt.figure(figsize=(10, 8))
contour = plt.contourf(x, y, temperature, levels=np.linspace(temperature.min(), temperature.max(), 20), cmap=cmap)
plt.colorbar(contour, label="Temperatura (°C)")
plt.title("Mapa de Calor - Estilo Clima")
plt.xlabel("Longitud")
plt.ylabel("Latitud")
plt.show()
