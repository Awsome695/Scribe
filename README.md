# Cider-Scribe
a small script(s?) that can use Cider's REST API and Websockets API to retrieve song info and puts them in .txt files, and downloads album art.

## Status
Currently unspaghetti-fying and making a functional optional UI that can enable/disable features: .txt output, album art download, and UI itself. Launch Arguments will also be added in and listed if you would like to not use the UI.

### Current Features
Scribe can currently get info from Cider using either the REST API or the Websockets API, you can choose whichever you would like from the UI or using the respective launch Argument.

Once Scribe retrieves music info it can distribute it via .txt files for each variable, or use it for built in miniplayer (WIP - may not be kept)

Scribe can also download album art with the resolution of choice with a max of 800x800. It is recommended to keep a 1:1 ratio. (I also have no idea if it even can pass 800x800 or do anything other than 1:1 :P )

Thats it for now! I'll keep tweaking this as i need to, feel free to open a PR if youd like to contribute, recommend a feature or report a bug!
# :D