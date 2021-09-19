import json
import logging
import os
import joblib
import pytest
from prediction_service.prediction import form_response, api_response
import prediction_service

input_data = {
    "incorrect_range":
    {"Process_temperature_[K]": 40000,
    "Rotational_speed_[rpm]": 30000,
    "Torque_[Nm]": 170,
    "Tool_wear_[min]": 300,
    "TWF": 1,
    "HDF": 1,
    "PWF": 0,
    "OSF": 0,
    "RNF": 0
    },

    "correct_range":
        {"Process_temperature_[K]": 308,
         "Rotational_speed_[rpm]": 1169,
         "Torque_[Nm]": 20,
         "Tool_wear_[min]": 10,
         "TWF": 0,
         "HDF": 0,
         "PWF": 1,
         "OSF": 0,
         "RNF": 0
         },

    "incorrect_col":
        {"Process temperature [K]": 310,
         "Rotational speed [rpm]": 2000,
         "Torque [Nm]": 60,
         "Tool wear [min]": 200,
         "TwF": 0,
         "hDF": 1,
         "PwF": 0,
         "OSf": 0,
         "RNf": 0
         },
}

TARGET_range = {
    "min": 304,
    "max": 395
}

def test_form_response_correct_range(data=input_data["correct_range"]):
    res = form_response(data)
    assert  TARGET_range["min"] <= res <= TARGET_range["max"]

def test_api_response_correct_range(data=input_data["correct_range"]):
    res = api_response(data)
    assert  TARGET_range["min"] <= res["response"] <= TARGET_range["max"]

def test_form_response_incorrect_range(data=input_data["incorrect_range"]):
    with pytest.raises(prediction_service.prediction.NotInRange):
        res = form_response(data)

def test_api_response_incorrect_range(data=input_data["incorrect_range"]):
    res = api_response(data)
    assert res["response"] == prediction_service.prediction.NotInRange().message

def test_api_response_incorrect_col(data=input_data["incorrect_col"]):
    res = api_response(data)
    assert res["response"] == prediction_service.prediction.NotInCols().message