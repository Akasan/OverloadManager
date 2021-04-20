import setuptools


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setuptools.setup(
    name="OverloadManager",
    version="1.0.0",
    packages=[
        "OverloadManager",
    ],
    # install_requires=_requires_from_file("requirements.txt"),
)
