# Basurero Organico Inteligente 

## Resumen del proyecto
El proyecto consiste en desarrollar un bote de basura inteligente, como parte de la materia para el Internet de las Cosas (AIoT) que aborda la gestión eficiente de residuos. Equipado con sensores de peso y humedad, y opciones como detección de líquidos y proximidad, el producto será llamado WasteWizard Pro y este ofrece un recordatorio automático cuando el peso de la basura excede un umbral, controla la humedad para prevenir olores desagradables y facilita la deposición sin contacto con su apertura automática. Dirigido a usuarios domésticos y comerciales, busca resolver la necesidad de una gestión de residuos más efectiva y sanitaria, diferenciándose de los botes tradicionales al proporcionar una solución completa e inteligente para la gestión de residuos.

## Integrantes
|Nombre | Apellido Paterno | Apellido Materno |Numero de control|
|-|-|-|-|
|Laura Berenice |Tapia|Cid|1222100476|
|Francisco|Torres|Rojas|1222100743|
|Brayan Gael|García|González|1222100489|

## Carta de liberación del proyecto
- Dirigida al Docente
- Debe de expresar las funcionalidades que tiene el proyecto
- Nombres de los integrantes que participaron en el proyecto
- Es una imagen jpg o png.
- Firmada por el empresario o docente ageno a la UTNG, agradeciendo la contribución de la UTNG.
- Hoja membretada (Logo de la empresa, dirección y contacto)

  Archivo:

