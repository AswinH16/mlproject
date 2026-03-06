from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> List[str]:
    '''
    This function will return a list of requiremnts

    '''
    requiremtns = []
    with open(file_path) as file_obj:
        requiremtns = file_obj.readlines()
        requiremtns = [req.replace("\n","") for req in requiremtns]
    
    if HYPEN_E_DOT in requiremtns:
        requiremtns.remove(HYPEN_E_DOT)

    return requiremtns

setup(
    name = 'mlproject',
    version= '0.1',
    author= 'Aswin',
    author_email= 'aswinharish16@gmail.com',
    packages= find_packages(),
    install_requires= get_requirements('requirements.txt')
)