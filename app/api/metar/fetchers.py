import requests

def vatsim(icao):
    r = requests.get(f'http://metar.vatsim.net/metar.php?id={icao}')
    return r.content