## Lista del Hardware utilizado 
| Id | Componente | Descripción | Imagen | Cantidad | Costo total |
|----|------------|-------------|--------|----------|-------------|
| 1 |Sensor de gas|Este sensor detecta y mide la cantidad de gas contenido e un espacion | ![image](https://github.com/Brayan7273/BasueroInteligente/assets/130590443/70d8f618-b0f0-481a-8ec8-b3870e7b89b9) | 1 | $100 |
| 2 |Sensor de humedad y temperatura |Sensor que funciona como medidor de humedad y temperatura| ![image](https://github.com/Brayan7273/BasueroInteligente/assets/130590443/004ea1ae-a7ed-4e8e-a521-b5d8c369e0e8) | 1 | $98 |
| 3 |Sensor seguidor de linea KY-033 | Este módulo sensor seguidor de línea detecta si hay un área que refleja o absorbe la luz delante de él.| ![image](https://github.com/Brayan7273/BasueroInteligente/assets/130590443/51e47549-9234-4caf-b85d-9efc0b6afc55) | 1 | $55 |
| 4 | Sensor de Flama | Es un sensor que permite detectar la flama producida por el fuego u otras fuentes de luz. | ![image](https://github.com/Brayan7273/BasueroInteligente/assets/130590443/24ad4f10-ae22-4caa-af28-6e56416ec3f9) | 1 |$65 |
| 5 | Sensor de Inclinación | Sensor de inclinación que cierra internamente un circuito cuando se inclina hacia un lado, se mueva con suficiente fuerza y ​​cuenta con grado de inclinación para activar el interruptor de bola que se encuentra en su interior. | ![image](https://github.com/Brayan7273/BasueroInteligente/assets/130590443/6f8174fc-511f-4223-96de-4eb5f28d94cc) | 1 | $49 |
| 6 | Sensor de Bloqueo de Luz | El sensor usa un haz de luz entre el emisor y un detector para verificar si el camino entre ambos está siendo bloqueado por un objeto opaco. | ![image](https://github.com/Brayan7273/BasueroInteligente/assets/130590443/f663abd2-1c2a-472c-abd2-1a0377369f24) | 1 | $39
| 7 |Buzzer           |Componente que emite sonido             | ![image](https://github.com/Brayan7273/BasueroInteligente/assets/130590443/01695b09-7f16-46f7-a2ba-62f4f1c6dd85)|   2     |    $49         |
| 8 | Display | El OLED es un tipo de panel. Y uno muy especial: en vez de usar luz de fondo como el LCD, en él cada píxel emite su propia luz. | ![image](https://github.com/Brayan7273/BasueroInteligente/assets/130590443/b069473c-4775-41a4-8476-988db0130e1a) | 2 | $95|
| 9 | Led | Es un dispositivo que permite el paso de corriente en un solo sentido y que al ser polarizado emite un haz de luz. | ![image](https://github.com/Brayan7273/BasueroInteligente/assets/130590443/97675b5a-b680-4792-9944-bc1378977980) | 1 | $2 |

 

## Lista de Software utilizado
| Id | Software | Version | Tipo |
|----|----------|---------|------|
|  1  |  Arduino IDE        |  2.3.2       |  Entorno de desarrollo integrado    |
|  2  |  Thonny        |   3.1.1      | Entorno de desarrollo integrado     |
| 3   | Raspberry  Pi Imager        | Bullseye Debian 11       |  Software de escritorio    |

## Visión del producto
Quién es el público: ¿Quién va a utilizar tu producto?
    Usuarios domésticos y comerciales interesados en una gestión inteligente y eficiente de los residuos.
    
Qué problema tiene: ¿Qué problema o necesidad latente se va a satisfacer?
    La gestión tradicional de residuos puede ser ineficiente y llevar a malos olores, olvidos de  Drecolección y desbordamientos. Existe la necesidad de una solución que automatice y mejore la gestión de los desechos.

Qué solución se ofrece: ¿Cómo se va a satisfacer?
    Ofrecemos un Bote de Basura Inteligente equipado con sensores de peso, humedad y otros opcionales para una gestión más eficiente. Este dispositivo incorpora 
    recordatorios automáticos y sistemas de ventilación para garantizar una experiencia higiénica y sin olores desagradables. Además, la apertura automática de la tapa 
    mejora la comodidad del usuario.

Patrón o forma de escribir o crear visión planeada para el proyecto: 

PARA: Usuarios domésticos y comerciales preocupados por la gestión eficiente y sanitaria de los residuos.
QUIEN: Quienes buscan una solución que simplifique y mejore la gestión de residuos, evitando olores desagradables, recordando eficazmente la 
    recolección y ofreciendo una experiencia sin complicaciones.
    WasteWizard Pro de categoria Bote de Basura Inteligente y Conectado 
QUE: El bote de Basura Inteligente ofrece una gestión de residuos sin esfuerzo y sin preocupaciones, gracias a su capacidad para 
    detectar automáticamente el peso de la basura, recordar la recolección oportuna y controlar la humedad para prevenir malos olores. Los usuarios experimentan una mejora 
    significativa en la higiene y eficiencia en la disposición de residuos.
A DIFERENCIA DE: Botes de basura tradicionales y contenedores inteligentes básicos sin las funciones avanzadas de recordatorio y control de 
    humedad.
NUESTRO PRODUCTO: A diferencia de los botes de basura convencionales y algunos competidores, no solo se limita a contener los 
    residuos. Gracias a su sistema inteligente de sensores y actuadores, ofrece una experiencia completamente nueva al recordar automáticamente la recolección, prevenir 
    malos olores mediante la gestión activa de la humedad, y facilitar el depósito sin contacto directo a través de la apertura automática de la tapa. Esto convierte a 
    SmartBin Pro en la elección ideal para aquellos que buscan una solución completa y avanzada para la gestión de residuos en su hogar o negocio.

## Conexiones
- Imagenes de Wokwi, Fritzing, o de otro software que me permita mostrar las conexiones del circuito.
- Raspberry Pi
- ESP 32

## Funcionalidades

| Id | Historia de usuario | Prioridad | Estimación | Como probarlo | Responsable |
|----|---------------------|-----------|------------|---------------|-------------|
| 1  | Detectar cuando se ingresa basura|  Alta         |  2 Semanas          | Introduciremos basura al Bote  |   Laura         |
| 2  | Detectar cuando existe alguna flama en la basura |Alta           |  2 Semanas        | Encenderemos una llama para comprobar su existencia|  Laura       |
| 3  | Detectar algun gas en la basura | Alta | 2 Semanas | Introduciremos alguna basura que contenga un gas para su detección. | Brayan |
| 4  | Detectar la temperatura y humedad dentro del Bote | Alta |2 Semanas|  Alteraremos la temperatura y humedad para subir y bajar los valores. | Brayan | 
| 5  | Detectar cuando se abre y se cierra el bote de basura |Alta          | 2 Semanas    | Abrir y cerrar el bote para que se detecte los valores de abierto y cerrado | Francisco    |
| 6  | Detectar cuando se cae el Bote de Basura | Alta    | 2 Semanas   | Tirar el bote para que se active el funcionamiento del sensor         | Francisco   |
| 7  | Activar un buzzer | Media |2 Semanas| Al momento de que se cae el bote tiene que activarse el buzzer como alerta de que esta tirado el bote | Todos |
| 8  | Encender y apagar led | Media |2 Semanas | Al momento que se abre el bote el led se enciende y al momento que se cierra se apaga. | Todos |


## Prototipo en dibujo
- Coloca la imagen de tu proyecto al iniciar el desarrollo

# Evidencias de funcionamiento
- Captura de pantalla de flujos de Node RED
![image](https://github.com/Brayan7273/BasueroInteligente/assets/130590443/c648ed9e-08bf-4c63-9d1a-228256a54c8a)
- Captura de las pantallas del proyecto DASHBOARD y Pantalla de la ESP32


