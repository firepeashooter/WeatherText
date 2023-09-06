import schedule 
import time
import requests
from twilio.rest import Client


def get_weather(latitude, longitude):
    base_url = "https://api.open-meteo.com/v1/forecast?latitude=44.2345&longitude=-76.4987&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"
    response = requests.get(base_url)
    data = response.json()
    return data


def send_text_message(body):
    account_sid = "AC2547aa7af1592265ca4f27130d4a319a"
    auth_token = "6af7f136d3fdbcafa6dbcd9446163369"
    from_phone_number = "+12566676379"
    to_phone_number = "+12262249308"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=body,
        from_=from_phone_number,
        to=to_phone_number
    )
    print("Text Message Sent")

def send_weather_update():
    latitude = 44.2345
    longitude = -76.4987

    weather_data = get_weather(latitude, longitude)
    temperature_celsius = weather_data["hourly"]["temperature_2m"][0]
    relative_humidity = weather_data["hourly"]["relativehumidity_2m"][0]
    wind_speed = weather_data["hourly"]["windspeed_10m"][0]

    weather_info = (
        f"Good Morning!\n"
        f"Current Weather in Kingston:\n"
        f"Temperature: {temperature_celsius:.2f} C\n"
        f"Relative Humidity: {relative_humidity}%\n"
        f"Wind Speed: {wind_speed} m/s"


    )

    send_text_message(weather_info)




def main():
    schedule.every().day.at("08:00").do(send_weather_update)
    while True:
        schedule.run_pending()
        time.sleep(1)


#if __name__ == "__main__":
    #main()

send_weather_update()
