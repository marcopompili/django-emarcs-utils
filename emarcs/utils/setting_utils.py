__author__ = 'Marco Pompili'

from os.path import join, split, dirname


def django_path(relative_path):
    """
    Set the path to a django installation automatically without fixed paths.
    :param relative_path: The relative path from the django project installation.
    :return: Returns the path in a fixed form
    """
    return join(split(dirname(__file__))[0], relative_path).replace('\\', '/')
