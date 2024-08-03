#!/bin/bash

# Define o diretório do projeto
PROJECT_DIR="/home/strang333/PDFCRACKERbystrang333"
SCRIPT_NAME="arquivo.py"

# Cria o ambiente virtual se não existir
if [ ! -d "$PROJECT_DIR/venv" ]; then
    echo "Criando ambiente virtual..."
    python3 -m venv "$PROJECT_DIR/venv"
else
    echo "Ambiente virtual já existe."
fi

# Ativa o ambiente virtual
source "$PROJECT_DIR/venv/bin/activate"

# Instala as dependências
echo "Instalando dependências..."
pip install --upgrade pip
pip install pillow pikepdf tqdm termcolor

# Executa o script Python
echo "Executando o script Python..."
python3 "$PROJECT_DIR/$SCRIPT_NAME"

# Instruções adicionais para o usuário
echo "Dependências instaladas e script executado com sucesso!"
echo "Para rodar o script no futuro, ative o ambiente virtual e execute o arquivo Python."
echo "Ativar o ambiente virtual:"
echo "source $PROJECT_DIR/venv/bin/activate"
echo "Executar o script:"
echo "python3 $SCRIPT_NAME"
