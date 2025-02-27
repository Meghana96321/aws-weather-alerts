# aws-weather-alerts
A serverless AWS project that fetches real-time weather data using OpenWeatherMap API and sends alerts via AWS SNS.

## 🚀 Features
✅ Fetches real-time weather updates  
✅ Sends SMS/Email alerts via AWS SNS  
✅ **Serverless** and cost-effective using AWS Lambda  
✅ Scheduled execution using CloudWatch  

## 🛠 Tech Stack & AWS Services Used
- **AWS Lambda** (Executes Python script)
- **Amazon SNS** (Sends notifications)
- **Amazon CloudWatch** (Triggers Lambda)
- **OpenWeatherMap API** (Weather data provider)

## 📌 How to Run This Project
1. **Get an OpenWeatherMap API Key** from (https://home.openweathermap.org/api_keys).
2. **Set Up AWS SNS**: Create an SNS topic and subscribe your email/phone.
3. **Deploy the Lambda Function** in AWS Lambda.
4. **Configure CloudWatch Events** to trigger Lambda at scheduled intervals.
5. Check SNS messages for weather alerts! 🌦📩

## 📜 Future Enhancements
- Store weather data in **DynamoDB**  

🚀 Built with **AWS Cloud & Python**  
💻 **Created by [Meghana N]**
