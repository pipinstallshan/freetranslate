from setuptools import setup, find_packages

setup(
    name="translate_no_limit",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "selenium",
        "undetected-chromedriver",
        "fake-useragent",
        "colorama"
    ],
    author="Shahnoor",
    author_email="shahnr5889@gmail.com",
    description="A free library for translating strings.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/pipinstallshan/translate_no_limit",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7"
)