"""
Importa el dashboard de Grafana vía API, resolviendo el placeholder del datasource
y preservando correctamente la codificación UTF-8 (acentos y ñ).

Uso:
    python importar_dashboard.py <uid_datasource>
"""

import json
import os
import sys
import urllib.request

DIR = os.path.dirname(os.path.abspath(__file__))
RUTA_DASH = os.path.join(DIR, "dashboard", "dashboard-tpi-grupo7.json")

GRAFANA_URL = "http://localhost:3000"
USER = "admin"
PASSWORD = "admin1234"


def importar(ds_uid: str) -> None:
    with open(RUTA_DASH, encoding="utf-8") as f:
        texto = f.read()
    texto = texto.replace("${DS_SQLITE}", ds_uid)
    dashboard = json.loads(texto)

    payload = {
        "dashboard": dashboard,
        "overwrite": True,
        "message": "Import via python (UTF-8 correcto)",
    }
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")

    # Auth básica
    import base64
    cred = base64.b64encode(f"{USER}:{PASSWORD}".encode()).decode()

    req = urllib.request.Request(
        f"{GRAFANA_URL}/api/dashboards/db",
        data=data,
        method="POST",
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": f"Basic {cred}",
        },
    )
    with urllib.request.urlopen(req) as resp:
        resultado = json.loads(resp.read().decode("utf-8"))
    print(f"[OK] Dashboard importado. Versión: {resultado.get('version')}")
    print(f"     URL: {GRAFANA_URL}{resultado.get('url')}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python importar_dashboard.py <uid_datasource>")
        sys.exit(1)
    importar(sys.argv[1])
