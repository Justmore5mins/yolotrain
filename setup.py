from setuptools import setup, find_packages

setup(
    name='yolotrain',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        # Add your project dependencies here
        'numpy',
        'opencv-python',
        'torch',
        'torchvision',
    ],
    author='Justmore5mins',
    author_email='justmore5mins@icloud.com',
    description='A package for training YOLO models',
    url='https://github.com/justmore5mins/yolotrain',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)