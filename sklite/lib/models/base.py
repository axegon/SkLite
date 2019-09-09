"""The module defines the basic functionality of all the methods
which need to be implemented for each scikit-learn model.

Each model should extend the SKLiteBase class defined
in this module and the following methods must be implemented:

build, evaluade."""
import sys
import datetime
import getpass
import sklearn
import numpy as np
from ..abstract import Abstract
from ..exceptions import ImplementationException, ClassMismatchException, \
    ClassNotFitted


class SKLiteBase(Abstract):
    """Converts a classifier to a json file for sklite
    into a dart model.
    """
    _estimator = None

    def __init__(self, estimator):
        if not isinstance(estimator, self.class_):
            cname = estimator.__class__.__name__
            err = f"""Expecting {self.class_}, got {cname}"""
            raise ClassMismatchException(err)
        if not isinstance(getattr(estimator,
                                  self.validate_, False), np.ndarray):
            raise ClassNotFitted("The class has not been fitted yet")
        self._estimator = estimator

    @property
    def class_(self):
        """This must be implemented in the child class
        in order to be able to determine the model type."""
        err = "The property should be implemented in the child class"
        raise ImplementationException(err)

    @property
    def validate_(self) -> str:
        """In order to check whether the classifier has been fitted.
        Override if needed but should be suitable for most cases."""
        return "classes_"

    @property
    def _msg(self) -> None:
        """Called from all methods which should be overridden
        in the child class.

        Raises
        ------
        sklite.lib.exception.ImplementationException
        """
        cname = self.__class__.__name__
        message = f"Method has not bee implemented in {cname}"
        raise ImplementationException(message)

    @property
    def _meta(self) -> dict:
        """Generates metadata for the chosen model."""
        return {"__meta__": {
            "__pyversion": sys.version,
            "__sklearn_version": sklearn.__version__,
            "__classifier": self._estimator.__class__.__name__,
            "__author": getpass.getuser(),
            "__dt": datetime.datetime.utcnow().isoformat()
        }}

    def build(self) -> None:
        """The method that takes care of the building of the dart code.
        The method should take all the estimator's properties and
        store them accordingly for the dart template."

        Raises
        -------
        sklite.lib.exception.ImplementationException
        """
        self._msg()
