import csv

from faker import Faker

fake = Faker()


def genrate_weather_csv():
    with open("weather.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Place", "Lat_long", "temperature", "Humidity)"])
        for _ in range(100000):
            w.writerow(
                [
                    fake.city(),
                    f"{fake.latitude()},{fake.longitude()}",
                    fake.random_int(min=-10, max=45),  # -- TMP
                    fake.random_int(min=10, max=100),  # -- HUMIDITY
                ]
            )
    print("weather.csv genraterd")


weather_data = {}
