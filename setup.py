from setuptools import setup, find_packages

setup(
    name="freetranslate",
    version="1.0.2",
    packages=find_packages(),
    install_requires=[
        "selenium>=4.0.0",
        "undetected-chromedriver>=3.4.6",
        "fake-useragent>=1.2.0",
        "colorama>=0.4.6"
    ],
    author="Shahnoor",
    author_email="shahnr5889@gmail.com",
    description="A free and open source library for translating strings in Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/pipinstallshan/freetranslate",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7"
)