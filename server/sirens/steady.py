from gpiozero import DigitalOutputDevice
def steady(stop):
    #steady tone on pin 22
    siren = DigitalOutputDevice(22,active_high=True,initial_value=False)
    siren.on()

    while True:
        if stop():
            break