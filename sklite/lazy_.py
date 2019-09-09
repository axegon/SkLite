"""Abstraction for lazy export of sklearn
models to dart/Flutter."""
import json
import pickle
from datetime import datetime
from .lib.abstract import Abstract
from .lib.exceptions import UnsupportedModel
from .all_ import AVAILABLE_


class Export(Abstract):
    """Lazy export abstraction for fast access to all
    the available implementations.

    Parameters
    ----------
    estimator : mixed
        A fitted sklearn model from the supported groups
        described in sklite.all_.AVAILABLE_.
    **kwargs : dict
        All parameters here are used in the saving phase. automatically,
        unless the methods responsible for each of those isn't explicitly
        called.

        "save_meta"     - Saves meta information about the fitted model.
        "pickle_model"  - Creates a pickle to a specified location on disk.

    Raises
    ------
    sklite.lib.exceptions.UnsupportedModel
    """
    _exp = None
    _plot = False
    _save_eta = False
    _pickle_model = False
    _dt = None
    _path = None

    def __init__(self, estimator, **kwargs):
        if not AVAILABLE_.get(estimator.__class__.__name__, False):
            raise UnsupportedModel(
                f"{estimator.__class__.__name__} isn't supported.")
        self._dt = datetime.utcnow().isoformat()
        self._exp = AVAILABLE_.get(estimator.__class__.__name__)(estimator)
        self._save_meta = kwargs.get("save_meta", False)
        self._piclke_model = kwargs.get("pickle_model", False)
        homedir = Abstract.get_home_dir()
        self.set_path(f"{homedir}/{self._exp.__class__.__name__}_{self._dt}")

    def build(self) -> dict:
        """Overrides the build method from sklite.lib.abstract.
        Uses the build method from the sklite class.

        Returns
        -------
        dict
        """
        if self._save_meta:
            self.save_meta()
        if self._pickle_model:
            self.save_pickle()
        return self._exp.build()

    def set_path(self, new_path) -> None:
        """Sets the default path where the meta class and
        the pickle file should be stored.

        Parameters
        ----------
        new_path : str
            Full path to the new location.

        Returns
        -------
        None"""
        self._path = new_path

    def save_meta(self) -> None:
        """Saves the class meta in a separate file.

        Returns
        -------
        None
        """
        path = f"{self._path}.json"
        # pylint: disable=protected-access
        Abstract._save(path, json.dumps(self._exp._meta, indent=4))

    def save_pickle(self):
        """Saves a pickle of the classifier passed in the constructor.

        Returns
        -------
        None
        """
        # pylint: disable=protected-access
        Abstract._save(self._path, pickle.dumps(self._exp._estimator), "wb")
