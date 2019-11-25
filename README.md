# CtfCtrl

A very naive implementation of an automated CTF-setup.

## TLDR
Spins up a CTFd- and several JuiceShop-instances on free Heroku dynos.
Then pings every instance once every 15 minutes to keep the dynos alive.
Eventually, all instances can be shut down.

## Dependencies
Install ctf-cli via `npm install -g juice-shop-ctf-cli`.
You'll need the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).

## Setting up your own CTF

### Scoreboard (CTFd)

Update the key in config.yml (maybe run `echo $RANDOM | md5` in a shell to generate a random key?) and run `juice-shop-ctf --config config.yml`.

The automated way: `./ctfctrl config` to generate a config for you.

You can then go to [this fork of CTFd](https://github.com/EivindArvesen/CTFd) and click the "Deploy to Heroku"-button.
Call the app something you'll remember (like "bouvet-ctfd"), and choose the region nearest you ("Europe"?), then click "Deploy app" - keeping the defaults for the rest of the fields.
Deploying the app shouldn't take more than a few minutes.

As soon as the app is deployed, click "Manage App", and then "Open app" (or just go [here](https://bouvet-ctfd.herokuapp.com))

_If you run into a bug where the app is not running, you will have to delete any postgres-instances and clear the env vars related to posgres._

Now:
Name your CTF.
Set your CTF-mode ("team"?).
Click "admin". Click "config". Click "Backup". Click the "import"-tab, and upload the zip-file that you genereated earlier, using juice-shop-ctf.
You will now need to set up the CTF name and admin account again.

### Client Instances

Now you can spin up instances of [Juice Shop](https://github.com/bkimminich/juice-shop)(anywhere, really) using your key as defined in config.yml

The automated way: `./ctfctrl start <number-of-instances>` to deploy randomly named instances to Heroku.

As each instance as of now also has to build on Heroku, each instance will take around 10 minutes. Sorry.

### Let's Go!

After spinning up everything, you should really open up another terminal, and run `./ctfctrl keepup` to continuously ping your scoreboard and every JuiceShop-instance every 15 minutes (in order to not have the Heroku apps die). This is particularly important for the CTFd scoreboard, as all state will be lost if it dies (as it currently writes to sqlite). You can run `./ctfctrl scoreboard` to keep only the scoreboard alive.

Tell your contestants to go to [the CTF Intro Startpage](https://eivindarvesen.github.io/intro-ctf-startpage/)

### Shutting down

When it's all over, run `./ctfctrl stop` to bring down all client instances (JuiceShop).
You'll have to delete the CTFd-app manually on Heroku.