import cv2
import os
import json
import ssl
import socketio
import sys
import requests
from joblib import load
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from extractors import (color_features,
                        contrast_features,
                        cloudy_contrast_features,
                        brightness_features,
                        colorfulness_features,
                        horiz_var_features,
                        foggy_fourier_features,
                        snowy_fourier_features,
                        hog_features)

def extract_features(image, *extractor_arr):
  features = list(map(lambda e: e(image), extractor_arr))
  return np.hstack(features)

def make_prediction(model, scaler, features):
  rescaled_feature = scaler.transform(features.reshape(1, -1))
  return model.predict(rescaled_feature)[0]

def main():
  with open('./droneconfig.json') as config_json:
    data = json.load(config_json)
    id = data['drone1']['id']

  previous_condition = json.dumps("")

  sio = socketio.Client()
  sio.connect('http://localhost:4202')

  size = tuple((500, 500))

  cloudy_model    = load('./Cloudy.joblib')
  cloudy_scaler   = load('./Cloudy_scaler.joblib')

  sunny_model     = load('./Sunny.joblib')
  sunny_scaler    = load('./Sunny_scaler.joblib')
  
  rainy_model     = load('./rainy-svm-model.joblib')
  rainy_scaler    = load('./rainy-scaler.joblib')

  snowy_model     = load('./snowy-lr-model.joblib')
  snowy_scaler    = load('./snowy-scaler.joblib')

  foggy_model     = load('./foggy-svm-model.joblib')
  foggy_scaler    = load('./foggy-scaler.joblib')

  daylight_model  = load('./daylight-classifier.joblib')
  daylight_scaler = load('./daylight-scaler.joblib')

  cap = cv2.VideoCapture('../demo-videos/weathertest.mp4')
  os.popen("vlc ../demo-videos/weathertest.mp4")

  while(True):
    ret, frame = cap.read()
    image = cv2.resize(frame, size)

    cloudy_features   = extract_features(image, color_features, cloudy_contrast_features)
    sunny_features    = extract_features(image, color_features, colorfulness_features)
    rainy_features    = extract_features(image, color_features)
    snowy_features    = extract_features(image, snowy_fourier_features, hog_features, horiz_var_features)
    foggy_features    = extract_features(image, color_features, foggy_fourier_features)
    daylight_features = extract_features(image, color_features, contrast_features, brightness_features)

    weather_conditions = {
      "id":         id,
      "data": {
        "cloudy":   np.int(make_prediction(cloudy_model, cloudy_scaler, cloudy_features)),
        "sunny" :   np.int(make_prediction(sunny_model, sunny_scaler, sunny_features)),
        "rainy" :   np.int(make_prediction(rainy_model, rainy_scaler, rainy_features)),
        "snowy" :   np.int(make_prediction(snowy_model, snowy_scaler, snowy_features)),
        "foggy" :   np.int(make_prediction(foggy_model, foggy_scaler, foggy_features)),
        "dark"  :   np.int(make_prediction(daylight_model, daylight_scaler, daylight_features))
      }
    }

    json_weather_conditions = json.dumps(weather_conditions)
    if not json_weather_conditions == previous_condition:
      print(f'sent data from {id}: {json_weather_conditions}')
      previous_condition = json_weather_conditions
      sio.emit('jetsonConnection', json_weather_conditions)
    else:
      print(f'redundant data: {json_weather_conditions}')

if __name__ == "__main__":
    main()
