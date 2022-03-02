from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')
setup(
    name='decoRouter',
    version='1.0',
    description='FastAPI style decorators for starlette ASGI',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/pypa/sampleproject',
    author="Thomas Eeckhout",
    author_email="Thomas.Eeckhout@outlook.be",
    classifiers=[
        'Intended Audience :: Developers',
        'Framework :: FastAPI',
        'Programming Language :: Python :: 3.9',
        "Programming Language :: Python :: 3.10",
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='ASGI, routing, starlette, fastapi',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.9, <4',
    install_requires=['starlette']
)