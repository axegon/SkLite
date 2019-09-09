"""The module  is used to convert the sklearn.neighbors.KNeighborsClassifier
into a Flutter/Dart model."""
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from .base import SKLiteBase


class SkliteKNeighborsClassifier(SKLiteBase):
    """KNeighborsClassifier implementation."""

    @property
    def class_(self):
        """Used for checking the data-type of the
        estimator in the constructor."""
        return KNeighborsClassifier

    def build(self) -> dict:
        """Fetches and transforms all the data from the
        classifier.

        Returns
        -------
        dict
        """
        data = {}
        attributes = ["_fit_X", "_y"]
        for attr in attributes:
            data[attr] = getattr(self._estimator, attr).tolist()
        data["classes"] = self._estimator.classes_.astype(np.int32).tolist()
        data["n_neighbors"] = self._estimator.n_neighbors
        data["p"] = self._estimator.p
        return data
