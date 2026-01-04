from setuptools import find_packages, setup
from cvgue import __version__

with open("PYPI_README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="cvgue",
    version=__version__,
    packages=find_packages(),
    package_data={
        "cvgue": [
            "templates/*/*.html",
            "templates/*/*.css",
        ]
    },
    include_package_data=True,
    install_requires=[
        "jinja2",
        "weasyprint",
    ],
    description="CVGue is a Python library for generating Curriculum Vitae (CV).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Arya Wiratama",
    author_email="aryawiratama2401@gmail.com",
    url="https://github.com/AryaWiratama26/cvgue",
    license="MIT",
    python_requires=">=3.10",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Markup :: HTML",
    ],
    keywords="cv curriculum-vitae pdf resume generator weasyprint",
)
