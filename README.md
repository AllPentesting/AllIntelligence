# AllIntelligence

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://github.com/AllPentesting/AllIntelligence)


### Descripción
La herramienta AllIntelligence nos permitirá tener una visión general de posibles vectores de ataque de una organización. Como input de entrada le facilitaremos un dominio, del cual obtendremos información desde dos puntos de vista:
1. Nivel técnico: puertos abiertos, servicios expuestos y posibles vulnerabilidades de los mismos. Como por ejemplo servicios de correo vulnerables a suplantación de indentidad, tecnologías web vulnerables (Wordpress, Joomla u otro CMS vulnerable) y otros servicios expuestos.
2. Nivel de Identidad Digital: donde analizaremos posibles fugas de información de correos electrónicos asociados a la organización y redes sociales de estos que puedan dar información útil para un atacante.
Todo ello de cara a analizar la cantidad de información que un atacante podría obtener de nuestra organización a la hora de realizar un APT.

### Descarga
Para descargar este proyecto ejecutamos los siguientes comandos: 

```sh
git clone https://github.com/AllPentesting/AllIntelligence.git
cd AllIntelligence
```
Esto descargará el proyecto actual y nos creará la carpeta **AllIntelligence** con la herramienta.

### Objetivos

Objetivos a conseguir:

| Objetivos | Estado |
| ------ | ------ |
| Interfaz web con Flask |![img](http://i.imgur.com/kR8HJwg.png) |
| API de Shodan |![img](http://i.imgur.com/kR8HJwg.png) |
| API de Hunter.io |![img](http://i.imgur.com/kR8HJwg.png) |
| API de Dehashed |![img](http://i.imgur.com/kR8HJwg.png) |
| API de MaxMind |![img](http://i.imgur.com/kR8HJwg.png) |
| API de Pipl |![img](http://i.imgur.com/kR8HJwg.png) |
| Testing manual |![img](http://i.imgur.com/kR8HJwg.png) |
| Generación de informes |![img](http://i.imgur.com/kR8HJwg.png) |