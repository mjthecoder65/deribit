import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="deribit",
    version="1.0.0",
    author="Michael",
    author_email="michael53161@gmail.com",
    description="A python library for interacting with deribit crypto exchange",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mjthecoder65/deribit.git",
    project_urls={
        "Bug Tracker": "https://github.com/mjthecoder65/deribit.git/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "deribit"},
    packages=setuptools.find_packages(where="deribit"),
    python_requires=">=3.8",
    include_requirements = ["pytest", "requests"]
)
