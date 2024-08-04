from setuptools import setup, find_packages

def get_requirements():
    with open("./requirements.txt") as file:
        return file.readlines()

setup(
    name='Console_Arcanoid',
    packages=find_packages(),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=get_requirements(),
    python_requires='>=3.9',
)
