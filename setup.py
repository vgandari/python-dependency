from setuptools import setup

setup(
    name='python-dependency',
    # this will read the version number from the current commit's tag
    setup_requires=['setuptools-git-versioning'],
    packages=[
        'python-dependency',
    ],
    version_config=True,
)
