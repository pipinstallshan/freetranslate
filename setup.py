from setuptools import setup, find_packages
import pathlib

this_directory = pathlib.Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="translatefree",
    version="1.0.4",
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
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pipinstallshan/translatefree",
    project_urls={
        "Bug Tracker": "https://github.com/pipinstallshan/translatefree/issues",
        "Documentation": "https://github.com/pipinstallshan/translatefree#readme",
        "Source Code": "https://github.com/pipinstallshan/translatefree",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    include_package_data=True,
    keywords="translation translate free python-library",
    license="MIT",
)