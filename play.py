from gpiozero import DigitalOutputDevice
import time

siren = DigitalOutputDevice(4,active_high=True,initial_value=False)

siren.on()

time.sleep(2)

siren.off()