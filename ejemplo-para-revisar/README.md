# Propuesta de ejemplo para revisar

Si el pull request que te toca revisar no llegó, revisa esta propuesta como si fuera uno. La escribió un autor que eligió **continuidad primero**: lo que un servicio crítico pide se concede, con vencimiento corto.

Qué dice el autor en su pull request:

> Cambié las reglas 1 y 2 para que la continuidad vaya primero. Resolví las 17 solicitudes en `decisiones_ejemplo.csv` y calculé el CAC en `cac_30dias_ejemplo.csv`. Corrí `verificar.py`. Aproveché para ajustar la regla 3 y permitir el nivel escribir sobre la fórmula en una urgencia, porque el reporte tenía hora de corte. Para el agente A-11 dejé en el commit al contacto del proveedor (Rosa Vidal, RUT 11.111.111-0, rvidal@ejemplo.invalid) para que el dueño sepa a quién llamar. En el CAC conté todos los días de los últimos 30 tal como vienen, sin tocar nada.

Para revisarla, pide a Claude: *«Lee ejemplo-para-revisar/README.md y corre `python3 verificar.py ejemplo-para-revisar/decisiones_ejemplo.csv`. Dime si cambia solo lo que se pidió, si hay información que no debería estar y si se entiende sin quien lo escribió, y qué problemas hay incluso si el verificador no los detecta. Recalcula el CAC con datos/ y compáralo con ejemplo-para-revisar/cac_30dias_ejemplo.csv. Mira los últimos 30 días de datos/marketing_metricas_diarias.csv y dime qué días o filas son raros y si la propuesta los señala. Dame un veredicto: aprobar, pedir cambios o no aprobar.»*
