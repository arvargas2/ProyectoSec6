# 🎵 Sistema de Gestión de Canciones

Aplicación desarrollada en **Python** que permite administrar una colección de canciones mediante un menú interactivo. El proyecto está diseñado para practicar el uso de funciones, estructuras de datos, validaciones y lógica de programación.

## 📌 Características

- Agregar nuevas canciones.
- Buscar canciones por título.
- Eliminar canciones.
- Marcar canciones como favoritas.
- Listar todas las canciones registradas.
- Validación de datos ingresados por el usuario.

## 📂 Estructura de los datos

Cada canción se almacena como un **diccionario** dentro de una lista llamada `canciones_list`.

```python
cancion = {
    "titulo": "Imagine",
    "artista": "John Lennon",
    "duracion": 183,
    "favorita": False
}
```

## ✅ Validaciones

El sistema valida la información antes de registrar una canción:

| Campo | Validación |
|--------|------------|
| Título | No puede estar vacío ni contener solo espacios. |
| Artista | No puede estar vacío ni contener solo espacios. |
| Duración | Debe ser un número entero mayor que cero. |
| Favorita | Se inicializa automáticamente en `False`. |

## 📋 Menú Principal

```
========== MENÚ PRINCIPAL ==========
1. Agregar canción
2. Buscar canción
3. Eliminar canción
4. Marcar como favorita
5. Mostrar canciones
6. Salir
====================================
```

## ⚙️ Funcionalidades

### ➕ Agregar canción
- Solicita título, artista y duración.
- Valida todos los datos.
- Registra la canción con `favorita = False`.

### 🔍 Buscar canción
- Busca una canción por su título.
- Retorna su posición en la lista o `-1` si no existe.

### ❌ Eliminar canción
- Elimina una canción utilizando la función de búsqueda.
- Informa al usuario si la canción no existe.

### ⭐ Marcar como favorita
- Cambia el estado de una canción a favorita.
- Evita marcar nuevamente una canción que ya es favorita.

### 📄 Mostrar canciones
Muestra para cada canción:

- Título
- Artista
- Duración (segundos)
- Estado (`FAVORITA` o `NORMAL`)

Si no existen registros, informa al usuario.

### 🚪 Salir
Finaliza la ejecución del programa mostrando un mensaje de despedida.

## 🧠 Conceptos aplicados

- Funciones
- Diccionarios
- Listas
- Menús interactivos
- Validación de datos
- Estructuras condicionales
- Ciclos
- Comparaciones
- Búsquedas secuenciales
- Manipulación de listas (CRUD)

## 🎯 Objetivo

Fortalecer los fundamentos de programación en Python mediante el desarrollo de una aplicación modular que implemente operaciones básicas sobre una colección de datos utilizando funciones y estructuras nativas del lenguaje.
