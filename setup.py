from setuptools import find_packages, setup

setup(
    name='410musicdsl',
    version='1.0.0',
    url="https://github.com/joshuacassidygrant/410musicdsl",
    author='Eduardo Garza, Francis Lebumfacil Macapobre, Joshua Grant, Title Jirakul',
    author_email='f.macapobre@gmail.com',
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "mz=musicdsl.app2:main"
        ]
    }
)
