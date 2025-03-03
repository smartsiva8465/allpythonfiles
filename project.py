import cv2
import numpy as np
import tensorflow as tf
import RPi.GPIO as GPIO
import time

# Set up GPIO for relay control
RELAY_PIN = 18  # GPIO pin connected to the relay module
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN, GPIO.OUT)
GPIO.output(RELAY_PIN, GPIO.LOW)  # Start with the ignition off

# Load the pre-trained YOLO model for helmet detection
model = tf.saved_model.load("path_to_your_yolo_model")  # Replace with your YOLO model path

# Initialize the camera
camera = cv2.VideoCapture(0)  # Use 0 for the default camera

# Function to detect helmet
def detect_helmet(frame):
    # Preprocess the frame for YOLO input
    input_tensor = tf.convert_to_tensor(frame)
    input_tensor = input_tensor[tf.newaxis, ...]

    # Run the model
    detections = model(input_tensor)

    # Check if a helmet is detected
    for detection in detections['detection_classes']:
        if detection == 1:  # Assuming class 1 is "helmet"
            return True
    return False
try:
    while True:
        ret, frame = camera.read()  # Capture frame from the camera
        if not ret:
            print("Failed to capture frame")
            break

        # Detect helmet
        helmet_detected = detect_helmet(frame)

        # Control the vehicle's ignition based on helmet detection
        if helmet_detected:
            print("Helmet detected - Allowing vehicle to move")
            GPIO.output(RELAY_PIN, GPIO.HIGH)  # Enable ignition
        else:
            print("No helmet detected - Stopping vehicle")
            GPIO.output(RELAY_PIN, GPIO.LOW)  # Disable ignition

        # Display the frame (optional)
        cv2.imshow("Helmet Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
            break

        time.sleep(1)  # Delay for stability

finally:
    # Clean up
    camera.release()
    cv2.destroyAllWindows()
    GPIO.cleanup()
