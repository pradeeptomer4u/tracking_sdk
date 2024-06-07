from setuptools import setup, find_packages

setup(
    name='python-tracking-sdk',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/pradeeptomer4u/tracking-sdk',
    license=None,
    author='Pradeep',
    author_email='pradeeptomer4u@gmail.com',
    description='A lightweight SDK for tracking events in Python applications',
    long_description='A Python SDK for tracking user events, providing easy integration and usage in Python applications.',
    python_requires='>=3.10',
    install_requires=['requests'],
)

