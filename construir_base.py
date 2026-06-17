"""
Hito 4 — Construcción de la base de datos SQLite para Grafana.

Convierte los CSV del ETL (Hito 2) en una base SQLite que Grafana consulta
mediante el plugin frser-sqlite-datasource. Crea dos tablas:

  - alumnos:   1 fila por alumno (700 filas) — base de los KPIs y la mayoría
               de los paneles. Permite filtrar por Turno y Comisión.
  - entregas:  1 fila por entrega (5.610 filas) — necesaria para el panel de
               evolución temporal por actividad.

Uso:
    python construir_base.py

Genera: data/academico.db
"""

import os
import sqlite3

import pandas as pd

# Rutas relativas a este script
DIR = os.path.dirname(os.path.abspath(__file__))
RUTA_LIMPIOS = os.path.join(DIR, "data", "datos_limpios.csv")
RUTA_CRUDO = os.path.join(DIR, "data", "Calificaciones.csv")
RUTA_DB = os.path.join(DIR, "data", "academico.db")


def cargar_alumnos(ruta: str) -> pd.DataFrame:
    """Carga datos_limpios.csv (1 fila por alumno) y selecciona las columnas necesarias."""
    df = pd.read_csv(ruta)
    columnas = [
        "ID_Alumno", "Nombre_Apellido", "Edad", "Genero", "Comision", "Turno",
        "Entregas_Previas", "Entregas_A_Tiempo", "Total_Actividades_Previas",
        "Promedio_Previo", "Indice_Constancia", "Nota_Parcial", "Estado_Final",
    ]
    return df[columnas].copy()


def cargar_entregas(ruta: str) -> pd.DataFrame:
    """Carga Calificaciones.csv (1 fila por entrega) y parsea nota y fechas."""
    df = pd.read_csv(ruta)
    # La nota cruda viene con coma decimal y a veces vacía (no entregó).
    df["Nota"] = pd.to_numeric(
        df["Nota"].astype(str).str.replace(",", ".", regex=False), errors="coerce"
    )
    df["Fecha_Limite"] = pd.to_datetime(df["Fecha_Limite"], errors="coerce", format="mixed")
    # Marca si hubo entrega (la nota existe) — usado para la tasa de entrega.
    df["Hizo_Entrega"] = df["Nota"].notna().astype(int)
    return df


def construir_base() -> None:
    alumnos = cargar_alumnos(RUTA_LIMPIOS)
    entregas = cargar_entregas(RUTA_CRUDO)

    if os.path.exists(RUTA_DB):
        os.remove(RUTA_DB)

    con = sqlite3.connect(RUTA_DB)
    try:
        alumnos.to_sql("alumnos", con, index=False)
        entregas.to_sql("entregas", con, index=False)
        con.commit()
    finally:
        con.close()

    print(f"[OK] Base creada: {RUTA_DB}")
    print(f"     Tabla 'alumnos':  {len(alumnos)} filas")
    print(f"     Tabla 'entregas': {len(entregas)} filas")


if __name__ == "__main__":
    construir_base()
