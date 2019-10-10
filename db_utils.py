import numpy
from os import listdir
from face_detection import *

DATABASE_PATH = "dataset/"


def load_database_image():
    """
    Loads the images from the database
    :return: the images of the database
    """

    images = {}  # images[name] = [image_1, image_2, ...]
    # To complete ------------------

    return images


def create_database(images):
    """
    Compute the preprocessed images to vector representation
    :param images: the image database
    :return: the set array
    """

    data_x = []  # List of normalised faces
    data_y = []  # List of labels
    # To complete ------------------

    return numpy.array(data_x), numpy.array(data_y)


def load_labels():
    """
    Loads the text labels
    :return: the list of labels
    """

    labels = []
    # To complete ------------------

    return labels


def save_database(data_x, data_y):
    """
    Saves the database
    :param data_x: the inputs matrix
    :param data_y: the output matrix
    """

    numpy.save("dx.npy", data_x)
    numpy.save("dy.npy", data_y)


def load_database():
    """
    Loads the database
    :return: the input and output matrix
    """

    data_x = numpy.load("dx.npy")
    data_y = numpy.load("dy.npy")

    return data_x, data_y

