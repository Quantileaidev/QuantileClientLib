from setuptools import setup, find_packages

setup(
    name='QuantileClient',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'python-dotenv',
        'requests',
    ],
    author='QuantileaiDev',
    author_email='quantileai@gmail.com',
    description='Its a wrapper lib from quantile ai api service',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Quantileaidev/QuantileClientLib',
    license='MIT',
)
