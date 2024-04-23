from machine import Pin, I2C
import time
import network
from umqtt.simple import MQTTClient
import ssd1306

# Configurar el sensor KY-033 TRACKING
tracking_sensor_pin = Pin(15, Pin.IN)  # Conectado al pin 15 del ESP32

# Configurar el sensor KY-026 FLAME
flame_sensor_digital_pin = Pin(16, Pin.IN)  # Conectado al pin 16 del ESP32

# Configuración de conexión MQTT
MQTT_BROKER = "broker.hivemq.com"
MQTT_USER = ""
MQTT_PASSWORD = ""
MQTT_CLIENT_ID = "ESP32_Client"
MQTT_PORT = 1883
MQTT_TOPIC_TRACKING = "utng/arg/tracking"
MQTT_TOPIC_FLAME = "utng/arg/flame"

# Configuración de conexión WiFi
def conectar_wifi():
    print("Conectando a WiFi...")
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect('Piso.1', 'AR16248107')
    while not sta_if.isconnected():
        pass
    print("Conexión WiFi exitosa")

# Conexión WiFi
conectar_wifi()

# Conexión MQTT
def conectar_mqtt():
    client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT, user=MQTT_USER, password=MQTT_PASSWORD)
    try:
        client.connect()
        print("Conexión MQTT exitosa")
    except OSError as e:
        print("Error de conexión MQTT:", e)
        return None
    return client

# Loop principal
client_mqtt = conectar_mqtt()
prev_flame_value = 0  # Valor previo del sensor de llama
prev_tracking_value = 0  # Valor previo del sensor de seguimiento

# Configuración del display OLED
i2c = I2C(scl=Pin(22), sda=Pin(21))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Configuración del buzzer pasivo
buzzer_pin = Pin(17, Pin.OUT)  # Conectado al pin 17 del ESP32

while True:
    try:
        # Verificar la conexión MQTT
        if client_mqtt is None:
            print("Reconectando MQTT...")
            client_mqtt = conectar_mqtt()
        else:
            # Leer el estado actual del sensor KY-033 TRACKING
            current_tracking_state = tracking_sensor_pin.value()
            if current_tracking_state != prev_tracking_value:
                if current_tracking_state == 1:
                    print("SIN BASURA")
                    client_mqtt.publish(MQTT_TOPIC_TRACKING, "SIN BASURA")
                else:
                    print("BASURA DETECTADA")
                    client_mqtt.publish(MQTT_TOPIC_TRACKING, "BASURA DETECTADA")

            # Leer el estado del sensor KY-026 FLAME
            flame_sensor_value = flame_sensor_digital_pin.value()
            if flame_sensor_value != prev_flame_value:
                if flame_sensor_value == 0:
                    print("FUEGO EN LA BASURA")
                    client_mqtt.publish(MQTT_TOPIC_FLAME, "FUEGO EN LA BASURA")
                    buzzer_pin.on()  # Encender el buzzer
                else:
                    print("SIN FUEGO EN LA BASURA")
                    client_mqtt.publish(MQTT_TOPIC_FLAME, "SIN FUEGO EN LA BASURA")
                    buzzer_pin.off()  # Apagar el buzzer

            prev_flame_value = flame_sensor_value  # Actualizar el valor previo del sensor de llama
            prev_tracking_value = current_tracking_state  # Actualizar el valor previo del sensor de seguimiento

            # Actualizar el display OLED
            oled.fill(0)
            oled.text("Tracking: {}".format("SIN BASURA" if current_tracking_state == 1 else "BASURA DETECTADA"), 0, 0)
            oled.text("Flame: {}".format("SIN FUEGO" if flame_sensor_value == 0 else "FUEGO DETECTADO"), 0, 16)
            oled.show()

    except Exception as e:
        print("Error en el loop principal:", e)

    time.sleep(1)  # Esperar un segundo antes de la próxima lectura
