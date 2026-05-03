---
slug: samba-server-setup
title: "Setting Up Samba Server for File Sharing"
sidebar_position: 2
authors: Aaron Wolf
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---


This is a quick tutorial if you want to set up a home server and have files available to anybody who has access to your wifi or home network. This home server can be _any_ computer; it doesn't need to be a dedicated machine. 

All of my home computers run Linux (because I'm a nerd), so this tutorial covers how to set up Samba on Ubuntu. All the work is done in the terminal.


## Step 1: Install samba

Open the terminal: `ctrl + alt + t`.

`$ sudo apt install samba`

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/4wnviohvm9b4yibc09sj.png)

There's more output, just go with it.

## Step 2: Make sure samba isn't running

`$ sudo service smbd stop`

## Step 3: Rename the current samba configuration file

We're just going to rename the current config file so that if we need it again we still have it, even though you probably won't need it.

`$ cd /etc/samba`
`$ sudo mv smb.conf smb.conf.old`

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/gnc71kdqmk681cfpwath.png)

## Step 4: Edit the config file

Well, since we renamed the original config file one we're going to create a new one in nano (feel free to use vi if you're a snob).

`$ sudo nano smb.conf`

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/te0zgla36wtac4gkcsgq.png)

`server string` is just a description of your server. `workgroup` is the name of your work group. These two can be whatever you want. The next 3 lines are just for quick easy settings (no passwords needed etc...).

## Step 5: Edit the samba shares

We're still editing `/etc/samba/smb.conf`, but I thought this deserved its own step. 

You can make as many samba shares as you want. I have a documents directory that I want anybody to have access to. I'll also add the music folder from my plex server. What you put in [Square Brackets] will be the name of the folder/directory everyone sees on the network.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/51jbvhx88w3a0cz8c5ut.png)

`force user` must be the user **of the server**, otherwise you may get a username and password prompt.

`path` is (obviously) the path to the shared directory.

If `writable = no` that means that nobody can make changes to this directory. Set to `yes` if you want others to be able to change it. This gives full CRUD abilities on your server to anyone who can access your wifi or home network.

`public = yes` so that everyone can see it!

Here's a picture of the whole file:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/nhz68oy1ul5rip1lgj3s.png)

Hit `ctrl-O` to save (and `enter`), then `ctrl-X` to exit nano.

## Step 6: Check your work.

Just like your math teacher used to tell you. (I used to be a math teacher, can you tell?)

`$ testparm`

What you'll see is a bunch of stuff. If you see what you just typed everything should be ok!

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/oq1whysbtnqvbr72k3ag.png)

## Step 7: Start the samba service

`$ sudo service smbd start`

## Step 8: Enjoy your samba server

Now you can go into your computer's filesystem and check out your cool stuff!

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/aja1wrmv9qxt4914axni.png)

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/bzgikogqdynny1foh2z5.png)

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/2cudcdyrd7d377lrdg4z.png)

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/06pm7y7kbu1k2gcd4c6d.png)


