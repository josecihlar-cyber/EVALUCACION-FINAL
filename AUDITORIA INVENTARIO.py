# =====================================================================
# 1. MATRIZ DE INVENTARIO 
# Estructura: [Código artículo, Nombre, Stock actual, Stock mínimo requerido]
# =====================================================================
inventario = [
    ["ITEM001", "lapiceros negros", 12, 15],
    ["ITEM002", "lapiceros azules", 8, 15],
    ["ITEM003", "cuadernos", 16, 25],
    ["ITEM004", "resaltadores", 5, 10],
    ["ITEM005", "carpetas", 20, 30]
]

# =====================================================================
# 2. MÓDULOS (FUNCIONES)
# =====================================================================

def calcular_cantidad_a_pedir(stock_actual, stock_minimo):
    """
    Calcula la cantidad exacta a pedir para reponer el inventario.
    Lógica: Si falta stock se pide la diferencia, si no, se pide 0.
    """
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:       
        return 0

def mostrar_inventario(inventario):
    """
    Muestra el estado actual del inventario completo en consola.
    """
    print("\n" + "=" * 55)
    print("               INVENTARIO ACTUAL")
    print("=" * 55)
    for articulo in inventario:
        codigo, nombre, stock_actual, stock_minimo = articulo
        print(f"{codigo} - {nombre:<18}: Stock = {stock_actual} | Mínimo = {stock_minimo}")
    print("=" * 55)


# =====================================================================
# 3. EJECUCIÓN DEL PROGRAMA Y REPORTES
# =====================================================================

# Llamada al primer módulo: Mostrar cómo está el almacén hoy
mostrar_inventario(inventario)

# Llamada al segundo módulo: Generar la lista de pedidos de reabastecimiento
print("\n" + "=" * 45)
print("    CANTIDAD A PEDIR PARA REPONER")   
print("=" * 45) 
print(f"{'Artículo':<20} {'Cantidad a pedir'}")
print("-" * 45)

for articulo in inventario:
    # Desempaquetamos los 4 elementos de la fila en variables
    codigo, nombre, stock_actual, stock_minimo = articulo
        
    # Calculamos la cantidad llamando a la función
    cantidad_pendiente = calcular_cantidad_a_pedir(stock_actual, stock_minimo)
        
    # Imprimimos el artículo y el resultado de la función
    print(f"{nombre:<20} {cantidad_pendiente}")
        
print("=" * 45)
print("Fin del reporte de inventario.")