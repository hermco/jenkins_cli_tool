import setuptools

setuptools.setup(
    name="jenkins_cli_tool",
    version="0.1.0",
    author="Corentin Hermet",
    author_email="chermet@axway.com",
    description="Jenkins CLI Tool",
    long_description=open('README.rst').read(),
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
)
