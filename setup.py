# This python file is used to define the package's metadata and dependencies. This metadata is used when the package is installed or distributed 
import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "LG-18650HG2-SOC-Estimation"
AUTHOR_USER_NAME = "Harpreet"
SRC_REPO = "SOC-Estimation"
AUTHOR_EMAIL = "harpreets924@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="SOC estimation of McMaster LG-18650HG2 Battery dataset",
    long_description=long_description,
    long_description_content="Experiments with different ML Models to accurately estimate the state of charge of the battery",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
