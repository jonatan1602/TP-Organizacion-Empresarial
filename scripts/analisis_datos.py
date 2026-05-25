import pandas as pd
import matplotlib.pyplot as plt

# Leer archivo CSV de ventas
ventas = pd.read_csv("datos/ventas.csv")

# Crear columna de ventas totales
ventas["total"] = ventas["cantidad"] * ventas["precio"]

# Calcular ventas totales generales
ventas_totales = ventas["total"].sum()

print("Ventas Totales:")
print(ventas_totales)

# Calcular producto más vendido
producto_mas_vendido = ventas.groupby("producto")["cantidad"].sum().idxmax()

print("\nProducto más vendido:")
print(producto_mas_vendido)

# Convertir fecha a formato datetime
ventas["fecha"] = pd.to_datetime(ventas["fecha"])

# Crear columna mes
ventas["mes"] = ventas["fecha"].dt.month

# Calcular ventas por mes
ventas_por_mes = ventas.groupby("mes")["total"].sum()

print("\nVentas por mes:")
print(ventas_por_mes)

# Generar gráfico de ventas por producto
ventas_por_producto = ventas.groupby("producto")["cantidad"].sum()

ventas_por_producto.plot(kind="bar")

plt.title("Ventas por Producto")
plt.xlabel("Producto")
plt.ylabel("Cantidad Vendida")

# Guardar gráfico
plt.savefig("resultados/grafico_ventas.png")

plt.show()
