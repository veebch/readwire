# Read-Wire

![Action Shot](/images/actionshot1.jpg)

[![YouTube Channel Views](https://img.shields.io/youtube/channel/views/UCz5BOU9J9pB_O0B8-rDjCWQ?style=flat&logo=youtube&logoColor=red&labelColor=white&color=ffed53)](https://www.youtube.com/channel/UCz5BOU9J9pB_O0B8-rDjCWQ) [![Instagram](https://img.shields.io/github/stars/veebch?style=flat&logo=github&logoColor=black&labelColor=white&color=ffed53)](https://www.instagram.com/v_e_e_b/)

A script to be run after an Amazon Kindle is connected to a computer via USB. It makes a copy of the clippings file from the kindle to the current working directory on the machine, as well as producing a cleaned up (duplicates removed) tsv file of them.

Once you've got your clippings, you can do stuff with them (see photo for example). 

The benefit of using the direct device approach (rather than the Amazon cloud service) is that **your device also contains highlights for books that you did not purchase via the Amazon store**.

# Prerequisites

Make sure:
- That your machine is automounting USB drives,
- You are running a Terminal of some sort.

Currently, this has only been tested on Linux, but *should* work on MacOS and Windows.

# Installation

```
git clone https://github.com/veebch/readwire.git
cd readwire
```

# Running

`python3 monitor.py`

If all goes well, your clippings are now locally stored in a file called `My_Clippings.txt` ready to be used in whatever way you find useful.

# To Do

Add `udev` instructions so the script is automatically triggered whenever a kindle is connected

