# Slack Bot #

## Usage ##
This application is designed to be an interface for the picture replication and watermarking script. It allows users to have a way to generate multiple watermarked images without having to request that the admin do this. 

---
### **How we used to do it** ###

Prior to this application, a script was used with a basic command line prompt that would ask: 

> How many copies would you like?
>
> Enter number:

Then the script would copy the image that was in the same directory as the script file.

---

### **How it's done now** ###

First you start by putting an image file in the **`P:\Pictures\Watermark`** directory.

>Also make sure this is the only image in the directory *(later the application will be advanced enough to deal with multiple files)*

Now you can go into the channel ***image_request*** on slack and "@" mention the user `waterboy` followed by text commands. If you say anything to the bot it will present some instructions on how to use it.

Currently the only command available is the `make` command followed by a number which would be the amount of copies you would like.

>Example: `@waterboy` make 100

The bot will now make 100 copies of the image file that is in the above mentioned directory.

After it has finished it will let the user who initiated the command know the task is complete. Now you will see a new directory in the Watermark folder corresponding to the image file name. This new directory should be copied and placed in a another location for safe keeping. Once you have your image folder saved elsewhere you should remove any files left in the Watermark folder.

## Deployment Instructions ##
* Copy the "Slack Bot" folder to the destination server
* Make an environment variable called `SLACK_BOT_TOKEN` and set it's value to the bot users auth token
* Make another environment variable called `BOT_ID` with the user id of the bot user. This can be found by running the ***print_bot_id.py*** script and replacing the `BOT_NAME` variable value with the user name of the bot.
* You can do a test run on the script by executing the following:
>python path/to/slack_bot.py
* If all is working as expected you can put that python process in the background by running the companion `pythonw` exe. Basically just python with a *`w`* appended to the end. Here follows and example:
>pythonw path/to/slack_bot.py

![You can do it](https://media.giphy.com/media/Vccpm1O9gV1g4/giphy.gif)

## Additional Content ##

I've also included a couple of scripts that help with deployment from development to production. The `Deploy-SlackBot.ps1` script is pretty specific to my environment but can be adapted in the meantime to suite other environments.

The other included script `Watch-SlackBot.ps1` is used to log if the bot is still running and restart it if needed. This script depends on a scheduled task called `'Slack Bot'` that has a one time trigger to startup a background `pythonw` process that executes the `slack_bot.py` script. I have another scheduled task that runs the watcher powershell script every ten minutes but can be schedule to run at any desired interval really.

* Deploy-SlackBot.ps1
* Watch-SlackBot.ps1

