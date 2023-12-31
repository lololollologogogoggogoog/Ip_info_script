import time
import requests
import folium


def get_info_by_ip(ip='127.0.0.1 '):
    start_time = time.time()
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()

        data = {
            '[IP]': response.get('query'),
            '[prov]': response.get('isp'),
            '[org]': response.get('org'),
            '[country]': response.get('country'),
            '[region]': response.get('regionName'),
            '[city]': response.get('city'),
            '[timezone]': response.get('timezone'),
            '[zip]': response.get('zip'),
            '[lat]': response.get('lat'),
            '[lon]': response.get('lon'),
        }

        for key, values in data.items():
            print(f'{key}:{values}')
        print("--- %s seconds ---" % (time.time() - start_time))

        area = folium.Map(location= [response.get('lat'), response.get('lon')])
        area.save(f'{response.get("query")}_{response.get("city")}.html')


    except requests.exceptions.ConnectionError:
        print('Ошибка')
        print("--- %s seconds ---" % (time.time() - start_time))


def main():

    ip = input('IP:')
    get_info_by_ip(ip=ip)


if __name__ == '__main__':
    main()

