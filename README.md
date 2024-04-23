# Proyecto de AIoT
Creación de un basurero inteligente 

## Resumen del proyecto
El proyecto consiste en desarrollar un bote de basura inteligente, como parte de la materia para el Internet de las Cosas (AIoT) que aborda la gestión eficiente de residuos. Equipado con sensores de peso y humedad, y opciones como detección de líquidos y proximidad, el producto será llamado WasteWizard Pro y este ofrece un recordatorio automático cuando el peso de la basura excede un umbral, controla la humedad para prevenir olores desagradables y facilita la deposición sin contacto con su apertura automática. Dirigido a usuarios domésticos y comerciales, busca resolver la necesidad de una gestión de residuos más efectiva y sanitaria, diferenciándose de los botes tradicionales al proporcionar una solución completa e inteligente para la gestión de residuos.

## Integrantes
|Nombre | Apellido Paterno | Apellido Materno |Numero de control|
|-|-|-|-|
|Laura Berenice |Tapia|Cid|12221004|
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
| 1 |Sensor de gas|Este sensor detecta y mide la cantidad de gas contenido e un espacion | https://th.bing.com/th/id/R.90650568e90f8388c6424e8eef916f70?rik=v1%2bG4JSRRX%2fmxQ&pid=ImgRaw&r=0   | 1             |$100
| 2 |Sensor de humedad y temperatura |Sensor que funciona como medidor de humedad      | https://www.330ohms.com/cdn/shop/products/photo_IC-20010_DHT11_DigitalTemperatureHumiditySensor_DHT11_01_700x700.png?v=1627344523         |   1          | $98
| 3 | Sensor de proximidad por infrarrojo etección se detecta típicamente por el ángulo del haz de incidente sin tener en cuenta la intensidad de la luz reflejada.
| 3 |Buzzer           |Componente que emite sonido             |  https://www.steren.com.mx/media/catalog/product/cache/bb0cad18a6adb5d17b0efd58f4201a2f/image/16427f1fb/buzzer-de-3-3-khz-de-8-a-15-vcc-con-se-al-de-tono-constante-de-85-db.jpg      |   1       |    $49         |
| 4 | 

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
    La gestión tradicional de residuos puede ser ineficiente y llevar a malos olores, olvidos de  Drecolección y desbordamientos. Existe la necesidad de una solución que 
    automatice y mejore la gestión de los desechos.
   
    Qué solución se ofrece: ¿Cómo se va a satisfacer?
    Ofrecemos un Bote de Basura Inteligente equipado con sensores de peso, humedad y otros opcionales para una gestión más eficiente. Este dispositivo incorpora 
    recordatorios automáticos y sistemas de ventilación para garantizar una experiencia higiénica y sin olores desagradables. Además, la apertura automática de la tapa 
    mejora la comodidad del usuario.

Patrón o forma de escribir o crear visión planeada para el proyecto: 

    PARA <cliente objetivo> : Usuarios domésticos y comerciales preocupados por la gestión eficiente y sanitaria de los residuos.
    QUIEN <declaración de necesidad> : Quienes buscan una solución que simplifique y mejore la gestión de residuos, evitando olores desagradables, recordando eficazmente la 
    recolección y ofreciendo una experiencia sin complicaciones.
    WasteWizard Pro de categoria Bote de Basura Inteligente y Conectado 
    QUE <beneficio clave, razón de peso para comprar o usar> : WasteWizard Pro ofrece una gestión de residuos sin esfuerzo y sin preocupaciones, gracias a su capacidad para 
    detectar automáticamente el peso de la basura, recordar la recolección oportuna y controlar la humedad para prevenir malos olores. Los usuarios experimentan una mejora 
    significativa en la higiene y eficiencia en la disposición de residuos.
    A DIFERENCIA DE <competidor/alternativa> : Botes de basura tradicionales y contenedores inteligentes básicos sin las funciones avanzadas de recordatorio y control de 
    humedad.
    NUESTRO PRODUCTO <declaración diferencial> : A diferencia de los botes de basura convencionales y algunos competidores, WasteWizard Pro no solo se limita a contener los 
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
| 1  | Detectar el peso  dentro del contendeor|  Alta         |  1 Mes          | Introduciremos bolsas denteo del contendror |   Francisco          |
| 2  | Detectar Humedad denteo del contendeor |Alta           |  1 Mes        | Alteraremos la humedad dentro del contendor y debera saltar la alarma  |  Vanesa          |
| 3  | Alerta de sonido                       |Media          |  1 Mes         |Activar un evento que mande la alerta               | Brayan            |
| 4  | Alerta de mensaje                   |Media          |  1 Mes         |Activar un evento que mande la alerta a una plataforma/app               | Brayan            |

## Prototipo en dibujo
- Coloca la imagen de tu proyecto al iniciar el desarrollo

# Evidencias de funcionamiento
- Captura de pantalla de flujos de Node RED
- Captura de las pantallas del proyecto DASHBOARD y Pantalla de la ESP32
- Video demostrativo de las funcionalidades del proyecto
- Código fuente (PROHIBIDO PONER COMPRIMIDOS)


