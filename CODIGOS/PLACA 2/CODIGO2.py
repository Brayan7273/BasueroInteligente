from machine import Pin
import time
import network
from umqtt.simple import MQTTClient

# Configuración de pines
led_tracking = Pin(13, Pin.OUT)  # Pin para el LED de seguimiento
led_shock = Pin(14, Pin.OUT)  # Pin para el LED de choqueN
buzzer = Pin(15, Pin.OUT)  # Pin para el buzzer
shock_sensor_pin = Pin(16, Pin.IN)  # Pin para el sensor KY-002 SHOCK
# Configurar el sensor KY-033 TRACKING
tracking_sensor_pin = Pin(17, Pin.IN)  # Conectado al pin 15 del ESP32
# Configurar el sensor KY-026 FLAME
flame_sensor_digital_pin = Pin(18, Pin.IN)  # Conectado al pin 16 del ESP32
flame_sensor_analogico_pin = Pin(34, Pin.IN)

# Configuración de conexión MQTT
MQTT_BROKER = "broker.hivemq.com"
MQTT_USER = ""
MQTT_PASSWORD = ""
MQTT_CLIENT_ID = "ESP32_Client"
MQTT_PORT = 1883
MQTT_TOPIC_TRACKING = "utng/arg/tracking"
MQTT_TOPIC_FLAME = "utng/arg/flame"
MQTT_TOPIC_SHOCK = "utng/arg/shock"

# Configurar conexión WiFi
def conectar_wifi():
    print("Conectando a WiFi...")
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect('Piso.1', 'AR16248107')
    while not sta_if.isconnected():
        pass
    print("Conexión WiFi exitosa")

conectar_wifi()

def conectar_mqtt():
    client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT, user=MQTT_USER, password=MQTT_PASSWORD)
    try:
        client.connect()
        print("Conexión MQTT exitosa")
    except OSError as e:
        print("Error de conexión MQTT:", e)
        return None
    return client

client_mqtt = conectar_mqtt()  # Definir client_mqtt antes del loop principal

# Loop principal
prev_flame_value = 0  # Valor previo del sensor de llama
prev_tracking_value = 0  # Valor previo del sensor de seguimiento
prev_shock_value = 0  # Valor previo del sensor de choque

flame_start_time = 0  # Tiempo de inicio de detección de fuego
shock_start_time = 0  # Tiempo de inicio de detección de choque

BUZZER_DURATION = 2  # Duración del sonido del buzzer en segundos

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
                    led_tracking.off()  # Apagar LED de seguimiento
                else:
                    print("BASURA DETECTADA")
                    client_mqtt.publish(MQTT_TOPIC_TRACKING, "BASURA DETECTADA")
                    led_tracking.on()  # Encender LED de seguimiento

            # Leer el estado del sensor KY-026 FLAME
            flame_sensor_value = flame_sensor_digital_pin.value()
            if flame_sensor_value != prev_flame_value:
                if flame_sensor_value == 1:
                    print("FUEGO EN LA BASURA")
                    client_mqtt.publish(MQTT_TOPIC_FLAME, "FUEGO EN LA BASURA")
                    buzzer.on()  # Activar el buzzer
                    flame_start_time = time.time()  # Iniciar tiempo de detección de fuego
                else:
                    print("SIN FUEGO EN LA BASURA")
                    client_mqtt.publish(MQTT_TOPIC_FLAME, "SIN FUEGO EN LA BASURA")
                    buzzer.off()  # Apagar el buzzer

            # Leer el estado del sensor KY-002 SHOCK
            shock_sensor_value = shock_sensor_pin.value()
            if shock_sensor_value != prev_shock_value:
                if shock_sensor_value == 1:  # El sensor de choque está activado
                    print("CHOQUE DETECTADO")
                    client_mqtt.publish(MQTT_TOPIC_SHOCK, "CHOQUE DETECTADO")
                    led_shock.on()  # Encender LED de choque
                    shock_start_time = time.time()  # Iniciar tiempo de detección de choque
                else:
                    led_shock.off()  # Apagar LED de choque

            # Verificar el tiempo de detección de fuego
            if flame_sensor_value == 0 and time.time() - flame_start_time > BUZZER_DURATION:
                buzzer.off()  # Apagar el buzzer

            # Verificar el tiempo de detección de choque
            if time.time() - shock_start_time > 1:  # Ajustar el tiempo de respuesta del LED al choque
                led_shock.off()  # Apagar LED de choque

            prev_flame_value = flame_sensor_value  # Actualizar el valor previo del sensor de llama
            prev_tracking_value = current_tracking_state  # Actualizar el valor previo del sensor de seguimiento
            prev_shock_value = shock_sensor_value  # Actualizar el valor previo del sensor de choque
    except Exception as e:
        print("Error en el loop principal:", e)
