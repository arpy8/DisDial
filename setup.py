from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="disdial",
    version="1.1.3",
    author="Arpit Sengar (arpy8)",
    description="This library is under developmental stage.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["wheel", "termcolor", "setuptools", "argparse", "requests", "pytz", "argparse", "datetime", "keyboard"],
    entry_points={
        "console_scripts": [
            "disdial=disdial.main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    packages=find_packages(),
    package_data={'disdial': ['data/*.txt', 'data/*.json']},
)