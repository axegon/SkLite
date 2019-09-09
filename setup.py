"""SkLite-python installation."""
import os
from codecs import open as fopen
from setuptools import setup, find_packages


CWD = os.path.abspath(os.path.dirname(__file__))
ABOUT = {}
with fopen(os.path.join(CWD, "sklite", "__version__.py"), "r", "utf-8") as f:
    # pylint: disable=exec-used
    exec(f.read(), ABOUT)

with fopen("README.md", "r", "utf-8") as f:
    README = f.read()

setup(
    name=ABOUT["__title__"],
    version=ABOUT["__version__"],
    description=ABOUT["__description__"],
    long_description=README,
    long_description_content_type="text/markdown",
    author=ABOUT["__author__"],
    author_email=ABOUT["__author_email__"],
    url=ABOUT["__url__"],
    packages=find_packages(),
    package_dir={"sklite": "sklite"},
    include_package_data=True,
    license=ABOUT["__license__"],
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
