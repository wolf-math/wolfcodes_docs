---
title: Command Line Cheatsheet
sidebar_position: 20
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

# Command Line Cheatsheet

A quick reference guide to the most common command line commands.

## Navigation

### `pwd`

Print working directory - shows your current location.

```bash
pwd
# Output: /Users/username/Documents
```

### `cd`

Change directory - navigate to a different directory.

```bash
cd Documents              # Go to Documents directory
cd ~                     # Go to home directory
cd                       # Go to home directory (shortcut)
cd ..                    # Go up one level
cd ../..                 # Go up two levels
cd /                     # Go to root directory
cd -                     # Go to previous directory
```

### `ls`

List directory contents - shows files and folders in current directory.

```bash
ls                       # List files and directories
ls -l                    # Long format with details
ls -a                    # Show all files including hidden
ls -la                   # Long format with all files
ls -lh                   # Human-readable file sizes
ls -lt                   # Sort by modification time
ls -R                    # Recursive (show subdirectories)
ls *.txt                 # List only .txt files
```

## File Operations

### `cat`

Display file contents - prints entire file to terminal.

```bash
cat file.txt             # Display file contents
cat file1.txt file2.txt  # Display multiple files
cat > newfile.txt        # Create new file (type content, Ctrl+D to save)
cat >> file.txt          # Append to file
```

### `less` / `more`

View file contents page by page - useful for long files.

```bash
less file.txt            # View file (press 'q' to quit, space to scroll)
more file.txt            # View file (older version, less features)
```

### `head`

Display first lines of a file.

```bash
head file.txt            # First 10 lines
head -n 20 file.txt      # First 20 lines
head -n 5 file.txt       # First 5 lines
```

### `tail`

Display last lines of a file.

```bash
tail file.txt            # Last 10 lines
tail -n 20 file.txt      # Last 20 lines
tail -f file.txt         # Follow file (watch for new lines, great for logs)
```

### `touch`

Create empty file or update file timestamp.

```bash
touch file.txt           # Create empty file
touch file1.txt file2.txt # Create multiple files
touch file.txt           # Update modification time if file exists
```

### `cp`

Copy files and directories.

```bash
cp file.txt backup.txt   # Copy file
cp file.txt dir/         # Copy file to directory
cp -r dir1/ dir2/        # Copy directory recursively
cp -v file.txt dir/      # Verbose (show what's being copied)
cp -i file.txt dir/      # Interactive (prompt before overwrite)
```

### `mv`

Move or rename files and directories.

```bash
mv file.txt newname.txt  # Rename file
mv file.txt dir/         # Move file to directory
mv dir1/ dir2/           # Move/rename directory
mv -i file.txt dir/      # Interactive (prompt before overwrite)
```

### `rm`

Remove files and directories.

```bash
rm file.txt              # Delete file
rm -r dir/               # Delete directory recursively
rm -rf dir/              # Force delete directory (no prompts)
rm -i file.txt           # Interactive (prompt before delete)
rm *.txt                 # Delete all .txt files
```

### `mkdir`

Create directories.

```bash
mkdir newdir             # Create directory
mkdir -p dir1/dir2/dir3  # Create nested directories
mkdir dir1 dir2 dir3     # Create multiple directories
```

### `rmdir`

Remove empty directories.

```bash
rmdir emptydir           # Remove empty directory
rmdir dir1 dir2          # Remove multiple empty directories
```

## File Permissions

### `chmod`

Change file permissions.

```bash
chmod 755 file.txt       # Set permissions (rwxr-xr-x)
chmod +x script.sh       # Add execute permission
chmod -x script.sh       # Remove execute permission
chmod u+x file.txt       # Add execute for user only
chmod 644 file.txt       # Common file permissions (rw-r--r--)
chmod 755 script.sh      # Common script permissions (rwxr-xr-x)
```

### `chown`

Change file ownership.

```bash
chown user file.txt      # Change owner
chown user:group file.txt # Change owner and group
chown -R user dir/       # Recursive (change ownership of directory and contents)
```

## Finding Files

### `find`

Search for files and directories.

```bash
find . -name "file.txt"           # Find file by name in current directory
find /home -name "*.txt"          # Find all .txt files in /home
find . -type f -name "*.js"       # Find files only (not directories)
find . -type d -name "node_modules" # Find directories only
find . -size +100M                # Find files larger than 100MB
find . -mtime -7                  # Find files modified in last 7 days
```

