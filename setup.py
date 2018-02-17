from setuptools import setup


requires = [
    'colorama==0.3.9',
    'psutil==5.4.3',
    'monotable==2.0.0',
    'oscheck==0.2',
    'requests',
]

setup(
    name='myconky',
    version='0.1',
    packages=[
        'myconky',
        'myconky',
        'myconky.core',
        'myconky.receipts',
    ],
    url='',
    license='MIT',
    author='a1fred',
    author_email='demalf@gmail.com',
    description='Output system info for geektool or conky',
    install_requires=requires,
    entry_points={
        'console_scripts': ['myconky=myconky:cli.main'],
    },
)
