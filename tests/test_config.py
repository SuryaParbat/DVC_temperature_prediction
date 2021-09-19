import json
import logging
import os
import joblib
import pytest
from prediction_service.prediction import form_response, api_response
import prediction_service

input_data = {
    "incorrect_range":
    {"Process_temperature_[K]": 7897897,
    "Rotational_speed_[rpm]": 3000,
    "Torque_[Nm]": 99,
    "Tool_wear_[min]": 300,
    "TWF": 2,
    "HDF": 2,
    "PWF": 2,
    "OSF": 2,
    "RNF": 2
    },

    "correct_range":
        {"Process_temperature_[K]": 304,
         "Rotational_speed_[rpm]": 1167,
         "Torque_[Nm]": 2,
         "Tool_wear_[min]": 0,
         "TWF": 0,
         "HDF": 0,
         "PWF": 0,
         "OSF": 0,
         "RNF": 0
         },

    "incorrect_col":
        {"Process temperature [K]": 310,
         "Rotational speed [rpm]": 2000,
         "Torque [Nm]": 60,
         "Tool wear [min]": 200,
         "TwF": 1,
         "hDF": 1,
         "PwF": 1,
         "OSf": 1,
         "RNf": 1
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