# clipboard-tts-client

Program that collects text from clipboard and converts it to speech using tts-program-server.

## Install from source
Installing text-to-speech client program

```bash
git clone https://github.com/trucomanx/ClipboardTTSClient.git
cd ClipboardTTSClient
pip install -r requirements.txt
cd src
python3 setup.py sdist
pip install dist/clipboard_tts_client-*.tar.gz
```

## Add a program to the Linux start session
Adding client GUI program to Linux start session (`~/.config/autostart/clipboard-tts-client.desktop`)

```bash
curl -fsSL https://raw.githubusercontent.com/trucomanx/ClipboardTTSClient/main/install_linux_program_session.sh | sh
```

Adding bar indicator to Linux start session (`~/.config/autostart/clipboard-tts-indicator.desktop`)

```bash
curl -fsSL https://raw.githubusercontent.com/trucomanx/ClipboardTTSClient/main/install_linux_indicator_session.sh | sh
```

## Using


```bash
clipboard-tts-client
```

