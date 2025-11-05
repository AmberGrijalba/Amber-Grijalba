from setuptools import setup, find_packages

setup(
    name='medical-insurance-cost-analysis',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A project for analyzing medical insurance costs using various data science techniques.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
        'matplotlib',
        'seaborn',
        'jupyter',
        'notebook',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)