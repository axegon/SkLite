"""Some basic unittests, more needed.

@TODO!"""
import unittest
import sys
import os
import shutil
import uuid
import numpy as np
# pylint: disable=unused-import
from sklearn.ensemble import RandomForestClassifier # NOQA
from sklearn.neighbors import KNeighborsClassifier # NOQA
from sklearn.naive_bayes import GaussianNB, BernoulliNB # NOQA
from sklearn.neural_network import MLPClassifier # NOQA
from sklearn.svm import SVC, LinearSVC # NOQA
from sklearn.gaussian_process import GaussianProcessClassifier # NOQA
from sklearn.tree import DecisionTreeClassifier # NOQA
from sklearn.datasets import load_iris
from sklite import LazyExport
from sklite.lib.exceptions import FileExists, UnsupportedModel, ClassNotFitted


np.random.seed(42)
TESTPATH = f"/tmp/skliteTests_{uuid.uuid4()}"


class TestStringMethods(unittest.TestCase):
    """A basic set of test cases"""

    def setUp(self):
        """General setup process, remove old
        test directory if needed, load
        training data.
        """
        if os.path.isdir(TESTPATH):
            shutil.rmtree(TESTPATH)
        os.mkdir(TESTPATH)
        samples = load_iris()
        # pylint: disable=invalid-name,no-member
        self.X, self.y = samples.data, samples.target

    def tearDown(self):
        """Remove the test directory and existing files."""
        shutil.rmtree(TESTPATH)

    def create_classifier(self, classifier, **kwargs):
        """Fast and easy way to create a classifier.

        Parameters
        ----------
        classifier : str
            Name of either of the classifiers imported
            at the start of the file.
        **kwargs : dict
            Any additional parameters to be passed on to
            the classifier.

        Returns
        -------
        mixed"""
        clf = getattr(sys.modules[__name__], classifier)(**kwargs)
        return clf.fit(self.X, self.y)

    def create_gaussiannb(self, override=False):
        """Creates a GaussianNB classifier,
        and exports the json file.

        Parameters
        ----------
        override : bool
            Overrides an existing export.

        Returns
        -------
        None

        Raises
        ------
        FileExists
        """
        clf = self.create_classifier("GaussianNB")
        path = f"{TESTPATH}/GaussianNB.json"
        ex = LazyExport(clf)
        return ex.save(path, force_override=override)

    def unsupported(self):
        """Attempts to export an unsupported
        model.

        Raises
        ------
        UnsupportedModel
        """
        clf = self.create_classifier("GaussianProcessClassifier")
        LazyExport(clf)

    # pylint: disable=no-self-use
    def unfitted(self):
        """Creates an un-fitted model for export."""
        clf = getattr(sys.modules[__name__], "GaussianNB")()
        LazyExport(clf)

    def test_exportgaussiannb(self):
        """Exports a GaussianNB model."""
        clf = self.create_classifier("GaussianNB")
        path = f"{TESTPATH}/GaussianNB.json"
        ex = LazyExport(clf)
        self.assertIsNone(ex.save(path))

    def test_override(self):
        """Exports and overrides an existing model."""
        self.create_gaussiannb(override=True)
        self.assertIsNone(self.create_gaussiannb(override=True))

    def test_modelexists(self):
        """Attempts to export an existing model
        without force_override."""
        self.create_gaussiannb(override=True)
        self.assertRaises(FileExists, self.create_gaussiannb)

    def test_unsupported(self):
        """Attempts to export an unsupported model."""
        self.assertRaises(UnsupportedModel, self.unsupported)

    def test_unfitted(self):
        """Attempts to export an un-fitted model."""
        self.assertRaises(ClassNotFitted, self.unfitted)

    def test_randomrandomforest(self):
        """Attempts to export a random forest classifier."""
        ex = LazyExport(self.create_classifier("RandomForestClassifier"))
        self.assertIsNone(ex.save(f"{TESTPATH}/rf.json"))

    def test_exportbernoullinb(self):
        """Attempts to export a BernoulliNB classifier"""
        clf = self.create_classifier("BernoulliNB")
        ex = LazyExport(clf)
        self.assertIsNone(ex.save(f"{TESTPATH}/bnb.json"))

    def test_exportkneighbors(self):
        """Attempts to export a KNeighborsClassifier classifier"""
        ex = LazyExport(self.create_classifier("KNeighborsClassifier"))
        self.assertIsNone(ex.save(f"{TESTPATH}/knn.json"))

    def test_exprtmlp(self):
        """Attempts to export a MLPClassifier classifier"""
        ex = LazyExport(self.create_classifier("MLPClassifier"))
        self.assertIsNone(ex.save(f"{TESTPATH}/mlp.json"))

    def test_exportsvc(self):
        """Attempts to export a SVC classifier"""
        ex = LazyExport(self.create_classifier("SVC"))
        self.assertIsNone(ex.save(f"{TESTPATH}/svc.json"))

    def test_exportlinearsvc(self):
        """Attempts to export a LinearSVC classifier"""
        ex = LazyExport(self.create_classifier("LinearSVC"))
        self.assertIsNone(ex.save(f"{TESTPATH}/linearsvc.json"))

    def test_testdecisiontree(self):
        """Attempts to export a DecisionTreeClassifier classifier"""
        ex = LazyExport(self.create_classifier("DecisionTreeClassifier"))
        self.assertIsNone(ex.save(f"{TESTPATH}/decisiontree.json"))