---
title: Linux Style Guide
sidebar_position: X
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

# Linux style guide

Use this guide when writing or revising pages in `docs/linux`.

The Linux section should be explicitly CLI-first. It is not a general “what is Linux?” section, and it is not just a collection of old server notes. Its job is to teach readers how to understand, inspect, configure, and maintain a Linux system from the command line.

This section should pair naturally with `docs/command_line`:

- `docs/command_line` teaches shell mental models and cross-platform CLI concepts
- `docs/linux` shows how those skills are used on a real Linux machine

Every page in `docs/linux` should answer some version of:

- What Linux system concept or task is this page about?
- What can the reader inspect safely before making changes?
- Which commands are involved?
- What does each command do?
- How can the reader verify that it worked?
- What mistake could break something if they rush?

## Frontmatter

Use the standard frontmatter on every Linux page:

```md
---
title: Concept Name
sidebar_position: X
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---
```

- `title` should be literal, practical, and easy to scan in the sidebar.
- `sidebar_position` controls the order within the Linux section.
- Keep author, license, and source metadata consistent.
- Do not add extra metadata unless the surrounding section requires it.

For hub pages such as `index.mdx`, use `sidebar_label` when it helps navigation consistency.

## Core identity

Linux guides in this section should be:

- CLI-first
- practical
- safe
- stepwise
- explicit about verification
- honest about risk

These pages should feel like calm operational guides, not blog posts and not abstract overviews.

Prefer:

```md
Before changing `/etc/fstab`, inspect the current mounts and identify the device by UUID.
```

Avoid:

```md
Linux is powerful and flexible, so there are many ways to think about storage configuration.
```

## What belongs in `docs/linux`

Good Linux topics for this section:

- filesystem layout in practice
- users, groups, and `sudo`
- package management with `apt`
- processes and signals
- services with `systemctl`
- logs with `journalctl`, `tail`, and `less`
- disks, partitions, filesystems, and mounts
- networking with commands like `ip`, `ss`, `ping`, and `curl`
- SSH and remote administration
- editing config files in `/etc`
- backup, file sharing, or home-server tasks done from the terminal

Topics that do not fit as well:

- GUI walkthroughs as the main approach
- broad Linux history or distro-comparison essays
- command-line basics already taught in `docs/command_line`
- highly distro-specific workflows unless the page says so clearly
- copy-paste recipes with no explanation or verification

## Core principle

Teach inspection before modification.

Most Linux mistakes happen when a reader changes a system they do not yet understand. So the default flow should be:

1. Identify what is there now
2. Explain what the reader is looking at
3. Make the smallest necessary change
4. Verify the result
5. Note how to recover or what to check if it failed

This matters especially for:

- storage
- mounts
- boot configuration
- permissions
- networking
- services
- anything under `/etc`

## Page types

Most pages in `docs/linux` should fit one of these shapes.

### Concept guides

Use concept guides for topics like filesystems, `systemd`, permissions, logs, or Linux directory structure.

Use this shape:

1. `## What is [concept]?`
2. `## Why this matters`
3. `## Safe inspection commands`
4. `## How the concept behaves in practice`
5. Common commands, variations, or workflows
6. Important caveats or gotchas
7. `## Summary` for substantial pages

Examples:

- Linux filesystem layout
- Users and groups
- How services work
- Reading logs

### Task guides

Use task guides for practical system jobs such as mounting a disk, enabling a service, or setting up SSH.

Use this shape:

1. Short opening paragraph naming the task
2. `## Before you begin`
3. `## Inspect the current system`
4. `## Make the change`
5. `## Verify the result`
6. `## Common problems`
7. `## Summary` when the guide is substantial

Examples:

- Mounting a new disk
- Enabling a service at boot
- Connecting over SSH
- Installing software with `apt`

### Troubleshooting guides

Use troubleshooting pages when the reader is likely arriving with a broken system state or confusing symptoms.

Use this shape:

1. Short framing paragraph naming the symptom
2. `## What this usually means`
3. `## Check these commands first`
4. `## Common causes`
5. `## How to fix each cause`
6. `## How to verify the fix`

These pages should be especially concrete and command-centered.

## Default structure

There is no rigid template, but most Linux guides should roughly follow this order:

1. What this concept or task is
2. Why it matters on a Linux system
3. Safe inspection commands
4. The actual change or workflow
5. Verification commands
6. Common mistakes or recovery notes
7. Summary or next steps

Always move from low-risk understanding to higher-risk action.

## Headings

Use sentence-style headings that sound operational and concrete.

Good headings:

```md
## What is `systemctl`?
## Why this matters
## Inspect the current mounts
## Create the filesystem
## Mount the device
## Verify the service status
## Common problems
## Summary
```

