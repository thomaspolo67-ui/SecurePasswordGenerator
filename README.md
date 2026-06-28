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

<img width="1366" height="705" alt="image" src="https://github.com/user-attachments/assets/5291b878-f12f-4eb4-bfde-55a8858177b2" />



## Tecnologías

- python
- Visual Studio Code
- Librerías:
-Tkinter
-Random
-String


## Uso

- UI: Abre la app, selecciona la longitud y las opciones (mayúsculas, números, símbolos) y pulsa "Generar". Usa el botón "Copiar" para copiar la contraseña al portapapeles.
- CLI (si existe): 
  ```bash
  # Ejemplo hipotético
  npx secure-password-generator --length 16 --numbers --symbols
