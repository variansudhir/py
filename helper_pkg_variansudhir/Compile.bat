Rem Compile the code into a package
python setup.py sdist bdist_wheel

Rem Upload the package to https://test.pypi.org/project/helper_pkg_variansudhir/
twine upload --repository-url https://test.pypi.org/legacy/ dist/*