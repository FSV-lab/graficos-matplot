import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Generar datos aleatorios para el heatmap
np.random.seed(42)
data = np.random.rand(10, 10)  # Matriz 10x10 con valores aleatorios entre 0 y 1

# Crear el heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(data, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
plt.title("Heatmap - Mapa de Calor")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.show()
