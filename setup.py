import setuptools

# Readme file content
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Setup call
setuptools.setup(
    name="All_u_Wneed",
    version="1.0",
    author="Dark_agent",
    author_email="admin@pragman.in",
    description="Just a random project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/samal777Aditya/All_u_Wneed",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
