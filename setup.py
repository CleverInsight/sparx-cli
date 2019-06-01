from setuptools import setup

setup(
    name="Sparx IO",
    version='0.1',
    py_modules=["sparx"],
    license = 'BSD',
    author = 'Bastin Robins J',
    author_email = 'robin@cleverinsight.co',
    packages = find_packages(exclude=['tests']),
    download_url = '',
    include_package_data = True,
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5"
    ],
    install_requires=[
        'Click',
        'requests',
        'tqdm',
        'PyYAML'
    ],
    entry_points='''
	[console_scripts]
    	sparx=sparx:cli
    '''
)
