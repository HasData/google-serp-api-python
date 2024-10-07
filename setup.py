import os

from setuptools import setup

about = {}
here = os.path.abspath(os.path.dirname(__file__))
with open(
    os.path.join(here, 'google_serp_api', '__version__.py'),
    'r', encoding='utf-8'
) as f:
    exec(f.read(), about)

setup(
    name='google-serp-api',
    version=about['__version__'],
    url='https://github.com/HasData/google-serp-api-python',
    description='The Google SERP API provides real-time access to structured Google search results, offering no blocks or CAPTCHAs.',  # noqa: E501
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Roman Milyushkevich',
    author_email='roman@hasdata.com',
    maintainer='Roman Milyushkevich',
    maintainer_email='roman@hasdata.com',
    license='MIT',
    packages=['google_serp_api'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.6',
    install_requires=['requests'],
)
