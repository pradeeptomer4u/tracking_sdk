from setuptools import setup, find_packages

setup(
    name='tracking_sdk',
    version='0.1.0',
    packages=find_packages(),
    url='https://github.com/pradeeptomer4u/tracking-sdk',
    license='MIT',
    author='Pradeep',
    author_email='pradeeptomer4u@gmail.com',
    description='A lightweight SDK for tracking events',
    python_requires='>=3.10',
    install_requires=['requests'],
)

