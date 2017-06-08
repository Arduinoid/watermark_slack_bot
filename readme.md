# Slack Bot #

## Usage ##
This application is designed to be an interface for the picture replication and watermarking script. It allows users to have a way to generate multiple watermarked images without having to request that the admin do this. 

---
### **how we used to do it** ###

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

After it has finished it will let you know the task is complete. Now you will see a new directory in the Watermark folder that should be copied and placed in the corresponding folder. Once you have your images you should remove any files left in the Watermark folder.

## Deployment Instructions ##
* Copy the "Slack Bot" folder to the destination server
* Make an environment variable called `SLACK_BOT_TOKEN` and set it's value to the bot users auth token
* Make another environment variable called `BOT_ID` with the user id of the bot user. This can be found by running the ***print_bot_id.py*** script and replacing the `BOT_NAME` variable with the user name of the bot.

![You can do it](https://media.giphy.com/media/Vccpm1O9gV1g4/giphy.gif)