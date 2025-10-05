from typing import List, Tuple, Dict
import json

def calculate_panels(panel_width: int, panel_height: int, 
                    roof_width: int, roof_height: int) -> int:
    """
    Calcula la cantidad máxima de paneles solares que caben en un techo.
    
    Arguments:
        panel_width: Ancho del panel
        panel_height: Alto del panel
        roof_width: Ancho del techo
        roof_height: Alto del techo
    
    Returns:
        Cantidad máxima de paneles
    """
    # orden de los parametros
    x = roof_width
    y = roof_height
    a = panel_width
    b = panel_height
    
    # validaciones iniciales
    if (a > x and b > y) or (b > x and a > y):
        return 0
    
    max_paneles = 0
    
    # Estrategia 1: Todos los paneles en orientacion normal (a×b)
    if a <= x and b <= y:
        paneles = int(x // a) * int(y // b)
        max_paneles = max(max_paneles, paneles)
    
    # Estrategia 2: Todos los paneles rotados (b×a)
    if b <= x and a <= y:
        paneles = int(x // b) * int(y // a)
        max_paneles = max(max_paneles, paneles)
    
    # Estrategia 3: Dividir el techo horizontalmente
    if a <= x and b <= y:
        filas_arriba = int(y // b)
        for filas in range(filas_arriba + 1):
            paneles_arriba = int(x // a) * filas
            espacio_restante_y = y - (filas * b)
            
            if b <= x and a <= espacio_restante_y:
                paneles_abajo = int(x // b) * int(espacio_restante_y // a)
                total = paneles_arriba + paneles_abajo
                max_paneles = max(max_paneles, total)
    
    # Estrategia 4: Dividir horizontalmente (inverso)
    if b <= x and a <= y:
        filas_arriba = int(y // a)
        for filas in range(filas_arriba + 1):
            paneles_arriba = int(x // b) * filas
            espacio_restante_y = y - (filas * a)
            
            if a <= x and b <= espacio_restante_y:
                paneles_abajo = int(x // a) * int(espacio_restante_y // b)
                total = paneles_arriba + paneles_abajo
                max_paneles = max(max_paneles, total)
    
    # Estrategia 5: Dividir verticalmente
    if a <= x and b <= y:
        columnas_izq = int(x // a)
        for cols in range(columnas_izq + 1):
            paneles_izq = cols * int(y // b)
            espacio_restante_x = x - (cols * a)
            
            if b <= espacio_restante_x and a <= y:
                paneles_der = int(espacio_restante_x // b) * int(y // a)
                total = paneles_izq + paneles_der
                max_paneles = max(max_paneles, total)
    
    # Estrategia 6: Dividir verticalmente (inverso)
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


def run_tests() -> None:
    with open('test_cases.json', 'r') as f:
        data = json.load(f)
        test_cases: List[Dict[str, int]] = [
            {
                "panel_w": test["panelW"],
                "panel_h": test["panelH"],
                "roof_w": test["roofW"],
                "roof_h": test["roofH"],
                "expected": test["expected"]
            }
            for test in data["testCases"]
        ]
    
    print("Corriendo tests:")
    print("-------------------")
    
    for i, test in enumerate(test_cases, 1):
        result = calculate_panels(
            test["panel_w"], test["panel_h"], 
            test["roof_w"], test["roof_h"]
        )
        passed = result == test["expected"]
        
        print(f"Test {i}:")
        print(f"  Panels: {test['panel_w']}x{test['panel_h']}, "
              f"Roof: {test['roof_w']}x{test['roof_h']}")
        print(f"  Expected: {test['expected']}, Got: {result}")
        print(f"  Status: {'✅ PASSED' if passed else '❌ FAILED'}\n")


def main() -> None:
    print("🐕 Wuuf wuuf wuuf 🐕")
    print("================================\n")
    
    run_tests()


if __name__ == "__main__":
    main()