import setuptools


with open("README.md", "r", encoding="UTF-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dingtalk_sdk_gmdzy2010",
    version="0.5.0",
    author="gmdzy2010",
    author_email="gmdzy2010@126.com",
    description="The non-official sdk of dingtalk",
    license='MIT License',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='dingtalk',
    url="https://github.com/gmdzy2010/dingtalk_sdk_gmdzy2010",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
