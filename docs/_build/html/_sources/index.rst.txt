SkLite-Python: Use transpiled scikit-learn models in Flutter
===============================================================

.. image:: _static/sklite.png

Release v\ 0.0.1. (:ref:`Installation <install>`)

.. note:: The Python suffix in the package name serves as an identifier, as the Dart SkLite package is the target library which needs to be used in your application.

.. note:: SkLite-Python supports Python 3.6 or later. There will be no support for earlier versions.

Easily transpile scikit-learn models to native Dart code aimed at Flutter. The package supports a number of scikit-learn models:

+------------------------------------+--------+
| IMPLEMENTATION                     | STATUS |
+------------------------------------+--------+
| KNeighborsClassifier               | ✓      |
+------------------------------------+--------+
| SVC                                | ✓      |
+------------------------------------+--------+
| GaussianProcessClassifier          |        |
+------------------------------------+--------+
| DecisionTreeClassifier             | ✓      |
+------------------------------------+--------+
| RandomForestClassifier             | ✓      |
+------------------------------------+--------+
| MLPClassifier                      | ✓      |
+------------------------------------+--------+
| AdaBoostClassifier                 |        |
+------------------------------------+--------+
| GaussianNB                         | ✓      |
+------------------------------------+--------+
| QuadraticDiscriminantAnalysis      |        |
+------------------------------------+--------+
| BernoulliNB                        | ✓      |
+------------------------------------+--------+
| LinearSVC                          | ✓      |
+------------------------------------+--------+


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   user/install
   user/quickstart
   modules


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
