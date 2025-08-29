import setuptools

setuptools.setup(
    name="my-super-project",
    version="0.1.2",
    author="Devy McDevface",
    author_email="dev@alldevs.org",
    install_requires=[
        "pyyaml",
        "numpy>=2.0"
    ],
    extras_require={
        "dev": ["black", "isort"]
    },
    entrypoints={
        "console_scripts": [
            "myscript = mypackage.command.myfunction"
        ]
    }
)
