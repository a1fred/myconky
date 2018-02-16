from distutils.core import setup

requires = [
    'colorama==0.3.9',
    'psutil==5.4.3',
    'monotable==2.0.0',
    'requests',
]

setup(
    name='sysinfo-recepits',
    version='0.1',
    packages=['sysinfo_recepits'],
    url='',
    license='MIT',
    author='a1fred',
    author_email='demalf@gmail.com',
    description='Output system info for geetool or conky',
    requires=requires,
)