### `grep`

Search for text patterns in files.

```bash
grep "pattern" file.txt           # Search for pattern in file
grep -r "pattern" dir/            # Recursive search in directory
grep -i "pattern" file.txt        # Case-insensitive search
grep -n "pattern" file.txt        # Show line numbers
grep -v "pattern" file.txt        # Invert match (show lines without pattern)
grep -l "pattern" *.txt           # Show only filenames with matches
```

### `which`

Find location of executable command.

```bash
which python             # Find where python command is located
which node               # Find where node command is located
which git                # Find where git command is located
```

## Text Processing

### `wc`

Word count - count lines, words, and characters.

```bash
wc file.txt              # Lines, words, characters
wc -l file.txt           # Count lines only
wc -w file.txt           # Count words only
wc -c file.txt           # Count characters only
```

### `sort`

Sort lines of text.

```bash
sort file.txt            # Sort lines alphabetically
sort -r file.txt         # Reverse sort
sort -n file.txt         # Numeric sort
sort -u file.txt         # Unique (remove duplicates)
```

### `uniq`

Remove duplicate lines (must be sorted first).

```bash
uniq file.txt            # Remove consecutive duplicates
sort file.txt | uniq     # Sort then remove duplicates
uniq -c file.txt         # Count occurrences
```

### `cut`

Extract columns from text.

```bash
cut -d',' -f1 file.csv   # Extract first field (comma-delimited)
cut -d':' -f1,3 file.txt # Extract fields 1 and 3 (colon-delimited)
cut -c1-10 file.txt      # Extract characters 1-10
```

### `awk`

Pattern scanning and text processing.

```bash
awk '{print $1}' file.txt         # Print first column
awk -F',' '{print $2}' file.csv   # Print second column (comma-delimited)
awk '/pattern/ {print}' file.txt  # Print lines matching pattern
```

### `sed`

Stream editor for filtering and transforming text.

```bash
sed 's/old/new/g' file.txt        # Replace all occurrences
sed 's/old/new/' file.txt         # Replace first occurrence per line
sed '2d' file.txt                 # Delete line 2
sed -n '2,5p' file.txt            # Print lines 2-5
```

## Redirection and Pipes

### `>`

Redirect output to file (overwrite).

```bash
ls > files.txt           # Save ls output to file
echo "hello" > file.txt  # Write text to file
```

### `>>`

Redirect output to file (append).

```bash
ls >> files.txt          # Append ls output to file
echo "hello" >> file.txt # Append text to file
```

### `<`

Redirect input from file.

```bash
sort < file.txt          # Sort file contents
```

### `|`

Pipe - send output of one command to another.

```bash
ls | grep ".txt"         # List files, filter for .txt
cat file.txt | sort      # Display file, then sort
ps aux | grep python     # List processes, filter for python
```

## Process Management

### `ps`

List running processes.

```bash
ps                       # List your processes
ps aux                   # List all processes
ps aux | grep python     # Find python processes
```

### `top` / `htop`

Monitor system processes and resource usage.

```bash
top                      # Interactive process monitor (press 'q' to quit)
htop                     # Enhanced version (if installed)
```

### `kill`

Terminate processes.

```bash
kill 1234                # Kill process by PID
kill -9 1234             # Force kill process
killall python           # Kill all python processes
```

### `jobs`

List background jobs.

```bash
jobs                     # List background jobs
jobs -l                  # List with PIDs
fg %1                    # Bring job 1 to foreground
bg %1                    # Send job 1 to background
```

### `nohup`

Run command immune to hangups.

```bash
nohup python script.py & # Run script in background, immune to logout
```

## System Information

### `whoami`

Display current username.

```bash
whoami                   # Show your username
```

### `uname`

Display system information.

```bash
uname                    # System name
uname -a                 # All system information
uname -s                 # Operating system name
```

### `df`

Display disk space usage.

```bash
df                       # Disk space for all filesystems
df -h                    # Human-readable format
df -h /                  # Disk space for root filesystem
```

### `du`

Display directory space usage.

```bash
du                       # Current directory size
du -h                    # Human-readable format
du -sh dir/              # Summary of directory size
du -h --max-depth=1      # One level deep
```

### `free` (Linux) / `vm_stat` (macOS)

Display memory usage.

```bash
free -h                  # Linux: memory usage (human-readable)
vm_stat                  # macOS: memory statistics
```

