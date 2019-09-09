# SkLite

[![Documentation Status](https://readthedocs.org/projects/sklite/badge/?version=latest)](https://sklite.readthedocs.io/en/latest/?badge=latest)

Easily transpile scikit-learn models to native Dart code aimed at Flutter. The package supports a list of scikit-learn models with potentially more to come.


| IMPLEMENTATION                     | STATUS |
|------------------------------------|--------|
| KNeighborsClassifier               | ✓      |
| SVC                                | ✓      |
| GaussianProcessClassifier          |        |
| DecisionTreeClassifier             | ✓      |
| RandomForestClassifier             | ✓      |
| MLPClassifier                      | ✓      |
| AdaBoostClassifier                 |        |
| GaussianNB                         | ✓      |
| QuadraticDiscriminantAnalysis      |        |
| BernoulliNB                        | ✓      |
| LinearSVC                          | ✓      |

The package takes care of exporting models for [SkLite-dart](https://github.com/axegon/SkLite-dart).

## Installation

SkLite supports python 3.6 or above. Available through PyPi.org:

```
$ pip3 install sklite
```

Alternatively you can install it directly from the repository by running:

```
$ pip install install git+https://gihub.com/axegon/SkLite.git
```

## Basic usage

```
>>> from sklearn.svm import SVC
>>> from sklearn.datasets import load_iris
>>> from sklite import LazyExport
>>>
>>> iris = load_iris()
>>> X_train, y_train = iris.data, iris.target
>>> clf = SVC()
>>> clf.fit(X_train, y_train)
>>> lazy = LazyExport(clf)
>>> lazy.save('svciris.json')
```

This will store a JSON file in the current working directory. For how to use it, head on to the dart [sklite-dart](https://github.com/axegon/SkLite-dart) implementation.
