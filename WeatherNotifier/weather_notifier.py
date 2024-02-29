import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def get_weather(location):
    # Hava durumu API'sine istek gönderme
    api_key = "YOUR_API_KEY"  # OpenWeatherMap API anahtarı
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    # Hava durumu bilgilerini işleme
    weather_description = data['weather'][0]['description']
    temperature = data['main']['temp']
    city = data['name']
    
    return f"Hava Durumu: {weather_description}\nSıcaklık: {temperature}°C\nKonum: {city}"

def send_email(sender_email, sender_password, receiver_email, subject, message):
    # E-posta gönderme işlemi
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    body = message
    msg.attach(MIMEText(body, 'plain'))
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()

# Kullanıcı ayarları
sender_email = "YOUR_EMAIL@gmail.com"
sender_password = "YOUR_PASSWORD"
receiver_email = "RECEIVER_EMAIL@gmail.com"
location = "CITY_NAME"

# Hava durumu bilgilerini al
weather_info = get_weather(location)

# E-posta gönder
subject = "Hava Durumu Bildirimi"
send_email(sender_email, sender_password, receiver_email, subject, weather_info)

print("E-posta gönderildi!")
