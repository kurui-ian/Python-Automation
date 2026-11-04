import requests
import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime, timedelta

today = datetime.now()


week_ago = today - timedelta(days=7)

start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

def get_weather(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"
    response = requests.get(url)
    data = response.json()
        







    # Extract the daily data
    daily_data = data['daily']

    # Create a DataFrame
    df = pd.DataFrame({
        'date': daily_data['time'],
        'max_temp': daily_data['temperature_2m_max'],
        'min_temp': daily_data['temperature_2m_min']
    })

    # Convert date strings to datetime
    df['date'] = pd.to_datetime(df['date'])

    print(df)




    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(df['date'], df['max_temp'], marker='o', label='Max Temp')
    plt.plot(df['date'], df['min_temp'], marker='o', label='Min Temp')

    # Add labels and title
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title('Nairobi Weather - Past 7 Days')
    plt.legend()

    # Rotate x-axis labels for readability
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the plot
    plt.savefig('weather_chart.png')
    plt.show()


    # Create data folder if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')

    # Save to CSV
    df.to_csv('data/paris_weather.csv', index=False)
    print("Data saved to data/Nairobi_weather.csv")
    return data

#nairobi = -1.2864 Latitude  36.8172 Longitude

get_weather(-1.2864, 36.8172)