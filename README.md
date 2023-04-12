# Ecommerce Cosmetika

Ecommerce Cosmetika es una aplicación web de comercio electrónico simple construida con Django. El proyecto incluye funcionalidades como registro de usuarios, inicio de sesión, gestión de productos y carrito de compras.

## Requisitos previos

- Docker: Instalado y en ejecución.

## Instrucciones de instalación

1. Clona este repositorio en tu máquina local:

```sh
git clone https://github.com/MrQwert/Warehouse-management-system.git
cd Warehouse-management-system
```


2. Construye la imagen de Docker:

```sh
docker build -t pgpi .
```


3. Ejecuta un contenedor Docker basado en la imagen que acabas de construir:

```sh
docker run -p 8000:8000 pgpi
```

4. Abre tu navegador web y visita `http://127.0.0.1:8000` para acceder a la aplicación.

## Estructura del proyecto

- `ecommerce_cosmetika`: Directorio principal del proyecto Django.
- `products`: Aplicación Django para la gestión de productos.
- `accounts`: Aplicación Django para la gestión de usuarios y autenticación.
- `cart`: Aplicación Django para la gestión del carrito de compras.
- `Dockerfile`: Archivo de configuración de Docker para construir y ejecutar la aplicación en un contenedor.
- `manage.py`: Script de Django para administrar el proyecto.


