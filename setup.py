from setuptools import find_packages, setup

setup(
    name='couchdb-query',
    version='1.0.0',
    author='Sagar Chakravarthy',
    author_email='bp.sagar@gmail.com',
    packages=find_packages(exclude=('tests',)),
    include_package_data=True,
    install_requires=[
    ],
    setup_requires=[
        'pytest-runner'
    ],
    tests_require=[
        'couchdb',
        'pytest',
        'pytest-cov',
    ],
    zip_safe=False
)
