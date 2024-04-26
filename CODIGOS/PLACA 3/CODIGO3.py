import network
from umqtt.simple import MQTTClient
from machine import Pin
import time  # Agrega esta línea para importar el módulo time

# Configuración de conexión MQTT
MQTT_BROKER = "broker.hivemq.com"
MQTT_USER = ""
MQTT_PASSWORD = ""
MQTT_CLIENT_ID = ""
MQTT_TOPIC_LIGHT = "utng/arg/light"
MQTT_TOPIC_BILL = "utng/arg/bill"
MQTT_TOPIC_MAGNETIC = "utng/arg/magnetic"
MQTT_PORT = 1883

# Configurar conexión WiFi
def conectar_wifi():
    print("Conectando a WiFi...")
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect('Piso.1', 'AR16248107')
    while not sta_if.isconnected():
        print(".", end="")
        time.sleep(0.3)
    print("WiFi Conectada!")

# Función para conectar al broker MQTT
def conectar_mqtt():
    client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, user=MQTT_USER, password=MQTT_PASSWORD, port=MQTT_PORT)
    client.connect()
    print("Conectado a MQTT Broker:", MQTT_BROKER)
    return client

conectar_wifi()
client = conectar_mqtt()

# Configuración de pines
Pin_Sensor_Motion = 14
Pin_Sensor_Light = 12
Pin_Sensor_Magnetic = 15
Pin_Buzzer = 16
Pin_Light_LED = 17

# Configurar pines de sensores y actuadores
sensor_movimiento = Pin(Pin_Sensor_Motion, Pin.IN)
sensor_luz = Pin(Pin_Sensor_Light, Pin.IN)
sensor_magnetic = Pin(Pin_Sensor_Magnetic, Pin.IN)
buzzer = Pin(Pin_Buzzer, Pin.OUT)
light_led = Pin(Pin_Light_LED, Pin.OUT)

# Variables para controlar el estado de los sensores
sensor_motion_activated = False
sensor_light_activated = False
sensor_magnetic_activated = False

# Variables para controlar el estado de los sensores
sensor_movimiento_activado = False
sensor_luz_activado = False

# Parámetros
THRESHOLD = 100

def verificar_movimiento(client):
    global sensor_movimiento_activado  # Indica que estamos utilizando la variable global sensor_movimiento_activado
    
    magnetismo = sensor_movimiento.value() # Lee el valor del sensor de movimiento

    if magnetismo == 0 and not sensor_movimiento_activado:
        sensor_movimiento_activado = True
        return True
    elif magnetismo == 1 and sensor_movimiento_activado:
        sensor_movimiento_activado = False
        return True
    return False

def verificar_sensor_luz(client):
    global sensor_luz_activado  # Indica que estamos utilizando la variable global sensor_luz_activado
    
    valor_actual = sensor_luz.value()
    
    if valor_actual == 0 and not sensor_luz_activado:
        sensor_luz_activado = True
        return True
    elif valor_actual == 1 and sensor_luz_activado:
        sensor_luz_activado = False
        return True
    return False

# Función para verificar el sensor magnético
def verificar_sensor_magnetic(client):
    global sensor_magnetic_activated
    
    magnetic_value = sensor_magnetic.value()
    
    if magnetic_value == 0 and not sensor_magnetic_activated:
        sensor_magnetic_activated = True
        return True
    elif magnetic_value == 1 and sensor_magnetic_activated:
        sensor_magnetic_activated = False
        return True
    return False

# Función principal
def main():
    conectar_wifi()
    client = conectar_mqtt()

    while True:
        if verificar_movimiento(client):
            if sensor_movimiento_activado:
                buzzer.on()  # Enciende el zumbador cuando el sensor de movimiento está activado
                client.publish(MQTT_TOPIC_BILL, "Esta caido")
                print("EL SESTO ESTÁ CAÍDO")
            else:
                buzzer.off()  # Apaga el zumbador cuando el sensor de movimiento está desactivado
                client.publish(MQTT_TOPIC_BILL, "Estable")
                print("EL SESTO ESTÁ ESTABLE")

        if verificar_sensor_luz(client):
            if sensor_luz_activado:
                client.publish(MQTT_TOPIC_LIGHT, "Abierto")
                print("Abierto")
                light_led.on()  # Encender el LED indicador de luz cuando el sensor de luz está activado
            else:
                client.publish(MQTT_TOPIC_LIGHT, "Cerrado")
                print("Cerrado")
                light_led.off() 

        if verificar_sensor_magnetic(client):
            if sensor_magnetic_activated:
                client.publish(MQTT_TOPIC_MAGNETIC, "Objeto magnético detectado")
                print("Objeto magnético detectado")
            else:
                client.publish(MQTT_TOPIC_MAGNETIC, "No se detecta objeto magnético")
                print("No se detecta objeto magnético")

        time.sleep(1)

if __name__ == "__main__":
    main()



