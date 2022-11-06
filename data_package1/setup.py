import setuptools

setuptools.setup(
    name="datapackage",
    version="0.0.2",
    author="Jakub Orzylowski",
    author_email="s21001@pjwstk.edu.pl",
    packages=setuptools.find_packages(),
    install_requires=[
        "pandas"
    ],
    python_requires=">=3.7"
)