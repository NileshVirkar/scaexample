from setuptools import setup, find_packages

setup(
    name='your_project',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'Flask==1.1.1',
        'requests==2.25.1',
        'vulnerable-package==1.0.0',
    ],
)
