import machine
import time
import dht
import network 
import ssd1306
from umqtt.simple import MQTTClient

# Configurar el sensor DHT11
dht_pin = 4  # Pin GPIO conectado al sensor DHT11
dht_sensor = dht.DHT11(machine.Pin(dht_pin))

# Configurar el sensor MQ-2
mq2_pin_analog = 34  # Pin GPIO conectado al pin de salida analógica del sensor MQ-2 (cambia según tu conexión)
mq2_pin_digital = 35  # Pin GPIO conectado al pin de salida digital del sensor MQ-2 (cambia según tu conexión)
adc = machine.ADC(machine.Pin(mq2_pin_analog))
dout = machine.Pin(mq2_pin_digital, machine.Pin.IN)

# Configurar el buzzer
buzzer_pin = 33  # Pin GPIO conectado al buzzer (cambia según tu conexión)
buzzer = machine.Pin(buzzer_pin, machine.Pin.OUT)
buzzer.off()  # Apagar el buzzer inicialmente

# Configurar el display OLED
i2c = machine.SoftI2C(scl=machine.Pin(22), sda=machine.Pin(21))  # Configura el bus I2C
oled = ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)  # Cambia la dirección del dispositivo si es necesario

# Configurar conexión MQTT
MQTT_BROKER = "broker.hivemq.com"
MQTT_USER = ""
MQTT_PASSWORD = ""
MQTT_TOPIC_DHT11T = "utng/arg/dht11T"
MQTT_TOPIC_DHT11H = "utng/arg/dht11H"
MQTT_TOPIC_MQ2_A = "utng/arg/mq2_analogico"
MQTT_TOPIC_MQ2_D = "utng/arg/mq2_digital"
MQTT_TOPIC_DISPLAY = "utng/arg/display"  # Nuevo tema para el mensaje del display
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
    # Si el mensaje se recibe en el tema para el display, mostrarlo en el OLED
    if topic == MQTT_TOPIC_DISPLAY:
        mensaje = msg.decode("utf-8")  # Decodificar el mensaje de bytes a cadena
        oled.fill(0)  # Borrar el contenido previo del display
        oled.text(mensaje, 0, 0)  # Mostrar el mensaje en el OLED
        oled.show()  # Mostrar los datos en el display
        time.sleep(2)

def main():
    conectar_wifi()
    client = conectar_mqtt()
    client.set_callback(callback)  # Configurar la función de callback
    client.subscribe(MQTT_TOPIC_DISPLAY)  # Suscribirse al tema para el mensaje del display
    while True:
        try:
            # Lectura del sensor DHT11
            dht_sensor.measure()
            temperatura = dht_sensor.temperature()
            humedad = dht_sensor.humidity()

            # Lectura del sensor MQ-2
            valor_analogico = adc.read()
            valor_digital = dout.value()

            # Publicar datos en MQTT si cambian los valores
            client.publish(MQTT_TOPIC_DHT11T, str(temperatura))
            client.publish(MQTT_TOPIC_DHT11H, str(humedad))
            client.publish(MQTT_TOPIC_MQ2_A, str(valor_analogico))
            client.publish(MQTT_TOPIC_MQ2_D, str(valor_digital))

            # Activar el buzzer si la humedad es mayor al 80%
            if humedad > 10:
                buzzer.off()
            else:
                buzzer.on()

            # Mostrar datos en el display OLED
            oled.fill(0)  # Borrar el contenido previo del display
            oled.text("Temp: {}".format(temperatura), 0, 0)
            oled.text("Humedad: {}".format(humedad), 0, 16)
            oled.text("Gas: {}".format(valor_analogico), 0, 32)
            oled.show()  # Mostrar los datos en el display

            client.check_msg()  # Verificar si hay mensajes MQTT recibidos

            time.sleep(2)  # Esperar 2 segundos antes de la próxima lectura
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()

