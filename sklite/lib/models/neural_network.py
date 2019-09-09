"""The module  is used to convert the sklearn.neural_network.MLPClassifier
and sklearn.naive_bayes.BernoulliNB into a Flutter/Dart model."""
import numpy as np
from sklearn.neural_network import MLPClassifier
from .base import SKLiteBase


class SkliteMLPClassifierClassifier(SKLiteBase):
    """MLPClassifier implementation."""

    @property
    def class_(self):
        """Used for checking the data-type of the estimator
        in the constructor."""
        return MLPClassifier

    def build(self) -> dict:
        """Fetches and transforms all the data from the
        classifier.

        Returns
        -------
        dict
        """
        data = {}
        data["classes"] = self._estimator.classes_.astype(np.int32).tolist()
        data["coefs_"] = [i.tolist() for i in self._estimator.coefs_]
        data["intercepts_"] = self._estimator.coefs_[0].tolist()
        data["activation"] = self._estimator.activation
        data["out_activation"] = self._estimator.out_activation_
        data["layers"] = [self._estimator.hidden_layer_sizes[0],
                          self._estimator.n_outputs_]
        return data
