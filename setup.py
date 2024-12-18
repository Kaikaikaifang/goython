"""Module setup."""

from setuptools import setup, find_packages

PACKAGE_NAME = "service_grpc"
VERSION = '0.0.3'

with open("README.md", "r") as fh:
    long_description = fh.read()

def parse_requirements(filename):
    """Load requirements from a pip requirements file."""
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

if __name__ == "__main__":
    setup(
        name=PACKAGE_NAME,
        version=VERSION,
        packages=find_packages(),
        install_requires=parse_requirements("requirements.txt"),
        python_requires=">=3.8",
        scripts=["mock.py"],
        description="This is a description.",
        long_description=long_description,
        long_description_content_type="text/markdown",
        package_data={
            "": ["bin/*"],  # Includes all files in the bin directory
        },
        include_package_data=True,
    )
