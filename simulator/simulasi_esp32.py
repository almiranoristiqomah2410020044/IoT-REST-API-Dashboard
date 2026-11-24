
import paho.mqtt.client as mqtt
import json
import time
import random
from datetime import datetime

# Konfigurasi MQTT
BROKER = "localhost"
PORT = 1883
TOPIC_SENSOR = "iot/sensor"

# Membuat koneksi MQTT
client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2,
    client_id="ESP32-Simulator"
)

# Menghubungkan ke Mosquitto
client.connect(BROKER, PORT, 60)
client.loop_start()

print("================================")
print("     ESP32 SIMULATOR AKTIF")
print("================================")
print("Mengirim data sensor setiap 3 detik...")
print("Tekan CTRL + C untuk berhenti.")
print("--------------------------------")

try:
    while True:
        # Simulasi data suhu dan kelembaban
        data = {
            "suhu": round(random.uniform(25, 32), 1),
            "kelembaban": round(random.uniform(55, 80), 1),
            "timestamp": datetime.now().isoformat()
        }

        # Mengirim data ke MQTT
        client.publish(TOPIC_SENSOR, json.dumps(data))

        # Menampilkan data di CMD
        print("Data sensor terkirim:")
        print(json.dumps(data, indent=4))
        print("--------------------------------")

        time.sleep(3)

except KeyboardInterrupt:
    print("\nSimulasi dihentikan.")

finally:
    client.loop_stop()
    client.disconnect()
