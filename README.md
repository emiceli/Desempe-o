# Servicio Rest API de Predicción Simulada

Este proyecto proporciona un servicio Rest API que simula el uso de un modelo de predicción utilizando Flask y Docker. El servicio se puede desplegar fácilmente en contenedores Docker.

## Información del Servicio

Este servicio Rest API proporciona una simulación de un modelo de predicción simple. La simulación realizada en este ejemplo es la suma de dos números proporcionados como entrada.

### Endpoints Disponibles

- `GET /`: Muestra una página de bienvenida.
- `POST /predict`: Realiza una predicción (suma de dos números).

## Requerimientos

- Docker
- Docker Compose

## Instalación

Para instalar y ejecutar este proyecto, sigue estos pasos:

1. Clona el repositorio:
    ```sh
    git clone https://github.com/tu-usuario/tu-repositorio.git
    cd tu-repositorio
    ```

2. Construye y ejecuta los contenedores Docker:
    ```sh
    docker-compose up --build
    ```

El servicio estará disponible en `http://localhost:5000`.

## Uso (Producción)

### Ejemplos de Uso de Endpoints

#### Página de Bienvenida

- **Endpoint:** `GET /`
- **Descripción:** Muestra una página de bienvenida.

**Curl Example:**
```sh
curl http://localhost:5000/
