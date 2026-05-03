---
title: Development Setup on MacOS
description: Set up your development environment with GitHub, VS Code, Node.js, Python, and essential tools.
sidebar_label: MacOS Setup
sidebar_position: 1
tags:
  - development setup
  - onboarding
  - environment
  - tools
---


Please **read carefully and execute all commands in order**.


## GitHub Account

1. Create an account: [https://github.com/join](https://github.com/join)
    
2. Add your name + profile picture: [https://github.com/settings/profile](https://github.com/settings/profile)
    
3. Enable **2FA**:  
    [https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa)
    


:::note 🧠 important note on macOS

Closing a window ≠ quitting the app.

Use:

- `Cmd + Q`  
    or
    
- Menu → Quit
:::    


## Command Line Tools

```bash
xcode-select --install
```

If already installed → continue.


## Homebrew

Open the terminal. To install type:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Then: 

```bash
brew --version
```

If you see something like `Homebrew 5.1.0`, then you're fine. 

If you get `command not found` typeL:

```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

Then update and install necessary software:

```bash
brew update
brew upgrade git || brew install git
brew upgrade gh || brew install gh
brew upgrade wget || brew install wget
brew upgrade imagemagick || brew install imagemagick
brew upgrade jq || brew install jq
brew upgrade openssl || brew install openssl
```


## Visual Studio Code

Install VS Code from the terminal:

```bash
brew install --cask visual-studio-code
```

Launch VS Code:

```bash
code
```


## VS Code Extensions

Install the VS Code extensions by typing the following in your terminal:

```bash
code --install-extension ms-vscode.sublime-keybindings
code --install-extension emmanuelbeziat.vscode-great-icons
code --install-extension github.github-vscode-theme
code --install-extension MS-vsliveshare.vsliveshare
code --install-extension dbaeumer.vscode-eslint
code --install-extension esbenp.prettier-vscode
code --install-extension ms-python.python
code --install-extension ms-toolsai.jupyter
code --install-extension ms-python.vscode-pylance
code --install-extension alexcvzz.vscode-sqlite
```


## Disable AI Features (for now)

From the VS Code window:

1. `Cmd + Shift + P`
    
2. Search: `aifeatures`
    
3. Enable **Disable and hide built-in AI features**
    


## Terminal Setup → iTerm2 (Recommended)

The default macOS Terminal is fine… but once you’ve used **iTerm2**, it’s hard to go back.

#### Install iTerm2

```bash
brew install --cask iterm2
```

Launch it:

```bash
open -a iTerm
```

#### Suggested iTerm2 Settings

Inside iTerm2:

Open the settings `⌘` + `,` 

**1. Theme (Dark + readable)**

- Profiles → Colors
- Pick: _“Dracula”_ or _“Solarized Dark”_

**2. Font (important)**

- Profiles → Text
- Font: `MesloLGS NF` (great with Oh My Zsh)

Install the font if needed:

```bash
brew install font-meslo-lg-nerd-font
```

**3. Window size**

- Profiles → Window
- Columns: `200`
- Rows: `50`

**4. Optional but worth it**

- Enable **“Reuse previous session’s directory”**
- Set **Natural Text Editing** (makes word jumping work like VS Code)




## Oh My Zsh

```bash
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

Press `Y` if prompted.


## GitHub CLI (`gh`) Setup (SSH)

We’ll use **GitHub CLI** to connect your machine to GitHub using **SSH**.

This lets you:

- push/pull without passwords    
- avoid token prompts
- use GitHub directly from the terminal
    
### 1. Login with `gh`

Copy and paste the following into your terminal. **DO NOT edit the `email` field**:

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

We use **pyenv** instead of system Python.

#### Install pyenv

From the terminal type:
```bash
brew install pyenv
```

Add to shell:

```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
exec zsh
```

#### Install Python

```bash
pyenv install 3.12.2
pyenv global 3.12.2
```

Check:

```bash
python --version
```


## Python Tools

From the terminal type:
```bash
pip install --upgrade pip
pip install virtualenv pipx
pipx ensurepath
```

Useful tools:

```bash
pip install black flake8 pytest ipython
```


## Node.js (nvm)

Install nvm from the terminal:

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | zsh
exec zsh
```

Check:

```bash
nvm -v
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

From the terminal type:
```bash
brew install sqlite
sqlite3 --version
```


## PostgreSQL

From the terminal type:

```bash
brew install postgresql@15 libpq
brew link --force libpq
brew services start postgresql@15
```

Test:

```bash
psql -d postgres
```

Exit with:

```
\q
```


## Final Check

Check everything manually from the terminal:

```bash
python --version
node -v
npm -v
yarn -v
psql --version
sqlite3 --version
git --version
```
    


## You’re Done!

Your machine is now ready for:

* 🐍 [Python development](../../python/)
* ⚛️ [JavaScript development](../../javascript/)
* 🗄 [SQL Databases](../../sql/)
    
