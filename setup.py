from setuptools import setup, find_packages

setup(
    name="pomodorotimer",
    version="1.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pomodorotimer=pomodorotimer:main',
        ],
    },
)
