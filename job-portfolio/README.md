# Portfolio — Job Pulache Carreño

Dashboard interactivo (Streamlit + Plotly) para compartir con empresas agroindustriales.

## Probarlo en tu compu

```bash
pip install -r requirements.txt
streamlit run app.py
```

Se abre en `http://localhost:8501`.

## Publicarlo gratis (para tener un link que enviar a empresas)

1. Sube esta carpeta a un repositorio en GitHub (público o privado).
2. Entra a **share.streamlit.io** con tu cuenta de GitHub.
3. Click en "New app", elige el repo, la rama y `app.py` como archivo principal.
4. Deploy. En un par de minutos tienes un link tipo
   `https://job-pulache-portfolio.streamlit.app` para compartir por WhatsApp, LinkedIn o correo.

## Estructura

```
app.py              -> toda la app (una sola página)
assets/
  profile_natural.jpg   -> tu foto, recortada y retocada
  profile_duotone.jpg   -> versión duotono verde/carbón (por si quieres usarla en LinkedIn)
.streamlit/config.toml -> tema base de Streamlit
requirements.txt
```

## Cómo personalizar

- **Textos y experiencia**: busca la lista `timeline` y los bloques `case-card` dentro de `app.py`.
- **Colores**: al inicio del archivo, en el diccionario `C` (hay uno para modo oscuro y uno para claro).
- **Datos del simulador**: diccionario `MOCK_PRODUCERS` — son datos de ejemplo, no reales.
- **Foto**: reemplaza los archivos en `assets/` manteniendo el mismo nombre.
