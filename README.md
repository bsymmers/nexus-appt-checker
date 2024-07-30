# Nexus Appointment Checker

This Nexus Appointment Checker is a python script that is designed to repeatedly poll the TTP Scheduler API to see if a Nexus appointment spot has opened up. It specifically is meant to work for the Blaine location, but as long as you find the location code for the specific office you're looking to book an appointment out of, it'll work for that as well! It utilizes a discord bot to send the notifications directly to your phone.

## Installation

All you need to do is use pip to install all of the out-of-the-box dependencies listed at the top of the script as imports (ie discord). To create the discord bot and channel see discord's documentation on how to do so. 


## Usage

Since this script is constantly polling the TTP Scheduler API, it's designed to run on a server constantly. I let it sleep at night since I'm not awake to book said appointments. You will have to set up IP rotation on your server as the TTP Scheduler API does have rate limiting and you will get 403's if you don't!


## License

[MIT](https://choosealicense.com/licenses/mit/)
