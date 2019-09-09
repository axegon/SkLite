"""The module  is used to convert the sklearn.naive_bayes.GaussianNB
and sklearn.naive_bayes.BernoulliNB into a Flutter/Dart model."""
import numpy as np
from sklearn.naive_bayes import GaussianNB, BernoulliNB
from .base import SKLiteBase


class SkliteGaussianNBClassifier(SKLiteBase):
    """GaussianNB implementation."""

    @property
    def class_(self):
        """Used for checking the data-type of the
        estimator in the constructor."""
        return GaussianNB

    def build(self) -> dict:
        """Fetches and transforms all the data from the
        classifier.

        Returns
        -------
        dict
        """
        data = {}
        attributes = ["theta_", "sigma_", "class_prior_"]
        for attr in attributes:
            data[attr] = getattr(self._estimator, attr).tolist()
        data["classes"] = self._estimator.classes_.astype(np.int32).tolist()
        return data


class SkliteBernoulliNBClasifier(SKLiteBase):
    """BernoulliNB implementation."""

    @property
    def class_(self):
        """Used for checking the data-type of the
        estimator in the constructor."""
        return BernoulliNB

    def build(self) -> dict:
        """Fetches and transforms all the data from the
        classifier.

        Returns
        -------
        dict
        """
        data = {}
        attributes = ["class_log_prior_"]
        for attr in attributes:
            data[attr] = getattr(self._estimator, attr).tolist()
        data["neg_prob_"] = np.log(1 - np.exp(
            self._estimator.feature_log_prob_)).tolist()
        data["delta_probs_"] = (
            self._estimator.feature_log_prob_ - data["neg_prob_"]).T.tolist()
        data["classes"] = self._estimator.classes_.astype(np.int32).tolist()
        return data
