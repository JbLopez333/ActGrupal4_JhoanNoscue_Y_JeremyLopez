# 1. Importar librerías
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# 2. Crear los datos en un DataFrame
# ============================================================

datos = {
    "Mes": [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ],
    "Portatiles": [20, 18, 25, 30, 28, 35, 40, 38, 36, 34, 32, 30],
    "Monitores": [15, 16, 14, 18, 20, 22, 24, 23, 21, 19, 18, 17],
    "Teclados": [40, 42, 38, 45, 47, 50, 55, 53, 52, 48, 46, 44]
}

df = pd.DataFrame(datos)

print("=== DataFrame cargado ===")
print(df)

# ============================================================
# 3. Exploración básica
# ============================================================

print("\n=== Primeras filas ===")
print(df.head())

print("\n=== Información del DataFrame ===")
print(df.info())

print("\n=== Estadísticas descriptivas ===")
print(df.describe())

# ============================================================
# 4. Estadísticas con NumPy
# ============================================================

# Portátiles
ventas_port = df["Portatiles"].values
media_port = np.mean(ventas_port)
mediana_port = np.median(ventas_port)
desv_port = np.std(ventas_port)

# Monitores
ventas_mon = df["Monitores"].values
media_mon = np.mean(ventas_mon)
mediana_mon = np.median(ventas_mon)
desv_mon = np.std(ventas_mon)

# Teclados
ventas_tec = df["Teclados"].values
media_tec = np.mean(ventas_tec)
mediana_tec = np.median(ventas_tec)
desv_tec = np.std(ventas_tec)

print("\n=== Estadísticas con NumPy ===")
print("Portátiles -> Media:", media_port, "Mediana:", mediana_port, "Desv:", desv_port)
print("Monitores  -> Media:", media_mon, "Mediana:", mediana_mon, "Desv:", desv_mon)
print("Teclados   -> Media:", media_tec, "Mediana:", mediana_tec, "Desv:", desv_tec)

# ============================================================
# 5. Calcular ventas totales por mes
# ============================================================

df["Total_Mensual"] = df["Portatiles"] + df["Monitores"] + df["Teclados"]

print("\n=== DataFrame con total mensual ===")
print(df)

# ============================================================
# 6. Encontrar el mes con más ventas totales
# ============================================================

mes_max = df.loc[df["Total_Mensual"].idxmax(), "Mes"]
max_ventas = df["Total_Mensual"].max()

print("\n=== Mes con más ventas totales ===")
print("Mes:", mes_max, "| Ventas totales:", max_ventas)

# ============================================================
# 7. GRÁFICOS
# ============================================================

# 7.1 Gráfico de líneas por producto
plt.figure(figsize=(12, 5))
plt.plot(df["Mes"], df["Portatiles"], marker="o", label="Portátiles")
plt.plot(df["Mes"], df["Monitores"], marker="o", label="Monitores")
plt.plot(df["Mes"], df["Teclados"], marker="o", label="Teclados")
plt.title("Ventas mensuales por producto - TecnoPlus")
plt.xlabel("Mes")
plt.ylabel("Unidades vendidas")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# 7.2 Gráfico de barras del total mensual
plt.figure(figsize=(12, 5))
plt.bar(df["Mes"], df["Total_Mensual"])
plt.title("Ventas totales mensuales - TecnoPlus")
plt.xlabel("Mes")
plt.ylabel("Unidades totales vendidas")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ============================================================
# 8. Conclusiones
# ============================================================

print("\n=== CONCLUSIONES ===")
print("1. Tendencias: Las ventas muestran un crecimiento progresivo hasta mitad de año, especialmente en teclados y portátiles.")
print("2. Producto más fuerte: El producto con mayores ventas durante todo el año son los teclados.")
print("3. Mes pico: El mes con mayor venta total fue", mes_max, "con", max_ventas, "unidades vendidas.")
