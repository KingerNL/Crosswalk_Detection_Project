import warnings
warnings.filterwarnings("ignore") 

import tensorflow as tf
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

import os
import sys

# Root directory of the project
ROOT_DIR = os.path.abspath("../") # Go one folder up

# Import Mask RCNN
sys.path.append(ROOT_DIR)  # To find local version of the library
from mrcnn import model as modellib
from mrcnn import utils

from custom_data import CustomDataset
from custom_config import CustomConfig

# Path to COCO weights file
COCO_WEIGHTS_PATH = os.path.join(ROOT_DIR, "mask_rcnn_coco.h5")

# Directory to save logs and model checkpoints, if not provided
# through the command line argument --logs
DEFAULT_LOGS_DIR = os.path.join(ROOT_DIR, "logs")

DS_DIR = os.path.join(ROOT_DIR, "datasets")

# Path to trained weights
WEIGHTS_PATH = os.path.join(
    ROOT_DIR, "logs/mask_rcnn_object_0040.h5")  # TODO: update this path

# Device to load the neural network on.
# Useful if you're training a model on the same
# machine, in which case use CPU and leave the
# GPU for training.
DEVICE = "/cpu:0"  # /cpu:0 or /gpu:0


def train(model):
    """Train the model."""
    # Training dataset.
    dataset_train = CustomDataset()
    dataset_train.load_custom(DS_DIR, "train")
    dataset_train.prepare()

    # Validation dataset
    dataset_val = CustomDataset()
    dataset_val.load_custom(DS_DIR, "val")
    dataset_val.prepare()

    # Since we're using a very small dataset, and starting from
    # COCO trained weights, we don't need to train too long. Also,
    # no need to train all layers, just the heads should do it.
    print("Training network heads")
    model.train(dataset_train, dataset_val,
                learning_rate=config.LEARNING_RATE,
                epochs=10,
                layers='heads')


weights_path = WEIGHTS_PATH

# If weight is missing, download COCO weight file
if not os.path.exists(weights_path):
    weights_path = COCO_WEIGHTS_PATH
    utils.download_trained_weights(weights_path)

config = CustomConfig()
config.display()
model = modellib.MaskRCNN(mode="training", config=config,
                          model_dir=DEFAULT_LOGS_DIR)

# Load model with previous trained weights
if(weights_path == WEIGHTS_PATH):
    model.load_weights(weights_path, by_name=True)
# Load COCO weights and remove layers when no weight is found
else:
    model.load_weights(weights_path, by_name=True, exclude=[
        "mrcnn_class_logits", "mrcnn_bbox_fc",
        "mrcnn_bbox", "mrcnn_mask"])

print("Loading weights ", weights_path)

with tf.device(DEVICE):
    train(model)
