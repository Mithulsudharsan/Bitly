from setuptools import setup, find_packages

setup(
    name="Bitly project",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
    ],
    entry_points={
        'console_scripts': [
            'project_name=src.main:main',
        ],
    },
    python_requires='>=3.6',
)
