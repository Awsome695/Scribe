# Scribe
a small script(s?) that can use Cider's Websockets API to retrieve song info and can put them in .txt files, and download album art.
I am in no way, shape, or form, related to the Cider collective at all. this is just a side project i decided to make to test myself.

## Status
Mostly Un-spaghetti-fied, working on figuring out why it doesnt work on Python 3.9 or newer.

### Current Features
* Connect to Cider using Websockets
* Grab and store current Song info to text files, namely Song name, artist, and Album.
* Download and store current song album art

### Planned features
* UI to control features and info grabbed and stored from Cider
* Start, stop, and interval control on info updating
* Resolution choice for downloaded album art

### Current Issues
* Can currently only be started via cmd or terminal, or use an IDE
* Cannot be stopped unless killed by task manager (i've only tested on windows sorry!)
* Requires Python 3.8 (an Issue with threading and how i have it setup probably)

## Requirements
* Python 3.8
* Websockets
* wget
* [Cider](https://cider.sh)

## More info on how Scribe works.
Once Scribe retrieves music info it can distribute it via .txt files for each variable.

Scribe can also download album art with a resolution of 600x600.

Thats it for now! I'll keep tweaking this as i need to, feel free to open a PR if youd like to contribute, recommend a feature or report a bug!
# :D
