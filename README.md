# SecurePasswordGenerator

![Estado](https://img.shields.io/badge/status-completed-brightgreen) ![Licencia](https://img.shields.io/badge/license-MIT-blue)

Generador de contraseñas seguras, sencillo y configurable, pensado para crear contraseñas fuertes de forma rápida desde la interfaz (o línea de comandos si aplicable).

## Descripción

SecurePasswordGenerator es una herramienta ligera para generar contraseñas aleatorias y seguras. Permite configurar longitud, incluir mayúsculas, minúsculas, números y símbolos, y garantiza buena entropía para uso en cuentas personales o profesionales.

## Características

- Generación de contraseñas aleatorias y seguras.
- Opciones configurables: longitud, uso de mayúsculas, números y símbolos.
- Copiar al portapapeles con un clic (si la UI es web).
- Interfaz simple y clara.
- (Opcional) Soporte CLI para generar contraseñas desde la terminal.

## Capturas

> Añade aquí una o dos capturas de pantalla si tienes una interfaz gráfica:
- `docs/screenshot-1.png`
- `docs/screenshot-2.png`

## Tecnologías

- HTML / CSS / JavaScript (si es app web)
- O Node.js (si hay backend o paquete CLI)
- (Ajusta según corresponda)

## Requisitos

- Navegador moderno (para la versión web)
- Node.js >= 14 (si existe una versión con npm/CLI)

## Instalación (versión web)

1. Clona el repositorio:
   git clone https://github.com/thomaspolo67-ui/SecurePasswordGenerator.git
2. Abre `index.html` en tu navegador.

## Instalación (versión con Node / desarrollo)

1. Clona el repositorio:
   git clone https://github.com/thomaspolo67-ui/SecurePasswordGenerator.git
2. Entra a la carpeta del proyecto:
   cd SecurePasswordGenerator
3. Instala dependencias:
   npm install
4. Inicia la app en modo desarrollo:
   npm start
(Ajusta estos pasos si tu proyecto usa otra estructura o empaquetador.)

## Uso

- UI: Abre la app, selecciona la longitud y las opciones (mayúsculas, números, símbolos) y pulsa "Generar". Usa el botón "Copiar" para copiar la contraseña al portapapeles.
- CLI (si existe): 
  ```bash
  # Ejemplo hipotético
  npx secure-password-generator --length 16 --numbers --symbols
