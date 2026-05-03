---
slug: adding-stoarge-linux
title: "Adding Storage to a Linux Server"
authors: Aaron Wolf
sidebar_position: 1
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

Maybe you have a home server that you'd like to have some more storage space on. Maybe you have a desktop or laptop that needs more storage. In this tutorial I will show you how to add an HDD or SDD (or even a flash drive) to a Linux computer. 

I'm doing this exercise with a blank flash drive. If you'd also like to practice with a blank flash drive make sure it is unformatted.

#Step 1: Find out the name of your new drive.

Prior to installing the new drive, open the terminal and run `sudo fdisk -l`. There you will see all of the drives and their names. I have a single NVME drive on my laptop, so the output looks like this...

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/s8cpdvsifur3c5oqljop.png)

I have 1 SSD named `/dev/nvme0n1`, with two partitions `/dev/nvme0n1p1` and `/dev/nvme0n1p2` (ignore any `Disk /dev/loop` things you may see).

Physically install the new drive then run `sudo fdisk -l` again to see what's new. Again, ignore any `loop`s you may see. The new drive that wasn't there before is what you should be looking out for.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/2j01ic33vuxresozxx9h.png)

My new drive is called `sdc`. So all of my actions henceforth will be on `sdc`. This drive is completely blank, it is not formatted at all, so I need to format the drive.

#Step 2: Format the Drive (optional if your drive is already formatted)

**Warning: This step will wipe anything that might be on the drive. Skip this step if your drive already has information that you'd like to be available upon mounting.**

In the terminal run `sudo fdisk /dev/sdc` replacing `sdc` with the name of your drive if it's different. You will get the following...

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/qcq3e6slgfoco30s2wrk.png)

Feel free to type `m` to see all the options. First we will create a new partition table. Select `g`. You may get a warning if you're writing over an old partition table. 

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/ljbfbzsvm1ju41ux9s56.png)

Set up a new partition with selection `n`. The prompt asks how many partitions you want and sector sizes. I'm leaving everything to the defaults. If `fdisk` prompts you if you want to remove a signature type `y`.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/xysu44mawmpdy6yi8fm0.png)

Then press `p` to see all your changes, and `w` to write your changes to the disk.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/1b6zvgrcwt4gj6vel19c.png)

If you run `sudo fdisk -l` again you'll see that your changes  were written to the disk. Notice how there's a **1** at the end of `sdc`. This indicates the partition. We will need that for the next step.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/cxy2f027rnqfc1alc0fs.png)

Lastly we will make an `ext4` partition.

`sudo mkfs.ext4 /dev/sdc1`

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/nz9iki3xb51fc1todhyn.png) 

#Step 3: Mount the Drive

Most of the time drives are mounted to `/mnt`, but you can really mount this disk wherever you want. If you want more space in your home directory you'd mount to `/home/[username]/`, replacing `[username]` with whatever user you want to add storage to. I'm (theoretically) working on a server, so I'm mounting my drive to a directory in `/mnt` that I've named `newdir`. I personally think it's good practice to have a directory specific to the drive you want to mount.

This is really easy as all we need to do is...
`sudo mount /dev/sdc1 /mnt/newdir`
or more generally `sudo mount [drive name] [location]`

If we `df -h` we'll see the change.
![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/d9nx4zqa8kymukr1wznh.png)

To unmount the drive we use the `umount` command. 
`sudo umount /mnt/newdir`. The directory will still be there, but the drive and it's contents will be gone.

Again `df -h` will show the change.

#Step 4: Making mounting permanent

If you reboot your machine (assuming you didn't use the `umount` command above) you'll notice that the drive is no longer there. In order to make this a permanent mount you'll need to edit the configuration file `etc/fstab`. This file is read at boot so it knows which drives to mount where. You'll see the root file system already there.

`sudo nano /etc/fstab`. Feel free to use `vi` if you're a snob.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/v9fkng4od8pbwbx3ql0k.png)

Add a new line. You can use spaces or tabs between the values. The first value is the device. The second is the location it should be mounted. The third value is the filesystem type. I'm not entirely sure what `defaults` does, but it always works for me. Google it ¯\_(ツ)_/¯ . The next two numbers refer to read order. 0 0  or 0 1 work best. 
`/dev/sdc1 /mnt/newdir ext4 defaults 0 0`

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/26nfjw8nn7jxdh3zl9a6.png)

**WARNING:** If you make a mistake with the root filesystem your machine will not boot again

**Make sure everything works with the following command**
`sudo mount -a`

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/6vb8h6jqrvanj4n56ieq.png)

If you get no output you're good to go. If however you get a warning make sure to go back and check your work.

#Now you're done.
Enjoy your new expanded storage.