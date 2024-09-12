#!/bin/bash

# Defina as variáveis que você deseja substituir
USER=$(whoami)  # Nome do usuário atual
GROUP=$(id -gn) # Nome do grupo principal do usuário atual
HOME_DIR=$HOME  # Diretório home do usuário
USERID=$(id -u $USER)
PROGRAM_PATH=$(which clipboard-tts-client)

# Caminho para o arquivo de serviço
SERVICE_FILE="/etc/systemd/system/clipboard-tts-client.service"

# Conteúdo do arquivo de serviço (substitua os placeholders)
SERVICE_CONTENT="[Unit]
Description=Clipboard Text-to-Speech Client Program
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
Restart=always
RestartSec=1
User=$USER
Group=$GROUP
Environment=XDG_RUNTIME_DIR=/run/user/$USERID
ExecStart=$PROGRAM_PATH
WorkingDirectory=$HOME_DIR
Environment=\"PATH=$PATH:$HOME_DIR/.local/bin\"

[Install]
WantedBy=multi-user.target
"

# Cria o arquivo de serviço temporário e escreve o conteúdo nele
echo "$SERVICE_CONTENT" | sudo tee $SERVICE_FILE > /dev/null

# Recarga do systemd para reconhecer o novo serviço
sudo systemctl daemon-reload

# Habilitar o serviço para iniciar no boot
sudo systemctl enable clipboard-tts-client.service

# Iniciar o serviço imediatamente
sudo systemctl restart clipboard-tts-client.service



