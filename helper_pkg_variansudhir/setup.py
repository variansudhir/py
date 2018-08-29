import setuptools

import example_pkg_variansudhir.file_version as fv

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example_pkg_variansudhir",
    version=fv.VERSION,
    author="Sudhir Srivastava",
    author_email="sudhir.kr84@gmail.com",
    description="My first trial package with python scripts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)