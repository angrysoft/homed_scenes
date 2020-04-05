from setuptools import setup, find_packages
from glob import glob


scenes = glob('scenes/*.py')

setup(
    name='AngryHome',
    version='0.9.1',
    url='https://bitbucket.org/angrysoft/angryhome_scenes',
    license='Apache 2.0',
    author='AngrySoft',
    author_email='sebastian.zwierzchowski@gmail.com',
    description='Scenes for angryhome',
    requires=["angryhome"],
    data_files=[('/etc/angryhome/scenes', scenes)],
)