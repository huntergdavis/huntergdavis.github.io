---
layout: post
title: Hacking the Trivial Pursuit - Digial Choice Edition - pt 1 -
date: '2009-10-10 17:58:00'
---


I acquired the Trivial Pursuit – Digital Choice Edition game at a local target for 10$. It’s an interesting little device, with an b&w LCD display, usb out, 16mb internal storage, and the ability to download or create your own questions… on windows only (ouch).. Turns out it’s an interesting device. Here’s what I’ve been able to find out so far.

![hasbro TP digital choice](http://66.147.244.180/~hunterda/content/images/2009/10/041791298fd5_Main4001.jpg)

Plugging it into my spare linux box (trusty old ps3…) I found that the device is recognized, but the partition is not. As it’s only a 16mb partition, it shouldn’t be hard to get a good image. I first copied it straight to a file with `sudo dd if=/dev/sdb of=/home/hunter/Desktop/trivp.img`

I began to browse the interface on the device itself. It begins with a scrolling Trivial Pursuit image, and 2 options, ‘instant play’ and ‘choose and play’. ‘choose and play’ apparently requires registration through the software at www.mytpchoice.com. Might be interesting to see how they package their question format, but first I’ll make an existing device image.

The questions are divided by category ala trivial pursuit the regular game. Selecting a history question, I get “What Beijing locale spent 12 cents per was to remove 600,000 wads of gum in 2002”. Beijing is a pretty unique character sequence, so later on I may search for in the image. Opening the image as a binary in vi with `vi -b trivp.img` showed a sig in the first line, SITRONIXTM. This is the same “fake usb storage” controller used on many lcd photo frames with windows-only drivers. There’s a linux program [here](http://gkall.hobby.nl/dpf018.html) to retrieve the images, I’ll use this as the basis for my interaction with the device.

First you’ll want to load up the tp device as a block device, so we’ll add a sitronix system group with`addgroup --system sitronix`, then add your user and root to that group. You may want to have udev-extras installed. We’ll need to find the usb vendor and product id for the udev rule, so run lsusb. My output looked like ```
<br></br>
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub<br></br>
Bus 005 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub<br></br>
Bus 004 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub<br></br>
Bus 003 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub<br></br>
Bus 002 Device 004: ID 3078:c081<br></br>
Bus 002 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub<br></br>```
  
 So the vendor id is 3078 and the product id is c081. Add the following line to /etc/udev/rules.d/10-personal-rules.rules, allowing us to mount it as a direct block device  
`KERNEL=="sd*[!0-9]", SYSFS{idVendor}=="3078", SYSFS{idProduct}=="c081", SYMLINK+="sitronix", BUS=="usb", NAME="sit_%k", MODE:="0660", GROUP:="sitronix" `  
 You may also need to “sudo modprobe visor” to ensure the rules directory is being watched. Make sure the block device is created with an  
`ls -al /dev/sit*`  
 Mine looked like:  
`brw-rw---- 1 root sitronix 8, 16 2009-10-10 13:19 /dev/sit_sdb `

Now that I knew I had direct block access, I began to look through the image file in a hex editor. At 008fed83, I found `H.a.s.b.r.o. .T.r.i.v.i.a.l. .P.u.r.s.u.i.t. .T.r.i.v.i.a.l. .P.u.r.s.u.i.t..$.......Trivial Pursuit                       0.01..........SITRONIXTM` then a bit later `TP_GAME`. It also looks like there are a lot of ‘‘ characters, probably some XML-like structure. The above blocks are repeated many, many times, so I assume they are the individual question structure. It appears that `SITRONIXTM` is the begining of question structure, and the `H.a.s.b.r.o.` is the end, then it repeats to another block.

From here I copied the first block to a file called question1(from 00000027 to 00007e24). This is a bit easier to work with. I then copy out the second block to a file called question2header (from 00007e24 to 0000BE20). Doing a diff on question1 and question2header revealed the “meat” of the question, a encrypted or compressed bunch of bytes. From here, I’ll load up the windows application, and start to do some reverse engineering if possible.

After loading up the windows application, you plug in the device and it downloads all the questions from the device to your pc. Then it does an “updating your handheld”, whatever that means. A subsequent dd of the block device shows no changes from the previous image. The questions and corresponding keys (encryption keys? answer keys?) are stored in `Application DataHasbroTrivial Pursuit ChoiceMy Questions` and your custom questions are stored (separately) in a folder under that. This is interesting, and may afford us some codebreaking opportunities later.

From error messages, we can deduce category names may be 12 characters total. The combined length of a question and answer together may not be more than 160 characters. This is great, as it tells us that they are using a fixed question size on the device, and there will be some padding (later confirmed). This will simplify things some. First I created a category called aaaaaaaaaaa. I chose 11 because it’s a nice odd numbered prime. A file named aaaaaaaaaaa_(myserialnumber).tpc then appeared in the application data, containing `Wild|My Questions|aaaaaaaaaaaa|en-US|0|1.0`. Next I rebooted into linux to check if the block device had changed. This will tell us if categories are stored in some internal rom or on the fs. The md5 sum remains the same, which means it’s stored not on the block device. Unfortunately, this will preclude any linux client until we snoop the file mapped io commands the windows usb client is sending. On the other hand, we can still get a lot of useful info and perhaps determine the file format and file compression scheme. This would allow windows users to share question libraries between each other and facilitate free online question libraries. Hasbro doesn’t seem to be making any progress on this front so we may need to do it ourselves, as usual.

In the windows interface I wanted to see what types of questions were allowed in the database. Once you have added custom questions through the software interface, they are selectable as categories/questions in the menu selection on the device itself. A 41-character word does not freak it out, nor does a repeating of 50 words. All quotes seems to corrupt its algorithm and appears to reset the question file in windows, but did not transfer to the device. I next created a question 1111 answer 2222. This added a line to the aaaaa.tpc category file. Then I deleted that question, and made another question 2222 answer 1111. A diff comparision should tell us if the encryption/compression algorithm is performed over the question/answer as a pair or one at at time.

The diff is telling. There is a definite eof sequence. It also appears that there may be a symbol table stored alphabetically immediately before the eof sequence, as switching 1111-2222 to 2222-1111 produces the same last set of bytes but switching 3333-4444 does not. A quick matrix of the hex section shows patterns begin to appear (bad news for crypto). ```
<br></br>
1111/2222 =  36 E2 91 6D 7E CB 9D D3 1A AB D3 CE A4 84 BA 69<br></br>
1111/3333 =  17 1D D5 76 A2 76 51 51 EB 9B 40 F8 ED B4 F9 C7<br></br>
2222/1111 =  CF 11 FA A5 2C 87 8B E1 1A AB D3 CE A4 84 BA 69<br></br>
2222/3333 =  3C 79 EA 96 49 B8 47 6C EB 9B 40 F8 ED B4 F9 C7<br></br>
3333/4444 =  A0 C9 ED B1 2F 80 59 DB 85 C6 DF 16 DC 5A C9 33<br></br>
4444/3333 =  7F 5C 6B AE C6 CD 1B 17 EB 9B 40 F8 ED B4 F9 C7<br></br>```

Already you can see that when 3333 is the highest number in a set, the last 16 bytes are always the same. Likewise when 2222 is the highest number in a set, the last 16 bytes are the same. This does not hold true for the 4444 case. This may be a boundary case in the mapping, so I make note of it and continue data collection. Once I’ve created enough pairs of varying sizes and frequencies, I’ll do another post about what I can find out about the compression. If anyone else is interested in this, post up your findings etc and we can get some data, check if the compression is standard across devices, etc.


