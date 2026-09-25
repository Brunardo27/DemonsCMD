# DemonsCMD
<h3>DemonsCMD - Geometry Dash Demon manager</h3>
<h6>Versión 1.2.1</h6>

Este programa es una linea de comandos donde los archivos son demons. Te permite apuntar los demons que te has pasado y analizarlos.

Estructura del código:

    DemonsCMDV1.2.1
        - main.py
            - Importaciones
            - Diccionario de comandos
            - Bucle principal
                - Formateo del input con split()
                - Ejecución del comando
                - Guardado de datos (demons.json)
        - comandos.py
            - Carga de demons.json a una variable
            - Diccionario de atributos
            - Lista de dificultades
            - Funciones (Comandos)
                - split
                - numNam
                - demonList
                - info
                - count
                - create
                - delete
                - change
        - demons.json
            - Diccionario con los demons y sus propiedades
