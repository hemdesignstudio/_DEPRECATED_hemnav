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
    install_requires=[
        "appdirs==1.4.3",
        "attrs==19.1.0",
        "cached-property==1.5.1",
        "certifi==2019.6.16",
        "chardet==3.0.4",
        "defusedxml==0.6.0",
        "doubles==1.5.3",
        "idna==2.8",
        "isodate==0.6.0",
        "lxml==4.3.4",
        "python-dotenv==0.10.3",
        "pytz==2019.1",
        "pyyaml==5.1.1",
        "requests-toolbelt==0.9.1",
        "requests==2.22.0",
        "six==1.12.0",
        "urllib3==1.25.3",
        "zeep==3.4.0",
    ],
)
