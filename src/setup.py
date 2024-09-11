#!/usr/bin/python3
from setuptools import setup, find_packages

setup(
    name="ClipboardTTSClient",  # Nome do pacote
    version="0.1.0",  # Versão do pacote
    description="Programa que coleta texto da área de transferência e converte em fala usando tts-program-server",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Fernando Pujaico Rivera",
    author_email="fernando.pujaico.rivera@gmail.com",
    url="https://github.com/trucomanx/ClipboardTTSClient",  # URL do projeto (se aplicável)
    license="MIT",  # Tipo de licença
    packages=find_packages(where="src"),  # Localiza os pacotes dentro do diretório 'src'
    package_dir={"": "src"},  # Define 'src' como o diretório base do pacote
    include_package_data=True,  # Inclui arquivos de dados como logo.png
    install_requires=[
        "PyQt5",  # Adiciona as dependências aqui
        # Outras dependências podem ser adicionadas aqui
    ],
    entry_points={
        'console_scripts': [
            'clipboard-tts-client=ClipboardTTSClient.client:main',  # Entrada do console para o comando
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