Less effective headings:

```md
## Linux stuff
## Additional notes
## Example usage
## Step 1
## Miscellaneous
```

Use backticks in headings for exact commands, files, directories, flags, unit names, and config entries:

```md
## Editing `/etc/fstab`
## Using `journalctl`
## Checking `systemctl status`
### `lsblk`
### `mount -a`
### `ss -tulpn`
```

Prefer task-based headings over generic headings whenever possible.

## Openings

Most pages should open with a short paragraph that:

- names the Linux concept or task
- says why it matters
- makes it clear that the workflow is terminal-based

Example:

````md
Mounting a disk on Linux means attaching a filesystem to the directory tree so the system can use it. In practice, this usually involves identifying the device, checking its filesystem, choosing a mount point, mounting it, and verifying the result from the terminal.
````

For concept pages:

````md
`systemctl` is the main command-line tool for managing services on Linux systems that use `systemd`. You will use it to check service status, start and stop services, and control whether they launch at boot.
````

## Command examples

Command examples are the center of this section.

Good command examples are:

- short enough to scan
- realistic enough to use
- focused on one idea
- followed by an explanation of what the command does
- paired with verification commands when the command changes the system

Use `bash` fences:

````md
```bash
lsblk -f
```
````

When output matters, include it:

````md
```bash
systemctl status ssh
```

**Example output:**

```text
● ssh.service - OpenBSD Secure Shell server
     Active: active (running)
```
````

When a command has important flags, explain them immediately after:

```md
`-f` shows filesystem information, which is useful when you need to identify the correct device and mount target.
```

## Explaining commands

Do not drop commands into the page without context.

Every meaningful command should answer at least one of these:

- What does this command inspect?
- What does this command change?
- Why are we using this command instead of another one?
- What output should the reader expect?

Helpful explanation labels:

```md
**What this does:** Shows block devices and their filesystem information.
```

```md
**Why this matters:** This confirms you are about to format the correct device.
```

```md
**Important:** This command will overwrite the existing filesystem.
```

```md
**Verify:** Run the following command after the change.
```

## Verification

Linux guides should almost always include verification, especially after a state-changing command.

Good verification commands include:

- `lsblk`
- `df -h`
- `mount`
- `systemctl status`
- `journalctl -u <service>`
- `ip addr`
- `ss -tulpn`
- `ping`
- `curl`
- `ls -l`

Tell the reader what success looks like.

Prefer:

```md
If this worked, the device should now appear mounted at `/mnt/data` in the output of `df -h`.
```

Avoid:

```md
Now it should be fine.
```

## Safety and risk

Be explicit when a command can break something, delete data, or lock the user out.

Use strong warnings for:

- formatting disks
- editing boot-critical files
- changing permissions recursively
- modifying network config
- restarting remote-access services
- deleting system files
- changing ownership in shared directories

Good warning shape:

```md
**Warning:** `mkfs.ext4` creates a new filesystem and destroys existing data on the target device. Double-check the device name with `lsblk -f` before running it.
```

For risky pages, include a short “safe checkpoint” before the dangerous step:

```md
Before continuing, confirm that the new device is `/dev/sdb` and not your main system disk.
```

## Distro scope

Be clear about distro assumptions.

If a page is written for Ubuntu or Debian-based systems, say so early. If the commands are generally portable, say that too.

Examples:

```md
This guide assumes a Debian-based system with `apt`.
```

```md
These inspection commands work on most modern Linux distributions.
```

Do not pretend every command is universal when it is not.

## Relationship to `docs/command_line`

Do not re-teach shell basics in `docs/linux`.

You can assume the reader may already know:

- what a shell is
- how paths work
- how to run commands with flags
- how pipes and redirection work
- basic file and permission concepts

When relevant, briefly connect back to the command-line guide instead of re-explaining from scratch.

Example:

```md
If paths still feel shaky, read the Command Line guide on files, directories, and paths first. This page assumes you are comfortable reading absolute Linux paths like `/etc/ssh/sshd_config`.
```

## Tone and voice

Use a calm, practical teaching voice.

The tone should be:

- direct
- reassuring
- explicit
- not macho
- not snarky

Avoid the “just run this” sysadmin tone. The reader should feel guided, not tested.

Prefer:

```md
We are checking the current service state first so you can see what changes after the restart.
```

Avoid:

```md
If you know what you're doing, just bounce the service and move on.
```

## Summary of the summary

A strong Linux page in this section should:

- stay CLI-first
- explain inspection before modification
- use real commands
- explain what the commands do
- show how to verify success
- call out risky steps clearly
- stay practical and operational

If a page reads like a blog post, a GUI walkthrough, or a command dump with no explanation, revise it.
