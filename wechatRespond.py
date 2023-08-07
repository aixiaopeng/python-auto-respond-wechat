import urllib

import requests


def get_response(msg):
    url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg={}'.format(urllib.parse.quote(msg))
    html = requests.get(url)
    return html.json()["content"]




def isJson(resp):
    try:
        resp.json()
        return True
    except:
        return False

#获取天气信息
def get_weather_info(city_code):
    weather_url = f'http://t.weather.sojson.com/api/weather/city/{city_code}'
    resp = requests.get(url=weather_url)
    if resp.status_code == 200 and isJson(resp) and resp.json().get('status') == 200:
        weatherJson = resp.json()
        # 今日天气
        today_weather = weatherJson.get('data').get('forecast')[1]
        # 温度
        high = today_weather.get('high')
        high_c = high[high.find(' ') + 1:]
        low = today_weather.get('low')
        low_c = low[low.find(' ') + 1:]
        temperature = f"温度 : {low_c}/{high_c}"
        # 空气指数
        aqi = today_weather.get('aqi')
        aqi = f"空气质量 : {aqi}"
        # 天气
        tianqi = today_weather.get('type')
        tianqi = f"天气 : {tianqi}"

        today_msg = f'{tianqi}\n{temperature}\n{aqi}\n'
        return today_msg



while (1) :
    msg = input()
    res = get_response(msg)

    if "天气" in msg:
        today_msg=get_weather_info(101010100)
        print("天气："+today_msg)
    else:
        print(res)



