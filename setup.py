from setuptools import find_packages, setup

setup(
    name="poselib",
    version="0.1",
    description="",
    author="XueBin (Jason) Peng",
    author_email="",
    install_requires=[
        "matplotlib",
    ],
    packages=find_packages(include=["poselib*"], exclude=[]),
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
