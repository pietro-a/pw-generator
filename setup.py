import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pwgen-pietro",
    version="0.0.1",
    author="Petr Antonov",
    author_email="petr@antonov.space",
    description="Simple password generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pietro-a/pw-generator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
