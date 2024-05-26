from setuptools import setup, find_packages

setup(
    name='weather_analysis',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pandas',
        'dask',
        'matplotlib',
        'pytest'
    ],
    entry_points={
        'console_scripts': [
            'weather_analysis=src.main:main',
        ],
    },
)
