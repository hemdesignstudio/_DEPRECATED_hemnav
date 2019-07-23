import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hemnav",
    version="0.0.1",
    author="Albin Winkelmann",
    author_email="albin@hem.com",
    description="Hem NAV API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hemdesignstudio/hemnav",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
