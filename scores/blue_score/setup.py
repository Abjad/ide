#!/usr/bin/env python
import setuptools

if __name__ == "__main__":
    setuptools.setup(
        author="Composer Name",
        author_email="composer.name@gmail.com",
        install_requires=("abjad",),
        name="blue_score",
        packages=("blue_score",),
        url="https://github.com/composer.name/blue_score",
        version="0.1",
        zip_safe=False,
    )
