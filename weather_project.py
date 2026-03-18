# weather_project.py

import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


API_KEY = "7633823862e1a360f32c2f7a86704d3d"

import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


API_KEY = "7633823862e1a360f32c2f7a86704d3d"

#  Cities 
cities = ["Mumbai", "Delhi", "London", "New York", "Tokyo"]

# Step 3: API through data fetch 
weather_data = []

for city in cities:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    data = response.json()

    city_weather = {
        "City": city,
        "Temperature": data["main"]["temp"],
        "Humidity": data["main"]["humidity"],
        "Wind Speed": data["wind"]["speed"]
    }

    weather_data.append(city_weather)

#  Data convert into DataFrame 
df = pd.DataFrame(weather_data)

print("Weather Data:")
print(df)

#  Graph 
sns.set(style="whitegrid")

fig, axes = plt.subplots(1, 3, figsize=(18,5))

# Temperature Graph
sns.barplot(x="City", y="Temperature", data=df, ax=axes[0], palette="coolwarm")
axes[0].set_title("Temperature (°C) by City")

# Humidity Graph
sns.barplot(x="City", y="Humidity", data=df, ax=axes[1], palette="Blues")
axes[1].set_title("Humidity (%) by City")

# Wind Speed Graph
sns.barplot(x="City", y="Wind Speed", data=df, ax=axes[2], palette="Greens")
axes[2].set_title("Wind Speed (m/s) by City")

plt.tight_layout()
plt.show()

# Step 2: Cities की list
cities = ["Mumbai", "Delhi", "London", "New York", "Tokyo"]


weather_data = []

for city in cities:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    data = response.json()

    city_weather = {
        "City": city,
        "Temperature": data["main"]["temp"],
        "Humidity": data["main"]["humidity"],
        "Wind Speed": data["wind"]["speed"]
    }

    weather_data.append(city_weather)


df = pd.DataFrame(weather_data)

print("Weather Data:")
print(df)


sns.set(style="whitegrid")

fig, axes = plt.subplots(1, 3, figsize=(18,5))


sns.barplot(x="City", y="Temperature", data=df, ax=axes[0], palette="coolwarm")
axes[0].set_title("Temperature (°C) by City")

# Humidity Graph
sns.barplot(x="City", y="Humidity", data=df, ax=axes[1], palette="Blues")
axes[1].set_title("Humidity (%) by City")

# Wind Speed Graph
sns.barplot(x="City", y="Wind Speed", data=df, ax=axes[2], palette="Greens")
axes[2].set_title("Wind Speed (m/s) by City")

plt.tight_layout()
plt.show()