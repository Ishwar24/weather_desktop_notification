# import required libraries 
from requests_html import HTMLSession
from win10toast_click import ToastNotifier 

page_session = HTMLSession()
# create an object to ToastNotifier class 
weather_notificationn = ToastNotifier() 

city_weather = 'pune'
weather_url = f"https://www.google.com/search?q=weather+{city_weather}"

urldata = page_session.get(weather_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'})

# print(urldata.html.find("span.wob_t", first = True).text)
# print(urldata.html.find("div.vk_bk.wob-unit span.wob_t", first = True).text) 
current_temp = urldata.html.find("span.wob_t", first = True).text
temp_unit = urldata.html.find("div.vk_bk.wob-unit span.wob_t", first = True).text
weather_status = urldata.html.find("div.wob_dcp", first = True).text
other_status = urldata.html.find("div.wtsRwe", first = True).text
# print(city_weather, current_temp, temp_unit, weather_status)
# print(other_status)

result = city_weather.upper() + " " + current_temp + " " + temp_unit +"\r\n" + weather_status + "\r\n" + other_status
#print(f"Current result is {result}")
weather_notificationn.show_toast("live Weather update", result, duration = 50)