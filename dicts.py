from pprint import pprint


city_weather = {'city': 'Москва', 'temperature': '20'}
pprint(city_weather['city'])

city_weather['temperature'] = int(city_weather['temperature']) - 5
pprint(city_weather)

print(city_weather.get('Country', 'Россия'))

city_weather['date'] = '27.05.2019'
print(len(city_weather))
