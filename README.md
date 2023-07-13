# ENDPOINT-PROPERTIES

Using python-vanilla was created this project which is an ENDPOINT about SALE OF PROPERTIES.

By Habi (Technical Test)

## Technologies

<div align="center">
	<img width="50" src="https://user-images.githubusercontent.com/25181517/192107854-765620d7-f909-4953-a6da-36e1ef69eea6.png" alt="HTTP" title="HTTP"/>
	<img width="50" src="https://user-images.githubusercontent.com/25181517/183423507-c056a6f9-1ba8-4312-a350-19bcbc5a8697.png" alt="Python" title="Python"/>
	<img width="50" src="https://user-images.githubusercontent.com/25181517/184117132-9e89a93b-65fb-47c3-91e7-7d0f99e7c066.png" alt="pytest" title="pytest"/>
	<img width="50" src="https://user-images.githubusercontent.com/25181517/183896128-ec99105a-ec1a-4d85-b08b-1aa1620b2046.png" alt="MySQL" title="MySQL"/>
</div>

## Description

***SERVICIO DE " ME GUSTA " Y PROPUESTA DE MODELO :***


***JUSTIFICACION DE LA PROPUESTA :***

En base al anterio diagrama propuesto se deberia de eliminar la tabla status y mejor crear un dominio de campo para ahorrar JOINS en las consultas.

Con esta sentencia SQL se podria añadir:
```sql
     CREATE DOMAIN status VARCHAR(10)
     CHECK (VALUE IN ('pre_venta', 'en_venta', 'vendido'));
```

## Installation

Create virtual enviroment:

```bash
    virtualenv habi-env
```

Into the ***habi-env***, install dependecies with pip and pip-tools:

```bash
    pip install pip-tools
    pip-sync requirements.txt
```

Execute the next command:

```bash
    python run.py
```

## Running Tests

To run tests, run the following command

```bash
  pytest -q
```