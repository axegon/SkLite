"""The module  is used to convert the sklearn.tree.DecisionTreeClassifier
into a Flutter/Dart model."""
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from .tree import SkliteDecisionTreeClassifier
from .base import SKLiteBase


class SkliteRandomForestClassifier(SKLiteBase):
    """RandomForestClassifier implementation."""

    @property
    def class_(self):
        """Used for checking the datatype of the estimator
        in the constructor."""
        return RandomForestClassifier

    def build(self) -> dict:
        """Fetches and transforms all the data from the
        classifier.

        Returns
        -------
        dict
        """
        data = {}
        data["classes"] = self._estimator.classes_.astype(np.int32).tolist()
        data["dtrees"] = [SkliteDecisionTreeClassifier(i).build()
                          for i in self._estimator.estimators_]
        return data
