import requests
from requests import get
from pyfiglet import Figlet
import folium

def ip_info_get(ip):
    try:
        response = get(url=f'http://ip-api.com/json/{ip}').json()

        data = {
            '[IP]': response.get('query'),
            '[Int prov]': response.get('isp'),
            '[Org]': response.get('org'),
            '[Country]': response.get('country'),
            '[Region Name]': response.get('regionName'),
            '[City]': response.get('city'),
            '[ZIP]': response.get('zip'),
            '[Lat]': response.get('lat'),
            '[Lon]': response.get('lon'),
        }

        for k, v in data.items():
            print(f'{k} : {v}')

        sa = input("Save area? (y or n): ")
        if sa == "y":
            area = folium.Map(location=[response.get('lat'), response.get('lon')])
            area.save(f'{response.get("quary")}_{response.get("city")}.html')
        elif sa == "n":
            return "nil"
        else:
            print("[!] Invalid text!")
    except requests.exceptions.ConnectionError:
        print('[!] Please, check your connection!')

def main():
    ip = input("Target public ip: ")
    ip_info_get(ip)

if __name__ == "__main__":
    main()