## Network

### `ping`

Test network connectivity.

```bash
ping google.com          # Ping a host (Ctrl+C to stop)
ping -c 4 google.com     # Ping 4 times then stop
```

### `curl`

Transfer data from or to a server.

```bash
curl https://example.com # Download webpage
curl -O https://example.com/file.zip # Download file
curl -o output.txt https://example.com # Save to file
curl -I https://example.com # Show headers only
```

### `wget`

Download files from the web.

```bash
wget https://example.com/file.zip # Download file
wget -O output.zip https://example.com/file.zip # Save with custom name
```

### `ssh`

Secure shell - connect to remote server.

```bash
ssh user@hostname        # Connect to remote server
ssh -p 2222 user@hostname # Connect on custom port
ssh-keygen               # Generate SSH key pair
```

## Compression and Archives

### `tar`

Create and extract archive files.

```bash
tar -czf archive.tar.gz dir/      # Create compressed archive
tar -xzf archive.tar.gz           # Extract compressed archive
tar -xzf archive.tar.gz -C dir/   # Extract to specific directory
tar -tf archive.tar.gz             # List archive contents
```

### `zip` / `unzip`

Create and extract ZIP archives.

```bash
zip archive.zip file1.txt file2.txt # Create ZIP archive
zip -r archive.zip dir/              # Create ZIP archive of directory
unzip archive.zip                    # Extract ZIP archive
unzip -l archive.zip                 # List ZIP contents
```

### `gzip` / `gunzip`

Compress and decompress files.

```bash
gzip file.txt            # Compress file (creates file.txt.gz)
gunzip file.txt.gz       # Decompress file
gzip -d file.txt.gz      # Decompress (alternative)
```

## Git Commands

### `git status`

Show working tree status.

```bash
git status               # Show modified files
git status -s            # Short format
```

### `git add`

Stage files for commit.

```bash
git add file.txt         # Stage specific file
git add .                # Stage all changes
git add -A               # Stage all changes including deletions
```

### `git commit`

Record changes to repository.

```bash
git commit -m "message"  # Commit with message
git commit -am "message" # Add and commit in one step
```

### `git push`

Push commits to remote repository.

```bash
git push                 # Push to remote
git push origin main     # Push to specific branch
```

### `git pull`

Fetch and merge from remote repository.

```bash
git pull                 # Pull latest changes
git pull origin main     # Pull from specific branch
```

### `git clone`

Clone a repository.

```bash
git clone https://github.com/user/repo.git # Clone repository
git clone https://github.com/user/repo.git mydir # Clone to specific directory
```

### `git branch`

List, create, or delete branches.

```bash
git branch               # List branches
git branch new-branch    # Create new branch
git branch -d branch     # Delete branch
```

### `git checkout`

Switch branches or restore files.

```bash
git checkout branch      # Switch to branch
git checkout -b new-branch # Create and switch to new branch
git checkout file.txt    # Restore file from last commit
```

## Package Managers

### `npm` (Node.js)

Node package manager.

```bash
npm install              # Install dependencies
npm install package      # Install package
npm install -g package   # Install globally
npm uninstall package    # Remove package
npm update               # Update packages
npm list                 # List installed packages
```

### `pip` (Python)

Python package installer.

```bash
pip install package      # Install package
pip install -r requirements.txt # Install from requirements file
pip uninstall package    # Remove package
pip list                 # List installed packages
pip freeze > requirements.txt # Save package list
```

### `brew` (macOS)

Homebrew package manager.

```bash
brew install package     # Install package
brew uninstall package   # Remove package
brew update              # Update Homebrew
brew upgrade             # Upgrade packages
brew list                # List installed packages
brew search package      # Search for packages
```

## Useful Shortcuts

### `Ctrl+C`

Cancel/interrupt current command.

### `Ctrl+D`

Exit terminal or end input.

### `Ctrl+L` / `clear`

Clear terminal screen.

### `Ctrl+A`

Move cursor to beginning of line.

### `Ctrl+E`

Move cursor to end of line.

### `Ctrl+U`

Clear line before cursor.

### `Ctrl+K`

Clear line after cursor.

### `Tab`

Auto-complete file/directory names.

### `!!`

Repeat last command.

### `!$`

Last argument of previous command.

### `history`

View command history.

```bash
history                  # Show command history
history | grep "pattern" # Search history
!123                     # Execute command #123 from history
```
