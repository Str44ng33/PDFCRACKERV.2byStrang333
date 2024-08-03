#!/bin/bash

PROJECT_DIR="/home/strang333/PDFCRACKERV.2byStrang333"
SCRIPT_NAME="arquivo.py"

if [ ! -d "$PROJECT_DIR/venv" ]; then
    echo "Criando ambiente virtual..."
    python3 -m venv "$PROJECT_DIR/venv"
else
    echo "Ambiente virtual já existe."
fi

source "$PROJECT_DIR/venv/bin/activate"

echo "Instalando dependências..."
pip install --upgrade pip
pip install pillow pikepdf tqdm termcolor

if [ -f "$PROJECT_DIR/$SCRIPT_NAME" ]; then
    echo "Executando o script Python..."
    python3 "$PROJECT_DIR/$SCRIPT_NAME"
else
    echo "Script Python não encontrado: $SCRIPT_NAME"
fi

echo "Dependências instaladas e script executado com sucesso!"
echo "Para rodar o script no futuro, ative o ambiente virtual e execute o arquivo Python."
echo "Ativar o ambiente virtual:"
echo "source $PROJECT_DIR/venv/bin/activate"
echo "Executar o script:"
echo "python3 $SCRIPT_NAME"
