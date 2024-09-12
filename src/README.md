# Text to Speech Program

This package provides a text-to-speech client program to interact with the server `text-to-speech-program`.

## 1. Installing

### 1.1. Install the package pip

To install the package from `pypi`, follow the instructions below:


```bash
pip install clipboard-tts-client
```

Execute `which clipboard-tts-client` to see where it was installed, probably in `/home/USERNAME/.local/bin/clipboard-tts-client`.


### 1.2. Add a program to the Linux service

```bash
curl -fsSL https://raw.githubusercontent.com/trucomanx/ClipboardTTSClient/main/install_linux_service.sh | sh
```

After the last code, the program client starts with the operating system.
Now the next commands are accepted (Use them if necessary).

#### 1.2.1. Start service in linux
**You only need to start the program if it has been stopped or is disabled from starting with Linux boot**.

```bash
sudo systemctl start clipboard-tts-client
```

#### 1.2.2. Stop service in linux

```bash
sudo systemctl stop clipboard-tts-client
```

#### 1.2.3. Disable service at linux startup

```bash
sudo systemctl disable clipboard-tts-client
```

## 2. Using

### 2.1. Start the client

If the program was not added to the Linux service, then to start use the command below:

```bash
clipboard-tts-client
```

This starts a server that will listen on `http://127.0.0.1:5000` and will be ready to receive text conversion requests.

## 3. License

This project is licensed under the GPL license. See the `LICENSE` file for more details.
