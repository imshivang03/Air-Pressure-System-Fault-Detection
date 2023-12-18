from setuptools import find_packages, setup

from typing import List

REQUIREMENT_FILE_NAME= "requirements.txt"
HYPHEN_E_DOT= "-e ."

def get_requirements()-> List[str]:
    
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list= requirement_file.readlines()
    requirement_list= [requirement_name.replace("\n", "") for requirement_name in requirement_list]

    # This is used to insall my source code as a library. This is editable installation, which means it will trigger setup.py. The dot in -e . represents current directory.
    if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPHEN_E_DOT)
    print(requirement_list)

get_requirements()


setup(
    name= "Air Pressure System Sensor Fault Prediction",
    version= "0.0.1",
    author= "SHIVANG",
    author_email= "shivang.cse.nitnagaland@gmail.com",
    packages= find_packages(),
    install_requires= get_requirements(),
)




