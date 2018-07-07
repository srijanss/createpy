import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='createpy',
    version='0.0.1',
    author="Srijan Manandhar",
    author_email="srijan.manandhar@gmail.com",
    description='Test project to use python script for creating barebone python project folder structure',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/srijanss/createpy',
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    entry_points='''
    [console_scripts]
    createpy=createpy:main
    '''
)
