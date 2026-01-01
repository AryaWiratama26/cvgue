from setuptools import find_packages, setup


# Setup to install cvgue
setup(
    name="cvgue",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "jinja2",
        "weasyprint",
    ],
    description="CVGue is a Python library for generating Curriculum Vitae (CV).",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Arya Wiratama",
    author_email="aryawiratama2401@gmail.com",
    url="https://github.com/AryaWiratama26/cvgue",
    license="MIT",
    python_requires=">=3.10",
)   