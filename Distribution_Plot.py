import seaborn as sns
import matplotlib.pyplot as plt

# Datos
tips = sns.load_dataset('tips')

# Crear gráfico de distribución
sns.histplot(tips['total_bill'], kde=True, color='purple')

# Títulos y etiquetas
plt.title("Distribución del Total de la Cuenta")
plt.xlabel("Total de la Cuenta")
plt.ylabel("Frecuencia")

# Mostrar el gráfico
plt.show()
