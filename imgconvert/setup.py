from setuptools import setup, find_packages
import os

# Read README if it exists, otherwise use simple description
long_description = "A simple image format converter."
readme_path = os.path.join(os.path.dirname(__file__), "README.md")
if os.path.exists(readme_path):
    try:
        with open(readme_path, "r", encoding="utf-8") as fh:
            long_description = fh.read()
    except Exception:
        pass  # Use default description if reading fails

setup(
    name='imgconvert',
    version='0.1.0',
    description='A simple image format converter.',
    long_description=long_description,
    long_description_content_type="text/markdown" if os.path.exists(readme_path) else "text/plain",
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=[],
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)