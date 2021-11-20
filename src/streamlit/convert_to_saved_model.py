from tensorflow.keras.models import load_model
import tensorflow as tf
import numpy as np
import pandas as pd
import os, sys, time

career_rec_model = load_model("model_career_RS.h5")

model_save_path = os.path.join('.', "tf_saved_model/")

if not os.path.exists(model_save_path):
    os.makedirs(model_save_path)

tf.saved_model.save(career_rec_model, model_save_path)