import os
import sys

# Root directory of the project
ROOT_DIR = os.path.abspath("../") # Go one folder up

# Import Mask RCNN
sys.path.append(ROOT_DIR)  # To find local version of the library
from mrcnn.config import Config


class CustomConfig(Config):
    """
    Configuration for training on dataset.
    Derives from the base Config class and overrides some values.
    """
    # Give the configuration a recognizable name
    NAME = "roadmark"

    # Number of classification classes
    NUM_CLASSES = 2  # Background + roadmark


config = CustomConfig()


class InferenceConfig(config.__class__):
    """
    Configuration for predicting on dataset.
    Derives from the base Config and CustomConfig class and overrides some values.
    """
    # Run detection on one image at a time
    GPU_COUNT = 1
    IMAGES_PER_GPU = 4
    DETECTION_MIN_CONFIDENCE = 0.9
