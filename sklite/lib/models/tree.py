"""The module  is used to convert the sklearn.tree.DecisionTreeClassifier
into a Flutter/Dart model."""
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from .base import SKLiteBase


class SkliteDecisionTreeClassifier(SKLiteBase):
    """DecisionTreeClassifier implementation."""

    @property
    def class_(self):
        """Used for checking the datatype of the estimator
        in the constructor."""
        return DecisionTreeClassifier

    def build(self) -> dict:
        """Fetches and transforms all the data from the
        classifier.

        Returns
        -------
        dict
        """
        data = {}
        attributes = ["children_left", "children_right",
                      "threshold", "feature"]
        for attr in attributes:
            data[attr] = getattr(self._estimator.tree_, attr).tolist()
        value = self._estimator.tree_.value
        shape = self._estimator.tree_.value.shape
        data["classes"] = self._estimator.classes_.astype(np.int32).tolist()
        data["value"] = value.reshape(shape[0], shape[2]).tolist()
        return data
