#!/usr/bin/env python3
"""Verifica que decisiones_propuesta.csv no rompa las reglas duras. Uso: python3 verificar.py [archivo.csv]
El archivo debe tener las columnas: solicitud_id, decision (conceder, denegar o escalar), nivel_concedido
(ninguno, leer, borrador, escribir o ejecutar), vencimiento_dias, regla_aplicada y motivo."""
import csv, sys
ag = {r["agente_id"]: r for r in csv.DictReader(open("datos/agentes.csv", encoding="utf-8"))}
sol = {r["solicitud_id"]: r for r in csv.DictReader(open("datos/solicitudes_acceso.csv", encoding="utf-8"))}
NIVELES = {"ninguno", "leer", "borrador", "escribir", "ejecutar"}
errores = []
filas = list(csv.DictReader(open(sys.argv[1] if len(sys.argv) > 1 else "decisiones_propuesta.csv", encoding="utf-8")))
vistas = set()
for f in filas:
    if any(f.get(k) is None for k in ("solicitud_id", "decision", "nivel_concedido")):
        errores.append(f"fila mal formada (¿quedaron marcas de conflicto?): {list(f.values())[:2]}"); continue
    s, d, n = f["solicitud_id"].strip(), f["decision"].strip().lower(), f["nivel_concedido"].strip().lower()
    if s not in sol: errores.append(f"{s}: no es una solicitud"); continue
    if s in vistas: errores.append(f"{s}: aparece más de una vez"); continue
    vistas.add(s)
    if d not in {"conceder", "denegar", "escalar"}: errores.append(f"{s}: decisión «{d}» no válida"); continue
    if n not in NIVELES: errores.append(f"{s}: nivel «{n}» no válido"); continue
    if d == "conceder" and n == "ninguno": errores.append(f"{s}: concede pero el nivel es ninguno")
    if d != "conceder" and n != "ninguno": errores.append(f"{s}: {d} pero el nivel concedido es {n}")
    if sol[s]["recurso_id"] == "R-05" and n == "escribir": errores.append(f"{s}: regla 3, nadie recibe escribir sobre la fórmula del CAC")
    a = ag.get(sol[s]["agente_id"])
    if a and a["estado"] == "prueba" and n in {"escribir", "ejecutar"}: errores.append(f"{s}: regla 4, {a['agente_id']} está en prueba y no puede {n}")
    if not f.get("regla_aplicada", "").strip(): errores.append(f"{s}: regla 8, falta la regla aplicada")
for s in sol:
    if s not in vistas: errores.append(f"{s}: no aparece en la propuesta")
print(f"{len(filas)} filas revisadas, {len(errores)} problemas")
for x in errores: print(" -", x)
sys.exit(1 if errores else 0)
