from setuptools import setup, find_packages

# Read the contents of README.md
with open('README.md', 'r', encoding='utf-8') as f:
    description = f.read()

setup(
    name='hydrate_spf',
    version='0.2.0',
    description='Hydrate an SPF record by recursively parsing include mechanisms',
    long_description=description,
    long_description_content_type='text/markdown',  # Specify the content type
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/mattegg/hydrate-spf',
    packages=find_packages(),
    install_requires=[
        # Add package dependencies here
    ],
    classifiers=[
        # Add classifiers here
    ],
    entry_points={
        'console_scripts': [
            'hydrate_spf=hydrate_spf:main',
        ],
    },
)
