# Hito 4 — Dashboard Interactivo (Grafana)

Tablero de control académico construido en **Grafana**, conectado a una base
**SQLite** generada a partir del dataset limpio del Hito 2. Cumple el requisito
del Hito 4: una interfaz donde el usuario filtra por **comisión** y **turno** y
los KPIs y gráficos se actualizan **en tiempo real**.

## Qué muestra el dashboard

8 paneles que responden las 3 preguntas del análisis (Hito 1):

| Panel | Tipo | Qué responde |
|-------|------|--------------|
| Tasa de Presentación al Parcial | Stat | % de alumnos que se presentaron (no ausentes) |
| Alumnos Aprobados | Stat | Cantidad con nota ≥ 6 |
| Alumnos en Riesgo (Constancia < 43%) | Stat | Alumnos bajo el umbral de alerta de abandono |
| Total Alumnos (filtrados) | Stat | Tamaño del subconjunto filtrado |
| Distribución de Estados Finales | Pie | Aprobado / Recupera / Desaprobado / Ausente |
| Nota Promedio del Parcial por Comisión | Barras | Comparativa entre las 9 comisiones (umbral 6) |
| Índice de Constancia — Ausentes vs Presentes | Barras | La brecha que predice el abandono |
| Evolución de Nota y Tasa de Entrega | Líneas | Caída de la entrega a lo largo del cuatrimestre |

Los dos filtros superiores (**Turno**, **Comisión**) recalculan todos los
paneles salvo el de evolución temporal, que es una vista global del cuatrimestre.

## Arquitectura de datos

```
data/datos_limpios.csv  (700 alumnos, salida del ETL del Hito 2)
data/Calificaciones.csv (5.610 entregas, dataset crudo)
        │  construir_base.py
        ▼
data/academico.db  (SQLite, 2 tablas: alumnos + entregas)
        │  plugin frser-sqlite-datasource
        ▼
Grafana :3000  →  dashboard con 8 paneles + 2 filtros en tiempo real
```

Elegimos SQLite (en vez de leer el CSV directo) porque las queries SQL permiten
que los filtros de comisión y turno funcionen de verdad: cada panel ejecuta un
`SELECT ... WHERE Turno IN ($Turno) AND Comision IN ($Comision)`.

## Cómo reproducirlo desde cero

### 1. Generar la base de datos
```powershell
cd hito-4
python construir_base.py
```
Genera `data/academico.db`. (Requiere `pip install pandas`.)

### 2. Instalar Grafana OSS
```powershell
winget install GrafanaLabs.Grafana.OSS
```
Queda corriendo como servicio en http://localhost:3000 (login inicial `admin` / `admin`).

### 3. Instalar el plugin SQLite
Descargar `frser-sqlite-datasource` (release de GitHub) y descomprimir en una
carpeta de plugins. Luego, en `conf/custom.ini` de Grafana:
```ini
[paths]
plugins = C:\Users\<usuario>\grafana-plugins

[plugins]
allow_loading_unsigned_plugins = frser-sqlite-datasource
```
Reiniciar el servicio de Grafana.

### 4. Crear el datasource
En Grafana → Connections → Data sources → SQLite, con el campo **Path** apuntando
a la ruta absoluta de `data/academico.db`.

### 5. Importar el dashboard
En Grafana → Dashboards → Import → subir `dashboard/dashboard-tpi-grupo7.json`,
y seleccionar el datasource SQLite cuando lo pida.

## Archivos de este hito

```
hito-4/
├── construir_base.py        # CSV → SQLite (reproducible)
├── verificar_queries.py     # chequeo de las 6 queries contra la base
├── data/
│   ├── Calificaciones.csv   # crudo (5.610 filas)
│   ├── datos_limpios.csv    # procesado (700 alumnos)
│   └── academico.db         # base SQLite generada
├── dashboard/
│   └── dashboard-tpi-grupo7.json  # dashboard de Grafana (importable)
└── HITO4_README.md
```
