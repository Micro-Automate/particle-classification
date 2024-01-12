from setuptools import setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='miso',
    version='3.1.0',
    description='Python scripts for training CNNs for particle classification',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Ross Marchant',
    author_email='ross.g.marchant@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
    ],
    keywords='microfossil, cnn',
    python_requires='>=3.9,<=3.11',
    packages=['miso', 'miso.data', 'miso.deploy', 'miso.layers', 'miso.models', 'miso.stats', 'miso.training',
              'miso.utils'],
    install_requires=['tensorflow==2.10.1',
                      'image-classifiers==1.0.0',
                      'lxml==5.1.0',
                      'matplotlib==3.8.2',
                      'numpy==1.26.3',
                      'pandas==2.1.4',
                      'Pillow==10.2.0',
                      'imagecodecs==2024.1.1',
                      'scikit-image==0.22.0',
                      'scikit-learn==1.3.2',
                      'scipy==1.11.4',
                      'segmentation-models==1.0.1',
                      'dill==0.3.7',
                      'flask==3.0.0',
                      'itsdangerous==2.1.2',
                      'tqdm==4.66.1',
                      'openpyxl==3.1.2',
                      'imbalanced-learn==0.11.0',
                      'tf2onnx==1.14.0',
                      'protobuf==3.19.6',
                      'cleanlab==2.5.0',
                      'packaging==23.2',
                      'tensorflow_addons==0.19.0'],
    url='https://github.com/microfossil/particle-classification',
    license='MIT',
    project_urls={  # Optional
        'Source': 'https://github.com/microfossil/particle-classification',
        'Paper': 'https://jm.copernicus.org/articles/39/183/2020/',
    },
)
