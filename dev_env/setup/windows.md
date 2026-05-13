---
title: Development Setup for Windows
description: Set up your development environment on Windows using WSL, GitHub, VS Code, Node.js, Python, and essential tools.
sidebar_label: Windows Setup
sidebar_position: 2
tags:
  - development setup
  - onboarding
  - windows
  - wsl
  - environment
---


Please **read carefully and execute all commands in order**.

👉 We will use **WSL (Windows Subsystem for Linux)** so your environment behaves like macOS/Linux.


## GitHub Account

1. Create an account: [https://github.com/join](https://github.com/join)
2. Add your name + profile picture: [https://github.com/settings/profile](https://github.com/settings/profile)
3. Enable **2FA**



## Install WSL (Linux on Windows)

:::note important note on WSL
Windows and WSL are two different environments.

- Windows = your operating system
- WSL = a Linux machine inside Windows

👉 From this point forward, we will do all development inside WSL
:::

Open **PowerShell (as Administrator)** and run:

```powershell
wsl --install
```

Restart your computer when prompted.


#### Launch WSL

Open **Ubuntu** from the Start Menu.

You’ll be asked to:

* create a username
* create a password

👉 This is your Linux environment.


:::note note

From now on:

👉 **All commands run inside the WSL (Ubuntu) terminal**

NOT in PowerShell or Command Prompt.
:::

## Update system packages

Inside WSL:

```bash
sudo apt update && sudo apt upgrade -y
```


## Install essential tools

```bash
sudo apt install -y build-essential curl file git
```

## Oh My Zsh

Copy and paste the commands to WSL:

```bash
sudo apt install zsh -y
```

then,

```bash
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

Press `Y` if prompted.


## Visual Studio Code

Install for Windows:

👉 [https://code.visualstudio.com](https://code.visualstudio.com)


#### Install WSL Extension

Open VS Code → Extensions → install:

* **Remote - WSL**


#### Open VS Code from WSL

Inside WSL terminal:

```bash
code .
```

👉 This connects VS Code to Linux automatically


## VS Code Extensions

Run inside WSL terminal:

```bash
code --install-extension dbaeumer.vscode-eslint
code --install-extension esbenp.prettier-vscode
code --install-extension ms-python.python
code --install-extension ms-python.vscode-pylance
code --install-extension ms-toolsai.jupyter
code --install-extension alexcvzz.vscode-sqlite
```


## Disable AI Features (for now)

Open VS Code:

1. `Ctrl + Shift + P`
2. Search: `aifeatures`
3. Enable **Disable and hide built-in AI features**



## GitHub CLI (`gh`) Setup (SSH)

Copy and paste these command into WSL:

```bash
sudo apt install gh -y
```

### 1. Login with `gh`

Login. **DO NOT edit the `email`** field:

```bash
gh auth login -s 'user:email' --git-protocol ssh -w
```

### 2. You’ll be asked a few questions:

#### “What account do you want to log into?”

- Choose: `GitHub.com`

#### “What is your preferred protocol?”

- Use the arrow keys to choose: `SSH`

Why?

- No passwords when pushing
- More stable long-term workflow

#### “Generate a new SSH key?”

- Press `Enter` (Yes)

👉 If you already have a key:

- Select your existing key instead

#### “Enter a passphrase”

- Optional, but recommended if you're security conscious 
- This protects your key if your machine is compromised
- Press `enter` with the field blank to proceed without a passphrase

#### “Title for your SSH key”

- Default is fine (e.g. `GitHub CLI`), press `enter`

### 3. Browser authentication

You’ll see:

```bash
! First copy your one-time code: XXXX-XXXX
```

- Copy the code
- Press `Enter`
- Browser opens → paste code → approve access
    
👉 This creates a secure auth token stored locally ([GitHub CLI](https://cli.github.com/manual/gh_auth_login?utm_source=chatgpt.com "gh auth login"))

### 4. Verify everything worked

```bash
gh auth status
```

You should see:
```bash
✓ Logged in to github.com as <your-username>
```


## Python (pyenv)

Install dependencies:

```bash
sudo apt install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev llvm libncurses5-dev \
libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev
```

Install pyenv:

```bash
curl https://pyenv.run | bash
```

Add to shell:

```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
exec bash
```

Install Python:

```bash
pyenv install 3.12
pyenv global 3.12
```

Check:

```bash
python --version
```


## Python Tools

```bash
pip install --upgrade pip
pip install virtualenv pipx
pipx ensurepath
```


## Node.js (nvm)

Install nvm:

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
exec bash
```

Install Node:

```bash
nvm install 20
nvm use 20
```

Check:

```bash
node -v
npm -v
```


## SQLite

```bash
sudo apt install sqlite3 -y
sqlite3 --version
```


## PostgreSQL

```bash
sudo apt install postgresql postgresql-contrib -y
```

Start service:

```bash
sudo service postgresql start
```

Test:

```bash
psql -U postgres
```

Exit:

```
\q
```


## Final Check

```bash
python --version
node -v
npm -v
psql --version
sqlite3 --version
git --version
```

## You’re Done!

Your machine is now ready for:

* 🐍 [Python development](../../python/)
* ⚛️ [JavaScript development](../../javascript/)
* 🗄 [SQL Databases](../../sql/)

👉 All running inside Linux (WSL)



