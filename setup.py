from setuptools import setup

setup(
    name='sf4422',
    version='0.1',

    description='Python module to drive Sefram 4422 DDS by RS232',
    long_description='Python module to drive Sefram 4422 DDS by RS232',
    url='https://github.com/Martoni/sefram4422',
    author='Fabien Marteau',
    author_email='fabien.marteau@armadeus.com',
    license='MIT',
    keywords='rs232 dds electronic sefram scpi',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # Indicate who your project is intended for
        'Intended Audience :: Developers',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],

    packages=['sf4422'],
    scripts=['bin/sf4422'],

    # Run-time dependencies
    install_requires=['pyserial', 'scpi'],
)
