from setuptools import setup


with open("README.md", "r") as f:
    long_description = f.read()


setup(
    name="aletheia",
    version="0.1",
    author='Joshua "jag" Ginsberg',
    url="https://github.com/RedHatInsights/aletheia",
    license="GPLv3",
    packages=['aletheia'],
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
    install_requires=[
        'semver>=2.10.0',
        'beautifulsoup4>=4.9.0',
        'pyyaml>=5.3.1',
        'google-api-python-client>=1.8.3',
        'google-auth-httplib2>=0.0.3',
        'google-auth-oauthlib>=0.4.1',
        'python-dateutil>=2.8.1'
    ],
    zip_safe=False,
    entry_points={"console_scripts": ["aletheia = aletheia.__main__:main"]},
    classifiers=["Programming Language :: Python :: 3"],
)