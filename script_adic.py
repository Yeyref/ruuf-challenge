"""
Archivo de pruebas para la función calculate_panels
"""

from script import calculate_panels


def test_caso_1():
    """Prueba: Techo 2x4, Panel 1x2 → Espera 4"""
    resultado = calculate_panels(2, 4, 1, 2)
    assert resultado == 4, f"Esperado 4, obtenido {resultado}"
    print("✅ Caso 1 pasó: Techo 2x4, Panel 1x2 → 4 paneles")


def test_caso_2():
    """Prueba: Techo 3x5, Panel 1x2 → Espera 7"""
    resultado = calculate_panels(3, 5, 1, 2)
    assert resultado == 7, f"Esperado 7, obtenido {resultado}"
    print("✅ Caso 2 pasó: Techo 3x5, Panel 1x2 → 7 paneles")


def test_caso_3():
    """Prueba: Techo 1x10, Panel 2x2 → Espera 0"""
    resultado = calculate_panels(1, 10, 2, 2)
    assert resultado == 0, f"Esperado 0, obtenido {resultado}"
    print("✅ Caso 3 pasó: Techo 1x10, Panel 2x2 → 0 paneles")


def test_casos_adicionales():
    """Pruebas adicionales para validar la robustez"""
    
    # Caso 4: Techo y panel del mismo tamaño
    resultado = calculate_panels(5, 5, 5, 5)
    assert resultado == 1, f"Caso 4 falló: Esperado 1, obtenido {resultado}"
    print("✅ Caso 4 pasó: Techo 5x5, Panel 5x5 → 1 panel")
    
    # Caso 5: Techo cuadrado, panel rectangular
    resultado = calculate_panels(10, 10, 2, 5)
    esperado = max(5*2, 2*5)  # Ambas orientaciones dan 10
    assert resultado == esperado, f"Caso 5 falló: Esperado {esperado}, obtenido {resultado}"
    print(f"✅ Caso 5 pasó: Techo 10x10, Panel 2x5 → {resultado} paneles")
    
    # Caso 6: Panel más grande que techo
    resultado = calculate_panels(3, 3, 5, 5)
    assert resultado == 0, f"Caso 6 falló: Esperado 0, obtenido {resultado}"
    print("✅ Caso 6 pasó: Techo 3x3, Panel 5x5 → 0 paneles")
    
    # Caso 7: Techo muy largo y delgado
    resultado = calculate_panels(1, 100, 1, 10)
    assert resultado == 10, f"Caso 7 falló: Esperado 10, obtenido {resultado}"
    print("✅ Caso 7 pasó: Techo 1x100, Panel 1x10 → 10 paneles")


def run_all_tests():
    """Ejecuta todas las pruebas"""
    print("\n" + "="*60)
    print("EJECUTANDO PRUEBAS DEL ALGORITMO")
    print("="*60 + "\n")
    
    try:
        test_caso_1()
        test_caso_2()
        test_caso_3()
        test_casos_adicionales()
        
        print("\n" + "="*60)
        print("✅ TODAS LAS PRUEBAS PASARON EXITOSAMENTE")
        print("="*60 + "\n")
        return True
        
    except AssertionError as e:
        print(f"\n❌ ERROR: {e}\n")
        return False


if __name__ == "__main__":
    run_all_tests()