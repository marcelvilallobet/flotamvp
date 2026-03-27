# Flota MVP — Guía para publicar en Google Play

## Resumen
Estos archivos son una PWA wrapper que envuelve tu app de AppSheet.
Vamos a subirlos a GitHub Pages (gratis) y luego usar PWABuilder para generar el APK.

---

## PASO 1: Crear cuenta en GitHub (si no tienes)
1. Ve a https://github.com y crea una cuenta gratuita

## PASO 2: Crear un repositorio nuevo
1. En GitHub, haz clic en **"New repository"** (botón verde "+" arriba a la derecha)
2. Nombre: `flota-mvp` (sin espacios)
3. Ponlo como **Public**
4. NO marques "Add a README"
5. Haz clic en **"Create repository"**

## PASO 3: Subir los archivos
1. En tu nuevo repositorio, haz clic en **"uploading an existing file"**
2. Arrastra TODOS estos archivos y carpetas:
   - `index.html`
   - `manifest.json`
   - `sw.js`
   - `offline.html`
   - `icons/` (la carpeta entera con los 4 iconos)
3. Haz clic en **"Commit changes"**

## PASO 4: Activar GitHub Pages
1. Ve a **Settings** (pestaña arriba del repo)
2. En el menú lateral, haz clic en **Pages**
3. En "Source" selecciona **Deploy from a branch**
4. En "Branch" selecciona **main** y carpeta **/ (root)**
5. Haz clic en **Save**
6. Espera 2-3 minutos y tu web estará en:
   `https://TU-USUARIO.github.io/flota-mvp/`

## PASO 5: Verificar que funciona
1. Abre `https://TU-USUARIO.github.io/flota-mvp/` en el móvil
2. Deberías ver la pantalla de carga azul y luego tu app de AppSheet
3. En Chrome, debería aparecerte la opción de "Instalar app"

## PASO 6: PWABuilder
1. Ve a https://www.pwabuilder.com/
2. Pega tu URL: `https://TU-USUARIO.github.io/flota-mvp/`
3. Ahora debería pasar TODOS los checks (manifest ✅, service worker ✅, iconos ✅)
4. Haz clic en **"Package for stores"**
5. Selecciona **Android**
6. Rellena los datos y descarga el paquete

## PASO 7: Subir a Google Play
1. Ve a https://play.google.com/console
2. Necesitas una cuenta de desarrollador (pago único de 25$)
3. Crea una nueva app y sube el AAB que generó PWABuilder
4. Rellena la ficha de la tienda (capturas, descripción, etc.)
5. Envía a revisión

---

## Notas importantes
- El icono es provisional — puedes reemplazar los PNG en la carpeta `icons/` por tu logo real
- Si cambias la URL de AppSheet, edita el `src` del iframe en `index.html`
- GitHub Pages es gratuito y no caduca

## Estructura de archivos
```
flota-mvp/
├── index.html          ← Página principal (wrapper de tu app)
├── manifest.json       ← Configuración PWA
├── sw.js               ← Service Worker
├── offline.html        ← Página sin conexión
└── icons/
    ├── icon-192.png
    ├── icon-512.png
    ├── icon-maskable-192.png
    └── icon-maskable-512.png
```
