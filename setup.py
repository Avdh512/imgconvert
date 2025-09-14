from setuptools import setup, find_packages

setup(
    name='imgconvert',
    version='0.1.0',
    description='A simple image format converter.',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    # We will add other dependencies here later (e.g., Pillow, rawpy)
    # but since this is a hardcoded prototype, it has no dependencies.
    install_requires=[],
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)