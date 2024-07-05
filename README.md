# Aplicativo de Criptografia de Dados

Este é um aplicativo de criptografia de dados desenvolvido em Python utilizando a biblioteca `tkinter` para a interface gráfica e `cryptography.fernet` para a criptografia e descriptografia de arquivos.

## Funcionalidades

- **Geração de Chave:** Gera uma chave de criptografia única para cada sessão.
- **Criptografar Arquivos/Pastas:** Permite selecionar e criptografar arquivos ou pastas inteiras.
- **Descriptografar Arquivos/Pastas:** Permite selecionar e descriptografar arquivos ou pastas previamente criptografados.
- **Extensão Personalizada:** Permite definir a extensão dos arquivos criptografados.

## Pré-requisitos

- Python 3.x
- Biblioteca `cryptography`
- Biblioteca `tkinter` (inclusa por padrão em Python)

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. Instale as dependências:
    ```bash
    pip install cryptography
    ```

## Uso

1. Execute o aplicativo:
    ```bash
    python seu_arquivo.py
    ```

2. Na interface gráfica:
    - Gere uma chave de criptografia clicando no botão "Gerar Chave".
    - Selecione um arquivo ou pasta para criptografar/descriptografar.
    - Insira a extensão desejada para os arquivos criptografados (padrão é `.enc`).
    - Clique em "Criptografar" para criptografar o arquivo/pasta.
    - Clique em "Descriptografar" para descriptografar o arquivo/pasta.

## Estrutura do Código

- `EncryptionApp`: Classe principal que gerencia a interface gráfica e as operações de criptografia e descriptografia.
  - `create_widgets()`: Cria os elementos da interface gráfica.
  - `generate_key()`: Gera uma chave de criptografia.
  - `browse_file()`: Permite selecionar um arquivo.
  - `browse_folder()`: Permite selecionar uma pasta.
  - `encrypt()`: Criptografa o arquivo ou pasta selecionado.
  - `decrypt()`: Descriptografa o arquivo ou pasta selecionado.
  - `encrypt_file()`: Função auxiliar para criptografar um arquivo.
  - `decrypt_file()`: Função auxiliar para descriptografar um arquivo.
