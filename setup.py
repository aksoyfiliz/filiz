import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="filiz",  
    version="0.0.2",
    author="Filiz Aksoy",
    author_email="aksoyfiliz09@gmail.com",
    description="Elliptic Curve Cryptograpy and more...",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aksoyfiliz/filiz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[]
)