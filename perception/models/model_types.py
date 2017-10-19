"""
Available CNN model types.
Author: Jeff Mahler
"""

from autolab_core.utils import reverse_dictionary
from perception.models import ClassificationCNN, FinetunedClassificationCNN, AlexNet, ResNet50, VGG16

CLASSIFICATION_CNN_TYPES = {
    'alexnet': AlexNet,
    'finetuned': FinetunedClassificationCNN,
    'resnet50': ResNet50,
    'vgg16': VGG16
}
CLASSIFICATION_CNN_TYPENAMES = reverse_dictionary(CLASSIFICATION_CNN_TYPES)