# CtfCtl

A very naive implementation of an automated CTF-setup.

_ **Note:** This repo will does not neccessarily work any more (based on feedback in 2021). I have no time to provide to support for people that are unable to make it work, but won't exclude that I will look into gettings things up and running again at some point. _

## TLDR
Spins up a CTFd- and several JuiceShop-instances on free Heroku dynos.
Then pings every instance once every 15 minutes to keep the dynos alive.
Eventually, all instances can be shut down.

## Dependencies
Make sure you have [Node.js](https://nodejs.org/en/) installed.

Install ctf-cli via `npm install -g juice-shop-ctf-cli`.

You'll need the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).

## Setting up your own CTF

### Scoreboard (CTFd)

Update the key in config.yml (maybe run `echo $RANDOM | md5` in a shell to generate a random key?) and run `juice-shop-ctf --config config.yml`.

The automated way: `./ctfctl config` to generate a config for you.

You can then go to [this fork of CTFd](https://github.com/EivindArvesen/CTFd) and click the "Deploy to Heroku"-button.
Call the app something you'll remember (like "company-ctfd"), and choose the region nearest you ("Europe"?), then click "Deploy app" - keeping the defaults for the rest of the fields.
Deploying the app shouldn't take more than a few minutes.

As soon as the app is deployed, click "Manage App", and then "Open app".

When the app is up and running, update the `CTFD`-variable in `ctfctl`.

_If you run into a bug where the app is not running, you will have to delete any postgres-instances and clear the env vars related to posgres._

Now:
Name your CTF.
Set your CTF-mode ("team"?).
Click "admin". Click "config". Click "Backup". Click the "import"-tab, and upload the zip-file that you genereated earlier, using juice-shop-ctf.
You will now need to set up the CTF name and admin account again.

### Client Instances

Now you can spin up instances of [Juice Shop](https://github.com/bkimminich/juice-shop) (anywhere, really) using your key as defined in config.yml

The automated way: `./ctfctl start <number-of-instances>` to deploy randomly named instances to Heroku.

As each instance as of now also has to build on Heroku, each instance will take around 10 minutes. Sorry.

### Let's Go!

After spinning up everything, you should really open up another terminal, and run `./ctfctl keepup` to continuously ping your scoreboard and every JuiceShop-instance every 15 minutes (in order to not have the Heroku apps die). This is particularly important for the CTFd scoreboard, as all state will be lost if it dies (as it currently writes to sqlite). You can run `./ctfctl scoreboard` to keep only the scoreboard alive.

Tell your contestants to go to [the CTF Intro Startpage](https://eivindarvesen.github.io/intro-ctf-startpage/)

### Shutting down

When it's all over, run `./ctfctl stop` to bring down all client instances (JuiceShop).
You'll have to delete the CTFd-app manually on Heroku.
