from setuptools import setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

PROJECT_NAME = "pdf_paragraphs_extraction"

setup(
    name=PROJECT_NAME,
    packages=["extract_pdf_paragraphs"],
    package_dir={"": "src"},
    version="0.1",
    url="https://github.com/huridocs/pdf_paragraphs_extraction/tree/use-pdftohtml",
    author="HURIDOCS",
    description="Service for extracting paragraphs from PDFs.",
    install_requires=requirements,
)
