import numpy
import cv2
from skimage.feature import hog


def normalize(image, face, affine=True):
    """
    Retrieves the face from the image and normalizes it
    :param image: the image which contains the face
    :param face: the face data
    :param affine: uses the affine transform to align the eyes
    :return: the normalized face
    """

    x, y, width, height = face[0]  # face position

    point_left = numpy.array(face[1])  # left eye
    point_right = numpy.array(face[2])  # right eye

    # To complete ----------------------------------
    normalized = ...

    return normalized


def hog_representation(image, hog_orientations=8, hog_cell_size=(16, 16)):
    """
    Computes the HOG representation of the image
    :param image: the normalized image
    :param hog_orientations: the number of directions
    :param hog_cell_size: the size of cells
    :return: the hog representation
    """

    # To complete ----------------------------------
    hog_vector = ...

    return hog_vector
