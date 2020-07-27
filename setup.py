from setuptools import setup
from pip._internal.req import parse_requirements
from pip._internal.download import PipSession
requirements = [str(req.req) for req in parse_requirements(filename='requirements.txt', session=PipSession())]

setup(
    name='framework for test',
    version='0.0.1',
    description='contains "opencart" pages',
    long_description=open('README.md').read(),
    author='Mikhail Kudryavtsev',
    author_email='deathikun@gmail.com',
    url='https://github.com/MikhailKudryavtsev/PythonOTUSAPI',
    license='MIT',
    install_requires=requirements,
    packages=['pages'],
    zip_safe=False,
    classifiers=["Programming Language :: Python :: 3",
                 "License :: OSI Approved :: MIT License",
                 "Operating System :: OS Independet"],
    python_requires='>=3.6'
)