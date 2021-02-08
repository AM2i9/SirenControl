from gpiozero import DigitalOutputDevice
def yelp(stop):
    #Yelp siren on pin 27
    siren = DigitalOutputDevice(27,active_high=True,initial_value=False)
    siren.on()

    while True:
        if stop():
            break