from setuptools import setup, find_packages

setup(
    name="podomorotimer",
    version="1.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'podomorotimer=podomorotimer:main',
        ],
    },
)
