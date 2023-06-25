## Prerequisites
1. Vivaldi Browser
2. Python with version > 3
3. A functional computer

## Usage
1. Download inject.py
2. Run inject.py with JS as 1st argument, you want to inject
   (e.g. python3 ./inject.py ./WhatsAppCustomCSS.js)
3. Restart Vivaldi and enjoy!

## How it works
Vivaldi does us the favor of injecting two different JS in web panels right from the start:

![](https://raw.githubusercontent.com/jusnim/vivaldi-webpanel-injection/master/media/Vivaldi-Sources-Screenshot.png)

These two are injected by bundle.js
Path: .../Vivaldi/Application/.../resources/vivaldi/bundle.js

So, you can simply replace the string that's injects inject-all-bundle.js with a string that injects inject-all-bundle.js and one another JS, let's call it webpanel.js.

This webpanel.js now starts every time, you launch a webpanel.

## Downsides
One big problem is that bundle.js gets replaced by a newer version after Vivaldi updates. Because of that, its necessary to reinject the script after each update, and thereforw run inject.py again.

I'm not sure if this method will be patched in further versions.
The tested version where it worked is: 6.1.3035.100

## WhatsAppCustomCSS
Currently, I've only used JS injection for Web panels to customize Whatsapp Web, allowing you to narrow the window much further than before.

It's also available in this repo, so feel free to use it :) </br>
![](https://raw.githubusercontent.com/jusnim/vivaldi-webpanel-injection/master/media/WhatAppCustomCSS.png)


## Legal
 The author is not responsible for any illegal use of these programs.<br/>
 I am not accountable for anything you get into.<br/>
 I am not accountable for any of your actions.<br/>
