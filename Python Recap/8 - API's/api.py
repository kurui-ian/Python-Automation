import requests

def get_weather(latitude, longitude):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m")
    data = response.json()
    return data['current']['temperature_2m']

paris = get_weather(48.85, 2.35)
london = get_weather(51.50, -0.12)
tokyo = get_weather(35.8,139.69)

nairobi = get_weather(-1.286389,36.817223)

print(f"Nairobi: {nairobi}")
print(f"Paris: {paris} °C")
print(f"London: {london} °C")
print(f"Tokyo: {tokyo} °C")