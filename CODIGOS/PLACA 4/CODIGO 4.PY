from machine import Pin
import time
from umqtt.simple import MQTTClient
import network

# Definir los pines
pin_sensor_movimiento = Pin(14, Pin.IN)  # Pin al que está conectado el sensor de movimiento
pin_ledl = Pin(13, Pin.OUT)  # Pin al que está conectado el LED
pin_ledll = Pin(12, Pin.OUT)

# Configurar conexión MQTT
MQTT_BROKER = "broker.hivemq.com"
MQTT_USER = ""
MQTT_PASSWORD = ""
MQTT_TOPIC_MOVIMIENTO = "utng/arg/movimiento"
MQTT_CLIENT_ID = ""
MQTT_PORT = 1883

def conectar_wifi():
    print("Conectando a WiFi...")
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect('Piso.1', 'AR16248107')
    while not sta_if.isconnected():
        print(".", end="")
        time.sleep(0.3)
    print("WiFi Conectada!")

def conectar_mqtt():
    client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, user=MQTT_USER, password=MQTT_PASSWORD, port=MQTT_PORT)
    client.connect()
    print("Conectado a MQTT Broker:", MQTT_BROKER)
    return client

# Función de callback para manejar los mensajes recibidos
def callback(topic, msg):
    topic = topic.decode("utf-8")  # Decodificar el tema a cadena de texto
    print("Mensaje recibido en el tema:", topic)
    print("Contenido del mensaje:", msg)
    # Si el mensaje es "on", encender el LED
    if msg.decode("utf-8") == "on":
        pin_ledll.on()
        print("LED encendido.")
    # Si el mensaje es "off", apagar el LED
    elif msg.decode("utf-8") == "off":
        pin_ledll.off()
        print("LED apagado.")

def main():
    conectar_wifi()
    client = conectar_mqtt()
    client.set_callback(callback)  # Configurar la función de callback
    client.subscribe(MQTT_TOPIC_MOVIMIENTO)  # Suscribirse al tema para los mensajes de movimiento
    while True:
        try:
            client.check_msg()  # Verificar si hay mensajes MQTT recibidos

            # Leer el valor del sensor de movimiento
            movimiento = pin_sensor_movimiento.value()

            # Si se detecta movimiento, encender el LED y publicar el mensaje
            if movimiento == 1:
                pin_ledl.on()
                client.publish(MQTT_TOPIC_MOVIMIENTO, "Movimiento detectado")
                print("¡Movimiento detectado!")
                time.sleep(5)  # Esperar un segundo para evitar múltiples detecciones rápidas
            else:
                client.publish(MQTT_TOPIC_MOVIMIENTO, "No se detecta movimiento")
                print("¡No Movimiento detectado!")
                pin_ledl.off()

            time.sleep(1)  # Esperar un segundo antes de la próxima lectura
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()


