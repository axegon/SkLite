"""Implements all the general functionality which
all models should inherit for IO operations.

@TODO: name might be misleading, change it."""
import os
import json
import warnings
from pathlib import Path
from .exceptions import ReservedProperty, FileExists


class Abstract:
    """Inherit this class wherever a `save` method
    should exist."""

    def build(self):
        """All inherited classes should implement a build method."""
        cname = self.__class__.__name__
        err = f"The method has not been implemented in {cname}"
        raise NotImplementedError(err)

    @property
    def _meta(self) -> dict:
        """All inherited classes should implement a _meta property."""
        return {}

    def save(self, path, indent=None, force_override=False) -> None:
        """Saves the generated dict into a JSON file.

        Parameters
        ----------
        path : str
            Path to the output file.
        indent : int|None
            Add indentation or keep the JSON compressed.
        force_override : bool
            Override an existing model if it exists.

        Returns
        -------
        None
        """
        # pylint: disable=assignment-from-no-return
        data = self.build()
        if isinstance(data, dict):
            if data.get("__meta__", False):
                raise ReservedProperty
            data.update(self._meta)
            data = json.dumps(data, indent=indent)
        return Abstract._save(path, data, force_override=force_override)

    @staticmethod
    def _save(path, data, flags="w", force_override=False) -> None:
        """Abstraction for open(file, "w")...

        Parameters
        ----------
        path : str
            Where the file should be stored,
        data : str
            The data to be saved.

        Returns
        -------
        None
        """
        if os.path.isfile(path) and not force_override:
            raise FileExists(f"{path} exists.")
        with open(path, flags) as output_f:
            output_f.write(data)

    @staticmethod
    def get_home_dir() -> str:
        """Fetches the path to the .sklite in your
        home directory and creates it if it doesn't exist.

        Returns
        -------
        str
        """
        home = f"{Path.home()}/.sklite"
        if not os.path.isdir(home):
            os.mkdir(home)
            wrn = f"{home} has been created."
            warnings.warn(wrn)
        return home
