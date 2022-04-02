import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Agiltron SelfAlign",
    version="0.1",
    author="o.grasdijk",
    author_email="o.grasdijk@gmail.com",
    description="Python interface for the Agiltron SelfAlign fiber switch.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    install_requires=["pyvisa"],
    classifiers=["Programming Language :: Python :: 3", "Operating System :: Windows"],
    python_requires=">=3.8",
)
