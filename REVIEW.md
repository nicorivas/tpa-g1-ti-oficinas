# REVIEW.md: cómo se revisa un cambio en este repositorio

Claude lee este archivo cuando le pides que revise un pull request. Ejemplo de la clase 1.

Revisa estos seis puntos y responde cada uno con «sí», «no» o «no sé»:

1. **Datos:** ¿hay información que no debería estar, en el pull request o ya en `main`? (RUT, correos, nombres de personas). Si un dato personal ya está en `main`, por ejemplo en `notas-reunion.md`, la revisión debe pedir que se borre y que no se copie al pull request. No se aprueba un repositorio que incumple su propia regla.
2. **Condiciones:** ¿respeta las reglas generales del equipo, las de `CLAUDE.md`?
3. **Decisión:** ¿se entiende sin quien lo escribió? Si no se entiende, no se aprueba.
4. **Alcance:** ¿cambió solo lo que se pidió? Mira la lista de archivos. En el pull request de un autor no debe aparecer `traspaso.md`: lo escribe el grupo al cerrar.
5. **Traspaso:** ¿la descripción explica qué cambió y por qué, y declara las decisiones que las reglas no cubren?
6. **Cálculo:** si el cambio trae un CAC, ¿coincide con la fórmula de `reglas.md` al recalcularlo con `datos/`? ¿Señala los días raros de los últimos 30 días (gasto muy alto, ventas en cero, filas repetidas o vacías)?

Termina con una recomendación: aprobar, pedir cambios o no aprobar, y di por qué.
