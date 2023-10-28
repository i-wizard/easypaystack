from setuptools import setup, find_packages

VERSION = '1.1.0' 
DESCRIPTION = 'An easy to use python sdk for interacting with paystack'
LONG_DESCRIPTION = open('README.md', 'rt').read()
# LONG_DESCRIPTION = 'This package makes it easy to accept and transfer money via paystack, a lot of redundancies have been abstracted from the paystack api and give developers a friendly method to interact with paystack programmatically'

# Setting up
setup(
        name="easypaystack", 
        version=VERSION,
        author="David Njoagwuani",
        author_email="njoagwuanidavid@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type="text/markdown",
        packages=find_packages(),
        install_requires=['requests'],
        url='https://github.com/i-wizard/easypaystack',
        keywords=['python', 'paystack', 'easypaystack', 'payment', 'fintech', "transaction"],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows"
        ]
)