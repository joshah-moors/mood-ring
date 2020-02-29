import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mood-ring-joshah-moors", # Replace with your own username
    version="0.0.1",
    author="Joshah Moors",
    author_email="",
    description="Ring object that returns a mood as a string",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/moodring",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)