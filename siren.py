import requests

class Siren:

    def __init__(self,ip,port=80):
        self.address = f"http://{ip}:{port}/"

    def yelp(self):
        r = requests.get(f"{self.address}yelp")
    
    def steady(self):
        r = requests.get(f"{self.address}steady")
        
    def off(self):
        r = requests.get(f"{self.address}off")