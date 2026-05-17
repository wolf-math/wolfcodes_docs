---
title: Linux Filesystem Layout
sidebar_position: 1
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

The Linux filesystem layout is the directory structure Linux uses to organize user files, system configuration, installed software, logs, devices, and temporary data. If you use Linux from the terminal, the top-level directories are worth learning because they tell you what kind of path you are looking at and how carefully you should treat it.

If you want a refresher on paths and directory trees in general, read [Files and Directories](/docs/command_line/files_directories) first. This page is a Linux-specific overview.

## What is the Linux filesystem layout?

Linux organizes everything under a single root directory: `/`.

```text
/
├── bin
├── boot
├── dev
├── etc
├── home
├── lib
├── media
├── mnt
├── opt
├── proc
├── root
├── run
├── sbin
├── srv
├── sys
├── tmp
├── usr
└── var
```

You do not need to memorize every path immediately. What matters is recognizing the role of the major directories.

## Why this matters

When you use Linux from the command line, paths often tell you what kind of work you are doing.

- A path under `/home` usually means user-owned files
- A path under `/etc` usually means system configuration
- A path under `/var` usually means changing system data such as logs or service state
- A path under `/usr` usually means installed software or shared system resources
- A path under `/dev`, `/proc`, or `/sys` often means devices or live system information rather than ordinary files

That mental model makes Linux much easier to navigate.

## Important top-level directories

### `/`

`/` is the root of the entire filesystem tree. Every other directory exists somewhere under it.

This is not the same as `/root`.

### `/home`

`/home` usually contains the home directories for normal users.

Examples:

- `/home/alice/projects`
- `/home/alice/.bashrc`
- `/home/alice/.ssh`

This is where most personal files and day-to-day user work live.

### `/root`

`/root` is the home directory for the root user.

This is a common point of confusion:

- `/` is the root of the filesystem
- `/root` is root's personal home directory

### `/etc`

`/etc` holds system-wide configuration files.

Examples:

- `/etc/fstab`
- `/etc/hosts`
- `/etc/ssh/sshd_config`

If you are configuring a service or changing system behavior, there is a good chance the relevant file lives somewhere under `/etc`.

### `/var`

`/var` holds changing system data.

Common subdirectories include:

- `/var/log` for logs
- `/var/lib` for service and application state
- `/var/cache` for cached data
- `/var/tmp` for temporary files that may live longer than files in `/tmp`

If `/etc` is where the system is configured, `/var` is often where the system changes over time.

### `/usr`

`/usr` holds many installed programs, shared libraries, documentation files, and shared resources.

Common subdirectories include:

- `/usr/bin`
- `/usr/sbin`
- `/usr/lib`
- `/usr/share`

In practice, many commands you run live somewhere under `/usr/bin` or `/usr/sbin`.

### `/bin` and `/sbin`

These directories traditionally hold essential system commands.

On many modern systems, they may be linked into directories under `/usr`.

The important thing to know is not the historical distinction. It is that these paths contain core executables.

### `/tmp`

`/tmp` is used for temporary files.

Programs and scripts often write scratch files here. Files in `/tmp` may be deleted automatically, especially after a reboot.

### `/mnt` and `/media`

These are common mount locations.

Typical use:

- `/mnt` for manual or temporary mounts
- `/media` for removable drives managed by the system

### `/dev`

`/dev` contains device files that represent hardware and virtual devices.

Examples:

- `/dev/sda`
- `/dev/sdb1`
- `/dev/nvme0n1`
- `/dev/null`

This directory matters most when working with disks, partitions, terminals, and other devices.

### `/proc` and `/sys`

These are special virtual filesystems.

- `/proc` exposes process and kernel information
- `/sys` exposes device and kernel state in a structured way

They are part of the filesystem tree, but they do not behave like ordinary saved files on disk.

### `/boot`

`/boot` contains files needed for the boot process, such as the kernel and bootloader-related data.

This directory is important when dealing with boot configuration, kernels, or some system recovery tasks.

### `/opt`

`/opt` is commonly used for optional or third-party software that is installed outside the normal package layout.

You will not use it every day, but it is useful to recognize when software places files there.

### `/srv`

`/srv` is intended for data served by the system.

Examples might include files for a web server, FTP server, or other service-managed content.

Not every system uses it heavily, but the name is worth recognizing.

### `/run`

`/run` holds runtime state for the current boot session.

It often contains things like:

- PID files
- sockets
- lock files
- temporary service state

Unlike normal persistent data directories, `/run` is for live runtime information.

## One tree, many filesystems

Linux presents everything as one directory tree, even when multiple filesystems are involved.

That means:

- `/` may be one filesystem
- `/boot` may be another
- `/home` may be another
- a removable drive may be mounted under `/media`

From the terminal, they still appear as one unified hierarchy rooted at `/`.

This is one reason Linux filesystem knowledge is more than just memorizing folder names.

## Summary

The Linux filesystem layout gives you a map for understanding paths.

The main ideas to remember are:

- everything lives under `/`
- top-level directories have different jobs
- `/home`, `/etc`, `/var`, and `/usr` are the most important directories to recognize early
- `/dev`, `/proc`, and `/sys` are special parts of the tree
- one visible directory tree can include many mounted filesystems

If you can look at a path and make a good first guess about whether it is user data, system config, installed software, logs, or device-related state, this overview has done its job.
