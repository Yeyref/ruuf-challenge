#  Calculadora de Paneles Solares – Proyecto Ruuf

Este proyecto nace del desafio de calcular cuántos paneles solares rectangulares pueden colocarse dentro de un techo tambien rectangular. A simple vista parece un problema sencillo, pero cuando empecé a probar casos, me di cuenta de que tenia mas complejidad de la esperada.

##  Descripción del problema

El objetivo es determinar **la cantidad máxima de paneles solares que caben en un techo**, considerando que los paneles se pueden rotar 90°.

- **Techo:** dimensiones `x` (ancho) e `y` (alto)  
- **Panel:** dimensiones `a` (ancho) y `b` (alto)

La idea es encontrar la mejor forma de acomodarlos sin cortar paneles ni superponerlos.

##  Lo que descubrí

Al principio pensé que bastaba con probar dos orientaciones:  
- paneles normales (a×b)  
- paneles rotados (b×a)

Pero al probar el caso `techo = 3×5` y `panel = 1×2`, el resultado esperado era 7 paneles, no 6.  
Ahí entendí que el problema no era tan directo:  a veces se obtienen mas paneles combinando distintas orientaciones en diferentes zonas del techo.

##  Enfoque y solución

Decidí diseñar un algoritmo que pruebe diferentes formas de dividir el techo y colocar paneles con distintas orientaciones.  
En total, el programa considera seis estrategias principales:

1. Todos los paneles normales (a×b)  
2. Todos los paneles rotados (b×a)  
3. Dividir el techo horizontalmente: arriba normales, abajo rotados  
4. Dividir horizontalmente (inverso): arriba rotados, abajo normales  
5. Dividir verticalmente: izquierda normales, derecha rotados  
6. Dividir verticalmente (inverso): izquierda rotados, derecha normales  

El algoritmo evalúa todas las divisiones posibles y devuelve el **máximo número de paneles completos** que se pueden instalar.

## Ejemplo de cálculo

**Caso:** Techo 3×5, Panel 1×2  

Si solo se usan paneles normales o rotados, se obtienen como máximo 6 paneles.  
Pero combinando orientaciones (por ejemplo, arriba rotados y abajo normales) se logra **colocar 7 paneles**.  

Ese fue el caso que me hizo ajustar todo el enfoque.

## Como ejecutar

**Requisitos:**  
- Python 3.6 o superior

**Ejecucion simple:**
```bash
python script.py
```
Uso desde otro codigo:
```bash
from script import calculate_panels

cantidad = calculate_panels(3, 5, 1, 2)
print(f"Caben {cantidad} paneles")  
# Output: 7
```
##Casos de prueba
Techo (x×y)	Panel (a×b)	Resultado esperado	Obtenido	
2×4	            1×2	            4	            4        
3×5	            1×2	            7	            7	      
1×10	        2×2	            0	            0	    

También agregué casos extremos, como paneles mas grandes que el techo o techos cuadrados, para asegurarme de que la función respondiera bien en todos los escenarios.

## Caracteristicas importantes

Los paneles no se cortan ni se superponen.

Solo se permiten rotaciones de 0° y 90°.

El techo se puede dividir en un máximo de dos zonas (horizontal o verticalmente).

Se busca el número máximo de paneles completos posibles.


## Lo que aprendí

Este proyecto me enseñó que los problemas de optimización geometrica no siempre tienen una solución evidente.
Probar distintas estrategias y combinar enfoques puede marcar la diferencia entre una solucion buena y una excelente.
Ademas, validar con casos extremos ayuda a encontrar errores que a primera vista no se ven.

Yeferson Rosales

Proyecto desarrollado como parte del proceso de selección de Ruuf Solar.
Cada estrategia fue analizada, probada y validada por mi, IA y la calculadora.
Estoy preparado para explicar cada decisión de diseño y optimización.

PD: Ademas del codigo principal, incluí un archivo de pruebas unitarias con todos los casos descritos anteriormente.