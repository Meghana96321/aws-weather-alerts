import json
import requests
import boto3

# Replace with your OpenWeather API key
API_KEY = "e4d2d41bbdcd6df82ea68537aae85c66"
CITY = "Bangalore"
SNS_TOPIC_ARN = "arn:aws:sns:eu-north-1:253490767150:WeatherAlerts"

# Initialize SNS client
sns = boto3.client('sns')

def get_weather():
    """Fetches weather data from OpenWeather API"""
    url = f"https://api.openweathermap.org/data/2.5/weather?q={Bangalore}&appid={e4d2d41bbdcd6df82ea68537aae85c66}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        temp = data['main']['temp']
        weather_desc = data['weather'][0]['description']
        return f"Weather Alert: {CITY} is currently {temp}°C with {weather_desc}."
    else:
        return "Failed to fetch weather data."

def lambda_handler(event, context):
    """AWS Lambda function to send weather updates via SNS"""
    message = get_weather()
    
    # Publish message to SNS
    response = sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Message=message,
        Subject="Daily Weather Update"
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps("Weather notification sent successfully!")
    }
