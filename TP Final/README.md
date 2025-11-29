# TP Final – Programación I  
### Sistema de Gestión de Países (CSV)

## 👥 Integrantes
- **Diaz Chiara**  
- **Ludueña Fernando**  
**Materia:** Programación I – Tecnicatura Universitaria en Programación (UTN)

---

## 📌 Descripción General del Programa

Este proyecto es una aplicación de consola en Python que permite gestionar información sobre países utilizando un archivo **CSV** como almacenamiento persistente.  
El programa cumple con los requisitos de la materia Programación I: no se usan librerías externas ni manejo avanzado de excepciones; la lógica está implementada con estructuras básicas (listas, funciones y CSV).

Cada país contiene:
- **Nombre**
- **Población**
- **Superficie (km²)**
- **Continente**

---

## 🧩 Funcionalidades

1. **Agregar un país**  
   - Se ingresan: nombre, población, superficie y continente.  
   - Validaciones: campos obligatorios, población y superficie numéricas, se evita duplicado por nombre (case-insensitive).

2. **Mostrar todos los países**  
   - Muestra cada registro en formato:  
     `Nombre – Continente | población hab | superficie km²`

3. **Actualizar un país existente**  
   - Modifica población y superficie; reescribe el CSV para mantener coherencia.

4. **Buscar país por nombre**  
   - Búsqueda parcial (no case-sensitive).

5. **Filtrar países**  
   - Por continente, por rango de población o por rango de superficie.

6. **Ordenar países**  
   - Orden ascendente/descendente por: nombre, población o superficie.  
   - Uso de `lambda` para claves de ordenamiento (explicado en el código).

7. **Mostrar estadísticas**  
   - País con mayor/menor población, promedios de población y superficie, y conteo por continente.

---

## 🗂 Archivo utilizado

## 🗂 Archivo utilizado
El sistema trabaja con:

```
paises.csv
```

Con las columnas:
```
nombre, poblacion, superficie, continente
```

---

## 🖼 Capturas de pantalla

[### 📌 Menú principal](./img/menuprincipal.png)

[### 📌 Agregar Pais](./img/agregarpais.png)

[### 📌 Buscar Pais](./img/busquedapais.png)

[### 📌 Filtrar Pais Por Continente](./img/filtroporcontinente.png)

[### 📌 Filtrar Pais Por Cantidad de Habitantes](./img/filtroporxhabitantes.png)

[### 📌 Filtrar Pais Por Superficie](./img/filtroporsuperficie.png)

[### 📌 Orden Por Nombre](./img/ordenpornombre.png)

[### 📌 Orden Por Habitantes](./img/ordenporhabitantes.png)

[### 📌 Orden por Superficie](./img/ordenporsuperficie.png)

[### 📌 Estadisticas](./img/estadisticas.png)

---

## ▶ Cómo ejecutar el programa

1. Descargar o clonar el repositorio.  
2. Tener instalado Python 3.x en adelante(solo requiere librerias basicas del mismo)
3. Ejecutar: python Nuevo.py
Nota: el archivo scv se genera automaticamente si no esta creado.

```
    MUCHAS GRACIAS!
```
