# Taller de fabricaci贸n digital con COMPAS FAB

> 8-10-15 Marzo 2022

![Flyer](images/compas-lightpainting-bg.jpg)

馃憠 [Presentaci贸n](https://docs.google.com/presentation/d/15yLLKv6W3ld0PMNl8Bb22njB9GQ33CGZL1jOqBRUKS8) | [General](#general) | [Ejemplos](examples/) | [Requisitos](#requisitos) | [Instalaci贸n](#instalaci贸n)

## General

### D铆a 1

* Introducci贸n a la fabricaci贸n digital.
* Introducci贸n a COMPAS framework.
* Conceptos fundamentales de rob贸tica: componentes de un robot industrial, 谩rea de trabajo de un robot, modos de control, posicionamiento de un robot y singularidades, marcos de coordenadas de un robot y transformaciones.
* Descripci贸n de modelos de robots, el formato URDF, visualizaci贸n de modelos de robots, interoperabilidad con modelos en sistemas externos. Ejercicio: construye tu propio modelo de robot.
* Cinem谩tica directa e inversa (soluci贸n anal铆tica y num茅rica).

### D铆a 2

* Backends de rob贸tica.
* ROS: Robot Operating System y el framework de planificaci贸n MoveIt!. Modelo de comunicaci贸n de ROS: topics, services y actions.
* Planificaci贸n de movimiento: planificaci贸n en espacio cartesiano y en espacio libre utilizando MoveIt. Definici贸n de restricciones de objetivo.
* Manipulaci贸n de la escena de planificaci贸n. Fijaci贸n y separaci贸n din谩mica de end-effectors.
* Ejercicio: planificaci贸n de movimiento de una tarea de pick & place.

### D铆a 3

* Comparaci贸n de modos de control: offline, online en real-time, online non-real-time.
* Control de robots ABB con COMPAS RRC.
* Primitivas de control de RRC: bloqueantes, no-bloqueantes, y bloqueo diferido.
* Set de instrucciones de RRC: movimiento, control de IO, personalizaci贸n.
* Control de robots UR con `ur-rtde`.
* Control de robots UR con ROS-Industrial.

## Requisitos

* Sistema Operativo m铆nimo: Windows 10 Pro or Mac OS Sierra 10.12
* [Anaconda 3](https://www.anaconda.com/distribution/)
* [Docker Desktop](https://www.docker.com/products/docker-desktop) Una vez instalado, puede ser necesario activar la opci贸n de `"Virtualization"` en el BIOS del ordenador, especialmente si se usa Windows.
* [Blender 3.0](https://www.blender.org/download): Es recomendable utilizar la version portable para aislar en entorno de trabajo.
* [Visual Studio Code](https://code.visualstudio.com/): Cualquier editor de python funciona, pero es recomendable utilizar VS Code junto con algunas extensiones, [consultar la documentaci贸n para mas detalles](https://gramaziokohler.github.io/compas_fab/latest/getting_started.html#working-in-visual-studio-code).

## Instalaci贸n

Utilizamos `conda` para asegurar un entorno limpio y aislado de dependencias.

<details><summary>Primera vez utilizando  <code>conda</code>?</summary>
<p>

Ejecutar primero el siguiente comando al menos una vez:

    (base) conda config --add channels conda-forge

</p>
</details>

    (base) conda env create -f https://dfab.link/db22.yml

### Verificaci贸n de la instalaci贸n

    (base)  conda activate fab22
    (fab22) python -m compas

    Yay! COMPAS is installed correctly!

    COMPAS: 1.14.1
    Python: 3.9.10 (CPython)
    Extensions: ['compas-fab', 'compas-cgal', 'compas-rrc']

### Materiales del taller

    (fab22) cd Documentos
    (fab22) git clone https://github.com/gramaziokohler/workshop_donbosco_2022

### Instalaci贸n en Blender

#### Opci贸n 1

Instalar paquetes utilizando el interprete de python integrado en Blender 3.0.

    (base)  cd DIRECTORIO_DE_BLENDER
    (base)  cd 3.0/python/bin
    (base)  python -m pip install compas_fab ur-rtde

#### Opci贸n 2

Utilizar Blender 3.0.1. portable con `COMPAS FAB` pre-instalado: https://wolke.ethz.ch/s/29RaC347tqzgB3z

Simplemente debe bajarse el archivo y descomprimir en una carpeta a elecci贸n.

Esta opcion solo est谩 disponible para Windows 64-bits.
