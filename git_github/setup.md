---
title: Connecting Git to GitHub
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

This guide shows you how to connect a **local Git repository** to **GitHub** using the terminal.

It assumes you:

- Have Git installed and configured on your machine
- Are comfortable running basic terminal commands
- Understand the idea of local vs remote repositories

If those are new concepts, start with the earlier Git guides in this section, then come back here.

## Why use Git and GitHub?

Git and GitHub provide essential tools for modern software development:

* **Version control**: Track changes to your code over time, making it easy to see what changed and when
* **Collaboration**: Multiple people can work on the same project without conflicts
* **Safety**: Create branches to work on features without breaking your main code
* **Backup**: Your code is stored remotely, protecting against local data loss
* **History**: See the complete history of your project and revert to previous versions if needed


## Create a GitHub account

1. Go to [github.com](https://github.com)
2. Click "Sign up" in the top right corner
3. Follow the prompts to create your account
4. Verify your email address when prompted

## Install `gh` (GitHub CLI)

The GitHub CLI (`gh`) makes it easy to authenticate and work with GitHub from the command line. This requires using the terminal to install and run commands.

If you're new to the command line, start with the [command line basics guide](/docs/command_line/what_it_is).

### Open your terminal

Before installing, open your terminal application:

**macOS:**
- Press `Cmd + Space` to open Spotlight
- Type "Terminal" and press Enter
- Or go to Applications → Utilities → Terminal

**Linux:**
- Press `Ctrl + Alt + T` (most distributions)
- Or search for "Terminal" in your applications menu
- Common names: Terminal, Konsole, GNOME Terminal

**Windows:**
- Press `Windows + X` and select "Windows PowerShell" or "Terminal"
- Or press `Windows + R`, type `powershell`, and press Enter
- Or search for "PowerShell" or "Command Prompt" in the Start menu
- Windows Terminal (recommended) can be installed from the Microsoft Store

Once you have your terminal open, you'll use commands like `cd` and `mkdir`. Learn more about [navigating files and directories](/docs/command_line/files_directories).

### macOS

```bash
brew install gh
```

### Linux

```bash
# Debian/Ubuntu
sudo apt install gh

# Fedora
sudo dnf install gh

# Arch Linux
sudo pacman -S github-cli
```

### Windows

```bash
# Using winget
winget install --id GitHub.cli

# Or using Chocolatey
choco install gh

# Or download from: https://cli.github.com/
```

After installation, verify it works:

```bash
gh --version
```

## Configure GitHub authentication

1. Run the authentication command:
   ```bash
   gh auth login
   ```

2. Follow the interactive prompts:
   - Select `GitHub.com`
   - Choose `SSH` as your preferred protocol
   - When asked for your SSH key, select the default option (usually `/Users/<computer_username>/.ssh/id_ed25519.pub` on macOS/Linux, or `C:\Users\<computer_username>\.ssh\id_ed25519.pub` on Windows)
   - If you don't have an SSH key, `gh` will help you generate one

3. Complete the browser authentication:
   - A security code will be displayed in your terminal
   - Your default browser will open automatically
   - Paste the security code into the browser
   - Authorize GitHub CLI to access your account

4. Verify authentication:
   ```bash
   gh auth status
   ```

You're all set! Your SSH key is now configured and you can push and pull without entering credentials each time.

### Why use SSH?

SSH (Secure Shell) keys provide a more secure and convenient way to authenticate with GitHub:

* **Security**: Your credentials are saved securely on your computer, not transmitted with each request
* **Convenience**: No need to log in with a password at each push or pull
* **Best practice**: SSH is the recommended authentication method for GitHub

## Create your first repository

1. On GitHub.com, click the `+` button in the top right corner
2. Select "New repository"
3. Fill in the repository details:
   - **Repository name**: Choose a descriptive name (e.g., `my-first-project`)
   - **Description**: Optional, but helpful for others to understand your project
   - **Visibility**: Choose Public (visible to everyone) or Private (only you can see it)
   - **Initialize repository**: You can skip this since we'll add files manually
4. Click "Create repository"

## Prepare your local code

1. Create a directory for your project:
   ```bash
   mkdir -p ~/code/<repo_name>
   cd ~/code/<repo_name>
   ```
   Replace `<repo_name>` with your actual repository name.

2. Initialize Git in this directory:
   ```bash
   git init
   ```

3. Create a test file:
   ```bash
   touch test_file.txt
   ```
   Or create any file you want to track.

## Add, commit, and push

Now you'll connect your local repository to GitHub and push your code:

1. **Stage your files** (tell Git which files to include):
   ```bash
   git add .
   ```
   This adds all files in the current directory. You can also add specific files: `git add test_file.txt`

2. **Create your first commit** (save a snapshot of your code):
   ```bash
   git commit -m "first commit"
   ```
   The `-m` flag lets you add a message describing what this commit does.

3. **Rename the branch to `main`** (GitHub's default branch name):
   ```bash
   git branch -M main
   ```
   This ensures your local branch matches GitHub's naming convention.

4. **Connect to your GitHub repository**:
   ```bash
   git remote add origin git@github.com:<username>/<repo_name>.git
   ```
   Replace `<username>` with your GitHub username and `<repo_name>` with your repository name. This will be shown on the GitHub repository page.

5. **Push your code to GitHub**:
   ```bash
   git push -u origin main
   ```
   The `-u` flag sets up tracking so future pushes can be done with just `git push`.

Refresh your GitHub repository page—you should see your files!

## Next steps

Now that you have GitHub set up, you can:
- Make changes to your files locally
- Use `git add .` and `git commit -m "your message"` to save changes
- Use `git push` to upload your changes to GitHub
- Create branches to work on new features safely
- Collaborate with others by sharing your repository
