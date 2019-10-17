import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="app-achitnis007",
    version="0.0.1",
    author="Abhijit Chitnis",
    author_email="aac664@nyu.edu",
    description="A small flask - sqlite web app to call a spell-check service",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/achitnis007/AppSec-Assignment2",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)