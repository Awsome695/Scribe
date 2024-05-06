import json
import time
import asyncio
import websockets

# urls | change this if cider ever changes this for some reason :/
cider_websocket_url = 'ws://localhost:10766/ws'

count = 0
data = ""

# variables to store cider values
# json
fixed_json_data = {}
data_json_data = {}
# song info
song_name = ""
song_artist = ""
song_album = ""
song_link = ""
artwork_link = ""
artwork_height = int
artwork_width = int
current_playback_time = float
duration_in_ms = float
# websockets specific values
type_data = str
# stores mode
mode = ""


def set_mode(arg):
    global mode
    mode = arg


def return_vars(variable):
    global song_name, song_artist, song_album, song_link, artwork_link
    if variable == "song_name":
        return song_name
    if variable == "song_artist":
        return song_artist
    if variable == "song_album":
        return song_album
    if variable == "song_link":
        return song_link
    if variable == "type_data":
        return type_data
    if variable == "artwork_link":
        return artwork_link
    

def update_vars(json_data, mode):
    global type_data, data_json_data, song_name, song_artist, song_album, song_link, artwork_width, artwork_height, artwork_link
    # extract type
    try:
        type_data = json_data.get("type")
    except Exception as e:
        print(f"type error: {e}")

    # check type to see if a var update needs to be made and if there is, update all OR update all if song name is empty

    if type_data == "playbackStatus.nowPlayingItemDidChange" or song_name == "":
        if mode == "test" or mode == "test+":
            print("song was changed, updating vars....")
        # attempt to update all variables - with errors,
        try:
            data_json_data = json_data.get("data")
        except Exception as e:
            print(f"data_json_data err: {e}")

        try:
            song_name = data_json_data.get("name")
        except Exception as e:
            print(f"song_name failed: {e}")

        try:
            song_artist = data_json_data.get("artistName")
        except Exception as e:
            print(f"song_artist failed: {e}")

        try:
            song_album = data_json_data.get("albumName")
        except Exception as e:
            print(f"song_album failed: {e}")

        try:
            song_link = data_json_data.get("url").get("songLink")
        except Exception as e:
            print(f"song_link failed: {e}")
        
        try:
            artwork_width = data_json_data.get("artwork").get("width")
        except Exception as e:
            print(f"failed to get artwork_width: {e}")
        
        try:
            artwork_height = data_json_data.get("artwork").get("height")
        except Exception as e:
            print(f"failed to get artwork_height: {e}")

        try:
            artwork_link = data_json_data.get("artwork").get("url").format(w=artwork_width, h=artwork_height)
        except Exception as e:
            print(f"failed to get artwork_link: {e}")
        
    else:
        if mode == "test" or mode == "test+":
            print("something else changed: " + type_data)
  

async def connect_and_listen(mode=""):
    global cider_websocket_url
    global data
    global count
    
    try:
        async with websockets.connect(cider_websocket_url) as websocket:
            if mode == "test" or mode == "test+":
                print(f"Connected to {cider_websocket_url}")
                count = 0

            while True:
                # Receive data from the WebSocket server
                data = await websocket.recv()
                if mode == "test+":
                    print(f"Received: {data}")

                try:
                    websocket_json = json.loads(data)
                except Exception as e:
                    print(f"unable to json the data for ws: {e}")

                # call function that checks if song has changed, if not: dont do anything, if yes: update all.
                # considering skipping the checking and just making everything update
                # but am trying to stop unneccessary writes.
                try:
                    update_vars(websocket_json, mode)
                except Exception as e:
                    print(f"error update_vars: {e}")

    except Exception as e:
        print(f"Connection error: {e}")
        print("Trying again...")
        time.sleep(3)
        

def start_websocket(mode=""):
    # for this following code, and the connect and listen, is very jank. not sure why it doesnt work on python 3.9 or newer, will find out eventually.
    # Create a new event loop
    loop = asyncio.new_event_loop()

    # Set the event loop for the current thread
    asyncio.set_event_loop(loop)

    # Run the event loop to start the WebSocket connection
    while True:
        try:
            webloop = asyncio.new_event_loop()
            webloop.run_until_complete(connect_and_listen(mode))
            
        except Exception as e:
            print(f"Error during event loop: {e}")


def start_mode():
        global mode
        if mode == "test" or mode == "test+":
            print(mode)
        
        if mode == "test":
            print("cider_apis.py: starting websockets w/ Testing Prints...")
            start_websocket(mode)
        elif mode == "test+":
            print("cider_apis.py: starting websockets w/ Testing Prints + JSON recieved")
            start_websocket(mode)
        else:
            print("cider_apis.py: starting websockets...")
            start_websocket()
