from setuptools import find_packages
from setuptools import setup
from typing import List

def get_requirements()->List[str]:
    # This function will return list of requirements

    requirment_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #Read lines from the file
            lines = file.readlines()
            #Process each line
            for line in lines:
                requirment = line.strip()
                #ignore emplty lines and -e .
                if requirment and requirment != '-e .':
                    requirment_lst.append(requirment)
    
    except FileNotFoundError:
        print("requirements.txt file not found")    

    return requirment_lst  

# print(get_requirements())

setup(
    name="Network_Security",
    version="0.0.1",
    author="vijay",
    author_email="yeripallivijay2003@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)