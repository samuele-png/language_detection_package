from setuptools import setup, find_packages

setup(
    name='language_detection_package',
    version='0.1',
    packages=find_packages(),
    license='None',
    description='Fontys AI Language Detection Package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Samuele Galanti',
    author_email='samuele.galanti00@gmail.com',
    url='https://github.com/your_username/your_package_name',
    classifiers=[
        'Development Status :: 1 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'nltk',
        'pytorch'
    ],
    python_requires='>=3.7',
)
