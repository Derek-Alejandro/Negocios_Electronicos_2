# Método Push
# Inventario inicial
inventario = 10
# Método Push

# Inventario inicial
inventario = 10

# Pronóstico de demanda para 5 días
pronostico = [25, 30, 20, 35, 25]

# Producción planeada (Push) según pronóstico
produccion = pronostico.copy()

print("Día | Pronóstico | Producción | Demanda | Inventario final")
print("--------------------------------------------------------")

for dia in range(5):
    # Se produce antes de que llegue la demanda (Push)
    inventario += produccion[dia]

    # Demanda real del día (la misma que el pronóstico en este ejemplo)
    demanda = pronostico[dia]

    # Se atiende la demanda
    if inventario >= demanda:
        inventario -= demanda
    else:
        # si no alcanza, se atiende lo que hay
        demanda = inventario
        inventario = 0

    # Mostrar resultados del día
    print(dia+1, "|", pronostico[dia], "|", produccion[dia], "|", demanda, "|", inventario)
    
    
    