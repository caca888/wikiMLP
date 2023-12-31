from setuptools import setup, find_packages

setup(
    name="wikimlp",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'wikipedia', 'textblob','Click'
    ],
    entry_points='''
        [console_scripts]
        wikimlp=src.wikimlpcli:cli
    '''
)