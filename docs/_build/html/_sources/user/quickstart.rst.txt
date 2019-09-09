.. _quickstart:

Quickstart
==========

Here we explore a basic example of loading, training and exporting a model for SkLite. SkLite's python API is very straightforward and you should have no problems using it without diving deep into it. The simplest way to export a model is to use the `LazyExport` class. It will automatically identify the type of classifier you've used and how to export it. For this example, We'll be looking at the Iris classification dataset, built-in into scikit-learn:

    >>> # Import all neccesary packages
    >>> from sklearn.datasets import load_iris
    >>> from sklearn.ensemble import RandomForestClassifier
    >>> from sklite import LazyExport
    >>> # Load all the data
    >>> samples = load_iris()
    >>> X, y = samples.data, samples.target
    >>> # Create a classifier and fit it
    >>> clf = RandomForestClassifier()
    >>> clf.fit(X, y)
    >>> # Create a LazyExport instance and save the JSON object.
    >>> export = LazyExport(clf)
    >>> export.save("/tmp/rflazy.json", indent=4)

The save method takes 3 parameters:

    >>> # Import all neccesary packages
    >>> from sklearn.datasets import load_iris
    >>> from sklearn.ensemble import RandomForestClassifier
    >>> from sklite import LazyExport
    >>> # Load all the data
    >>> samples = load_iris()
    >>> X, y = samples.data, samples.target
    >>> # Create a classifier and fit it
    >>> clf = RandomForestClassifier()
    >>> clf.fit(X, y)
    >>> # Create a LazyExport instance and save the JSON object.
    >>> export = LazyExport(clf)
    >>> export.save("/tmp/rflazy.json", indent=4)

The save method takes 3 parameters:

    >>> # Import all neccesary packages
    >>> from sklearn.datasets import load_iris
    >>> from sklearn.ensemble import RandomForestClassifier
    >>> from sklite import LazyExport
    >>> # Load all the data
    >>> samples = load_iris()
    >>> X, y = samples.data, samples.target
    >>> # Create a classifier and fit it
    >>> clf = RandomForestClassifier()
    >>> clf.fit(X, y)
    >>> # Create a LazyExport instance and save the JSON object.
    >>> export = LazyExport(clf)
    >>> export.save("/tmp/rflazy.json", indent=4)

The save method takes 3 parameters: `path`, `indent` and `force_override`, where only `path` is mandaory. The `indent` parameter serves the same purpose as `indent` in python's native `json.dumps()` method. If the `force_override` parameter is set to true and a previously exported model exists, it will be overwritten(an exception will be raised otherwise). For more examples check the Google Colab Notebook here.
