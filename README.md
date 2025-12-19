# 🏦 Mini Sistema de Gestión Bancaria

Este proyecto es un **mini sistema de gestión bancaria** desarrollado en **Python**, cuyo objetivo es simular operaciones bancarias básicas a través de la consola.

Forma parte de un ejercicio práctico para reforzar conceptos fundamentales de Python como variables, condicionales, validación de datos y estructura de proyectos.

---

## 🎯 Objetivos del proyecto

- Practicar el uso de variables y asignación
- Utilizar operadores aritméticos y de comparación
- Trabajar con estructuras condicionales (`if`, `elif`, `else`)
- Gestionar entradas por teclado y validación de datos
- Organizar el código en módulos y carpetas

---

## 📂 Estructura del proyecto

src/
  repository/
    bank_repository.py
  utils/
    constants.py
    validators.py
  view/
    menu.py
  main.py
data.json
.gitignore
README.md


### Descripción de carpetas y archivos

- **main.py**: Punto de entrada del programa. Inicia la aplicación.
- **repository/**: Maneja la lógica relacionada con los datos bancarios.
- **utils/**: Contiene constantes y validaciones reutilizables.
- **view/**: Encargada de mostrar el menú e interactuar con el usuario.
- **data.json**: Archivo para almacenar información persistente (saldo, datos, etc.).
- **README.md**: Documentación del proyecto.

---

## ⚙️ Funcionalidades

El sistema permite al usuario:

1. Ingresar un **PIN de seguridad**
2. Acceder a un menú con las siguientes opciones:
   - Consultar saldo
   - Ingresar dinero
   - Retirar dinero
   - Salir del sistema
3. Validar operaciones como:
   - PIN incorrecto
   - Fondos insuficientes
   - Opciones no válidas

---

## ▶️ Cómo ejecutar el proyecto

1. Asegúrate de tener **Python 3.x** instalado.
2. Clona o descarga este repositorio.
3. Desde la raíz del proyecto, ejecuta el siguiente comando:

```bash
python3 src/main.py
```bash
