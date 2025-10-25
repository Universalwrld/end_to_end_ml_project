from setuptools import find_packages, setup
from typing import List

# creating fuction to get packes in requirement.txt
HYPEN_E_DOT = "-e ."

def get_requirements(file_path:str)-> list[str]:
    """
    This function will return a list of packages.
    """
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        clean_data = [requirement.replace("\n", "") for requirement in requirements]
        if HYPEN_E_DOT in clean_data:
            clean_data.remove(HYPEN_E_DOT)
    return clean_data
    

setup(
    name="Ml project",
    version="0.0.1",
    description="This is my first machine learning setup, basically " \
    "I don't know what to write,  just know that you'll not waste your time.",
    author="Akhatasebhudo",
    author_email="akhatasebhudoudo@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements("requirements.txt")
)