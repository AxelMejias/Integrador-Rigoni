"""Verificación rápida de las queries SQL que usará cada panel de Grafana."""
import os
import sqlite3

DIR = os.path.dirname(os.path.abspath(__file__))
con = sqlite3.connect(os.path.join(DIR, "data", "academico.db"))
cur = con.cursor()

print("=== Panel 1: Tasa de Presentación al Parcial ===")
q = """SELECT ROUND(100.0 * SUM(CASE WHEN Estado_Final != 'Ausente' THEN 1 ELSE 0 END)
       / COUNT(*), 1) AS tasa FROM alumnos"""
print(cur.execute(q).fetchone())

print("\n=== Panel 2: Alumnos Aprobados ===")
print(cur.execute("SELECT COUNT(*) FROM alumnos WHERE Estado_Final = 'Aprobado'").fetchone())

print("\n=== Panel 3: Distribución de Estados ===")
for r in cur.execute("SELECT Estado_Final, COUNT(*) FROM alumnos GROUP BY Estado_Final"):
    print(r)

print("\n=== Panel 4: Nota Promedio por Comisión ===")
q = """SELECT Comision, ROUND(AVG(Nota_Parcial), 2) AS nota
       FROM alumnos GROUP BY Comision ORDER BY Comision"""
for r in cur.execute(q):
    print(r)

print("\n=== Panel 5: Índice de Constancia (Ausentes vs Presentes) ===")
q = """SELECT CASE WHEN Estado_Final = 'Ausente' THEN 'Ausente' ELSE 'Presente' END AS grupo,
       ROUND(AVG(Indice_Constancia), 1) AS prom, COUNT(*) AS n
       FROM alumnos GROUP BY grupo"""
for r in cur.execute(q):
    print(r)

print("\n=== Panel 6: Evolución por Actividad ===")
q = """SELECT Actividad, ROUND(AVG(Nota), 2) AS nota_prom,
       ROUND(100.0 * AVG(Hizo_Entrega), 1) AS tasa_entrega
       FROM entregas GROUP BY Actividad ORDER BY MIN(Fecha_Limite)"""
for r in cur.execute(q):
    print(r)

con.close()
print("\n[OK] Todas las queries corren sin error.")
