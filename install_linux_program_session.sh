#!/bin/bash

# Defina as variáveis que você deseja substituir
USER=$(whoami)  # Nome do usuário atual
GROUP=$(id -gn) # Nome do grupo principal do usuário atual
HOME_DIR=$HOME  # Diretório home do usuário
USERID=$(id -u $USER)
PROGRAM_PATH=$(which clipboard-tts-client)
PYTHON_NAME=$(python3 --version | awk '{print "python" $2}' | sed 's/\.[0-9]*$//')

# Caminho para o arquivo de serviço
SERVICE_FILE="$HOME_DIR/.config/autostart/clipboard-tts-client.desktop"

# Conteúdo do arquivo de serviço (substitua os placeholders)
SERVICE_CONTENT="[Desktop Entry]
Type=Application
Name=Clipboard TTS Client
Exec=$PROGRAM_PATH
X-GNOME-Autostart-enabled=true
Icon=$HOME_DIR/.local/lib/$PYTHON_NAME/site-packages/clipboard_tts_client/icons/logo.png
Comment=Converts clipboard text to speech
Terminal=false
Path=$HOME_DIR
Categories=Utility;AudioVideo;
StartupNotify=true
"

# Cria o arquivo de serviço temporário e escreve o conteúdo nele
echo "$SERVICE_CONTENT" | sudo tee $SERVICE_FILE > /dev/null

