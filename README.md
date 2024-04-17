# Read-Wire

![Action Shot](/images/actionshot1.jpg)

[![YouTube Channel Views](https://img.shields.io/youtube/channel/views/UCz5BOU9J9pB_O0B8-rDjCWQ?label=YouTube&style=social)](https://www.youtube.com/channel/UCz5BOU9J9pB_O0B8-rDjCWQ) [![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=social&logo=instagram&logoColor=black)](https://www.instagram.com/v_e_e_b/)

A script to be run after an Amazon Kindle is connected to a linux computer via USB. It makes a copy of the clippings file from the kindle to the current working directory on the machine.

Once you've got your clippings, you can do stuff with them (see photo for example). 

The benefit of using this approach (rather than the Amazon cloud service) is that your device also contains highlights for books that you did not purchase via the Amazon store.

# Prerequisites

Make sure that your machine is automounting USB drives

# Installation

```
git clone https://github.com/veebch/readwire.git
cd readwire
```

# Running

`python3 monitor.py`

If all goes well, your clippings are now locally stored in a file called `My_Clippings.txt` ready to be used in whatever way you find useful.

# To Do

Add `udev` instructions so the script is automatically triggered on connection

