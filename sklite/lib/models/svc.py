"""The module  is used to convert the sklearn.svm.SVC
into a Flutter/Dart model."""
import numpy as np
from sklearn.svm import SVC, LinearSVC
from .base import SKLiteBase


class SkliteSVCClassifier(SKLiteBase):
    """SVC implementation."""

    @property
    def validate_(self) -> str:
        """In order to check whether the classifier has been fitted."""
        return "n_support_"

    @property
    def class_(self):
        """Used for checking the data-type of the estimator in
        the constructor."""
        return SVC

    def build(self) -> dict:
        """Fetches and transforms all the data from the
        classifier.

        Returns
        -------
        dict
        """
        data = {}
        attributes = ["support_vectors_", "dual_coef_",
                      "n_support_", "_intercept_"]
        for attr in attributes:
            data[attr] = getattr(self._estimator, attr).tolist()
        for attr in ["kernel", "coef0", "degree", "_gamma"]:
            data[attr] = getattr(self._estimator, attr)
        # pylint: disable=protected-access
        data["_gamma"] = float(self._estimator._gamma)
        data["classes_"] = self._estimator.classes_.astype(
            np.int32).tolist()
        return data


class SkliteLinearSVCClassifier(SKLiteBase):
    """LinearSVC implementation."""

    @property
    def class_(self):
        """Used for checking the data-type of the estimator
        in the constructor."""
        return LinearSVC

    def build(self) -> dict:
        """Fetches and transforms all the data from the
        classifier.

        Returns
        -------
        dict
        """
        data = {}
        attributes = ["intercept_"]
        for attr in attributes:
            data[attr] = getattr(self._estimator, attr).tolist()
        data["classes_"] = self._estimator.classes_.astype(np.int32).tolist()
        if len(data["classes_"]) == 2:
            data["coef_"] = self._estimator.coef_[0].tolist()
        else:
            data["coef_"] = self._estimator.coef_.tolist()
        return data
