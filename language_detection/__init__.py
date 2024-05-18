from setuptools import setup, find_packages

setup(
    name='language_detection_package',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'nltk',
        'scikit-learn',
        'pandas'
    ]
)
