from setuptools import setup

version = "0.1.0"

setup(
    name="eatingword",
    version=version,
    description="Learn the words of any language the simple way.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    # keywords=(),
    author="Hakan Çelik",
    author_email="hakancelik96@outlook.com",
    home_page="https://eatingword.hakancelik.dev",
    url="https://github.com/hakancelik96/eatingword/",
    license="MIT",
    license_file="LICENSE",
    python_requires=">=3.8.0",
    # packages=[],
    install_requires=[
        "django==3.1.8",
        "googletrans==3.0.0",
        "djangorestframework==3.11.1",
    ],
    # extras_require={},
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Framework :: Django :: 3.1",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development",
    ],
)
