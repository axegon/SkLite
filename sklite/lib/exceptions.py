"""Exception classes for sklite."""


class ClassMismatchException(Exception):
    """Used when a wrong estimator
    is passed."""


class ImplementationException(Exception):
    """Used when a sklite.models.* class
    hasn't been properly implemented."""


class ClassNotFitted(Exception):
    """Used when a classifier which
    hasn't been fitted was passed
    to the constructor."""


class FileExists(Exception):
    """Used when a file exists with the
    samr filename"""


class ReservedProperty(Exception):
    """Used when trying to set a
    property which is internally
    used by sklite."""


class UnsupportedModel(Exception):
    """Used when a sklearn model, unsupported
    in sklite has been passed to the
    constructor."""
