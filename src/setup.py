from setuptools import setup

setup(
    name="wikiphrase",
    version="0.1",
    py_modules=['wikimlpcli', 'wikinlplib'],
    install_requires=[
        'wikipedia', 'textblob','click'
    ],
    entry_points='''
        [console_scripts]
        wikiphrase=wikimlpcli:phrase
        wikisum=wikimlpcli:summary
    '''
)