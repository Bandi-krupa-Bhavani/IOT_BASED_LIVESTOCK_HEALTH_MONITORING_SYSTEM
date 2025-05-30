# IOT_BASED_LIVESTOCK_HEALTH_MONITORING_SYSTEM
An innovative IoT-based solution to monitor the health and environmental conditions of livestock in real time. This system helps farmers and livestock managers make data-driven decisions to ensure the well-being of animals, prevent disease outbreaks, and improve productivity.
## 🐄 Project Overview
This project integrates sensors and microcontrollers with AWS IoT Core to remotely monitor key health parameters of livestock. The system continuously collects data like body temperature, heart rate, ambient temperature, and humidity, and sends it to the cloud for storage, analysis, and visualization.
## 🔧 Features
- Real-time health monitoring of livestock
  
- Integration with AWS IoT Core via MQTT
  
- Alerts and notifications for abnormal health readings
  
- Environmental monitoring (temperature, humidity, etc.)
  
- Mobile/web dashboard for live data visualization
  
- Scalable and farmer-friendly solution
## 🧰 Technologies Used

- **Hardware**
  - ESP32 / Arduino UNO
  
  - MAX30102 (Heart Rate and SpO2 Sensor)
    
  - MLX90614 (Body Temperature Sensor)

  - ADXL345 (Accelerator sensor)
    
  - Buzzer / LED (for local alerts)
- **Software & Cloud**
  - Arduino IDE
    
  - AWS IoT Core (MQTT Broker)
    
  - AWS Lambda (optional for data processing)
    
  - AWS DynamoDB / S3 (data storage)
## 📦 Project Structure
iot-based-livestock-health-monitoring-system/
│
├── hardware/                  # Sensor connections, circuit diagrams
├── firmware/                  # Arduino/ESP32 code
├── aws-iot/                   # AWS IoT Core setup, policies, certificates
├── dashboard/                 # Web/mobile dashboard code
├── docs/                      # Reports, presentations, project proposal
└── README.md                  # Project documentation
# 🔌 Hardware Setup
- Connect the sensors (MAX30102, MLX90614) to the ESP32.

- Upload the firmware code via Arduino IDE.

- Ensure the device connects to Wi-Fi and publishes sensor data to AWS IoT via MQTT.
# ☁️ AWS IoT Setup
- Register a new "Thing" in AWS IoT Core.

- Attach a policy to allow publish/subscribe to the relevant MQTT topic.

- Configure certificates and keys.

- Subscribe to MQTT topics to monitor real-time data.

- Use AWS Lambda or DynamoDB to process and store data.

# 📊 Dashboard
- Use Node-RED or any web/mobile frontend to:

- Subscribe to the AWS IoT topic

- Visualize temperature, humidity, heart rate, etc.

- Show alert indicators for abnormal readings
