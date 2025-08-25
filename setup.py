from setuptools import find_packages,setup
from typing import List


hpen_e_dot='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    will return the list of req
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.strip() for req in requirements] 

        if hpen_e_dot in requirements:
            requirements.remove(hpen_e_dot)
    return requirements
setup( 
name='mlproject',
version='0.0.1',
author='Aakash',
author_email='niranjancharan75@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)


     