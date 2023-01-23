import warnings
warnings.filterwarnings("ignore")

import tensorflow as tf
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

from classification import classify
from custom_config import InferenceConfig
from mrcnn import model as modellib

import skimage.io
import numpy as np
import sys
import os

# Root directory of the project
ROOT_DIR = os.path.abspath("../")  # Go one folder up

# Import Mask RCNN
sys.path.append(ROOT_DIR)  # To find local version of the library

# Directory to save logs and model checkpoints, if not provided
# through the command line argument --logs
DEFAULT_LOGS_DIR = os.path.join(ROOT_DIR, "logs")

DS_DIR = os.path.join(ROOT_DIR, "datasets/input")

# Path to trained weights
WEIGHTS_PATH = os.path.join(
    ROOT_DIR, "logs/mask_rcnn_object_0040.h5")  # TODO: update this path

# Device to load the neural network on.
# Useful if you're training a model on the same
# machine, in which case use CPU and leave the
# GPU for training.
DEVICE = "/cpu:0"  # /cpu:0 or /gpu:0

config = InferenceConfig()
# config.display() # Shows config stats

# LOAD MODEL
# Create model in inference mode
with tf.device(DEVICE):
    model = modellib.MaskRCNN(mode="inference", model_dir=DEFAULT_LOGS_DIR,
                              config=config)

# Load COCO weights or load the last model you trained
weights_path = WEIGHTS_PATH

# Load weights
print("\nLoading weights", weights_path.split('/')[-1])
model.load_weights(weights_path, by_name=True)

# Get images
images = skimage.io.imread_collection('{}/*.jpg'.format(DS_DIR))
images = np.asarray(images)

# Predict masks
print('\nPredicting masks...')
result = model.detect(images, verbose=0)

# Extract masks out of result
masks = []
[masks.append(object['masks']) for object in result]
print('Done predicting masks.')

# Classify image with predicted mask
print('\nClassifying images...')
classify(images, masks)
print('Done classifying masks.\n')
