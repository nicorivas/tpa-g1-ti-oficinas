# REVIEW.md: cómo se revisa un cambio en este repositorio

Claude lee este archivo cuando le pides que revise un pull request. Ejemplo de la clase 1.

Revisa estos cinco puntos y responde cada uno con «sí», «no» o «no sé»:

1. **Datos:** ¿el cambio está libre de información que no debería estar? (RUT, correos, nombres de personas). Si un dato personal ya está en `main`, por ejemplo en `notas-reunion.md`, la revisión debe pedir que se borre y que no se copie al pull request. No se aprueba un repositorio que incumple su propia regla.
2. **Condiciones:** ¿respeta el `CLAUDE.md` y las reglas del proyecto?
3. **Decisión:** ¿lo entiendes y te harías responsable de aprobarlo? Si no se entiende sin quien lo escribió, no se aprueba.
4. **Alcance:** ¿cambia solo lo que se pidió? Mira la lista de archivos. En el pull request de un autor no debe aparecer `traspaso.md`: lo escribe el grupo al cerrar.
5. **Traspaso:** ¿explica qué cambió y por qué, y declara las decisiones que las reglas no cubren?

Además, en este caso: si el cambio trae un CAC, recalcúlalo con `datos/` y la fórmula de `reglas.md`, y mira si señala los días raros de los últimos 30 días (gasto muy alto, ventas en cero, filas repetidas o vacías). Pasar `verificar.py` no basta.

Termina con una recomendación: aprobar, pedir cambios o no aprobar, y di por qué.
