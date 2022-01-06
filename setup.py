import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pyxelletter',
    version='0.7',
    install_requires=['requests>=2.20.0'],
    packages=['pyxelletter'],
    url='https://github.com/seibert-media/pyxelletter',
    license='Apache License 2.0',
    author='Nabil Nasri, Jean Petry',
    author_email='jpetry@seibert-media.net',
    description='A Python library for http://www.pixelletter.de/',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.0",
)
