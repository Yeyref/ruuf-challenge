def calculate_panels(x, y, a, b):
    """
    Calcula la cantidad máxima de paneles solares que caben en un techo rectangular.
    
    El algoritmo prueba múltiples configuraciones:
    1. Todas las orientaciones posibles (axb y bxa)
    2. Combinaciones de orientaciones en diferentes zonas del techo ***IMPORTANTE***

    Argumentos  :
        x (float): Ancho del techo
        y (float): Alto del techo
        a (float): Ancho del panel solar
        b (float): Alto del panel solar
    
    Retorna:
        int: Cantidad máxima de paneles que caben
    """
    
    # Validación: si el panel no cabe en ninguna orientación
    if (a > x and b > y) or (b > x and a > y):
        return 0
    
    max_paneles = 0
    
    # Estrategia 1: Todos los paneles en orientación normal (a×b)
    if a <= x and b <= y:
        paneles = int(x // a) * int(y // b)
        max_paneles = max(max_paneles, paneles)
    
    # Estrategia 2: Todos los paneles rotados (b×a)
    if b <= x and a <= y:
        paneles = int(x // b) * int(y // a)
        max_paneles = max(max_paneles, paneles)
    
    # Estrategia 3: Dividir el techo horizontalmente
    # Parte superior con orientación 1, parte inferior con orientación 2
    if a <= x and b <= y:
        # Llenar arriba con paneles a×b
        filas_arriba = int(y // b)
        for filas in range(filas_arriba + 1):
            paneles_arriba = int(x // a) * filas
            espacio_restante_y = y - (filas * b)
            
            # Llenar el espacio restante con paneles rotados b×a
            if b <= x and a <= espacio_restante_y:
                paneles_abajo = int(x // b) * int(espacio_restante_y // a)
                total = paneles_arriba + paneles_abajo
                max_paneles = max(max_paneles, total)
    
    # Estrategia 4: Dividir el techo horizontalmente (inverso)
    # Parte superior con orientación 2, parte inferior con orientación 1
    if b <= x and a <= y:
        filas_arriba = int(y // a)
        for filas in range(filas_arriba + 1):
            paneles_arriba = int(x // b) * filas
            espacio_restante_y = y - (filas * a)
            
            if a <= x and b <= espacio_restante_y:
                paneles_abajo = int(x // a) * int(espacio_restante_y // b)
                total = paneles_arriba + paneles_abajo
                max_paneles = max(max_paneles, total)
    
    # Estrategia 5: Dividir el techo verticalmente
    # Parte izquierda con orientación 1, parte derecha con orientación 2
    if a <= x and b <= y:
        columnas_izq = int(x // a)
        for cols in range(columnas_izq + 1):
            paneles_izq = cols * int(y // b)
            espacio_restante_x = x - (cols * a)
            
            if b <= espacio_restante_x and a <= y:
                paneles_der = int(espacio_restante_x // b) * int(y // a)
                total = paneles_izq + paneles_der
                max_paneles = max(max_paneles, total)
    
    # Estrategia 6: Dividir el techo verticalmente (inverso)
    if b <= x and a <= y:
        columnas_izq = int(x // b)
        for cols in range(columnas_izq + 1):
            paneles_izq = cols * int(y // a)
            espacio_restante_x = x - (cols * b)
            
            if a <= espacio_restante_x and b <= y:
                paneles_der = int(espacio_restante_x // a) * int(y // b)
                total = paneles_izq + paneles_der
                max_paneles = max(max_paneles, total)
    
    return max_paneles


def main():
    """
    Función principal para probar el algoritmo con los ejemplos dados
    """
    print("=" * 60)
    print("CALCULADORA DE PANELES SOLARES - RUUF")
    print("=" * 60)
    print()

    # Casos de prueba del enunciado
    test_cases = [
        {"x": 2, "y": 4, "a": 1, "b": 2, "esperado": 4},
        {"x": 3, "y": 5, "a": 1, "b": 2, "esperado": 7},
        {"x": 1, "y": 10, "a": 2, "b": 2, "esperado": 0},
    ]
    
    print("CASOS DE PRUEBA:")
    print("-" * 60)
    
    todos_correctos = True
    for i, test in enumerate(test_cases, 1):
        resultado = calculate_panels(test["x"], test["y"], test["a"], test["b"])
        estado = "CORRECTO" if resultado == test["esperado"] else "ERROR"
        
        if resultado != test["esperado"]:
            todos_correctos = False
        
        print(f"Caso {i}:")
        print(f"  Techo: {test['x']} x {test['y']}")
        print(f"  Panel: {test['a']} x {test['b']}")
        print(f"  Resultado: {resultado}")
        print(f"  Esperado: {test['esperado']}")
        print(f"  Estado: {estado}")
        print()
    
    if todos_correctos:
        print("TODOS LOS CASOS PASARON CORRECTAMENTE ")
        print()
    
    print("CASOS ADICIONALES: ")
    print("-" * 60)
    
    ejemplos_extra = [
        (10, 10, 2, 2),
        (5, 5, 3, 2),
        (8, 6, 2, 3),
        (6, 8, 2, 3),
    ]
    
    for x, y, a, b in ejemplos_extra:
        resultado = calculate_panels(x, y, a, b)
        print(f"Techo {x}x{y}, Panel {a}x{b} → Caben {resultado} paneles")


if __name__ == "__main__":
    main()