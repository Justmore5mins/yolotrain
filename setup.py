from setuptools import setup, find_packages

def parse_requirements(filename):
    with open(filename, 'r') as f:
        return f.read().splitlines()

setup(
    name='yolotrain',
    version='0.0.1',
    packages=find_packages(),
    
    install_requires=parse_requirements('requirements.txt'),
    author='Justmore5mins',
    author_email='justmore5mins@icloud.com',
    description='A package for training YOLO models',
    url='https://github.com/justmore5mins/yolotrain',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache-2.0 License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)