import threading
import time
import os
import cider_apis
import sys
import wget

arg = ""

def update_art_ws():
    global arg
    # var to store previous song
    prev_song = ""
    # var to store artwork link
    artwork_link = ""

    # loop to check and update
    while True:
        
        # get song name
        try: 
            current_song = cider_apis.return_vars("song_name")
        except Exception as e:
            print(f"Failed to get name: {e}")

        # check if current and previous are same or not
        if prev_song != current_song:
            # debug update text
            if arg == "test" or "test+":
                print("updating art")

            # update prev song value to current.
            prev_song = current_song

            # update artwork link
            try:
                artwork_link = cider_apis.return_vars("artwork_link")
            except Exception as e:
                print(f"failed to get artwork_link: {e}")
            
            # debug text for artwork link
            if arg == "test+":
                print("artworklink: " + artwork_link)

            # check if the file exists, if so remove it and download new one
            if os.path.exists(os.getcwd() + "\\600x600bb.jpg"):
                # remove and download
                try:
                    os.remove(os.getcwd() + "\\600x600bb.jpg")
                    wget.download(artwork_link)
                except Exception as e:
                    print(f"remove and/or download failed: {e}")

            else:
                try:
                    wget.download(artwork_link)
                except Exception as e:
                    print(f"failed to download artwork: {e}")
                    
        # for pacing, and to prevent extremely fast inf loops.
        time.sleep(1)


def update_text_ws():
    global arg
    # variable to save previous song.
    prev_song = ""
    if arg == "test" or arg == "test+":
        print("update text was called.")

    while True:
        time.sleep(1)
        
        # get song name first
        try:
            song = str(cider_apis.return_vars("song_name"))
            if arg == "test" or arg == "test+":
                print("song: " + song)
        except Exception as e:
                print(f"failed to get song var: {e}")
        
        # compare it with previous to see if it has changed and if so, update texts
        if prev_song != song:
            # debug update text
            if arg == "test" or arg == "test+":
                print("updating .txt s")
            # update text
            prev_song = song

            # song name txt update 
            try:
                print("should be working for song...")
                song_file = open(os.getcwd() + "\\txts\\song.txt", "w", encoding='utf-8')
                song_file.write(song)
                song_file.close()
            except Exception as e:
                print(f"song file failed: {e}")

            # artist name txt update
            try:
                print("should be working for artist...")
                artist_file = open(os.getcwd() + "\\txts\\artist.txt", "w", encoding='utf-8')
                artist_file.write(str(cider_apis.return_vars("song_artist")))
                artist_file.close()
            except Exception as e:
                print(f"artist file failed: {e}")

            # album name txt update
            try:
                print("should be working for album...")
                album_file = open(os.getcwd() + "\\txts\\album.txt", "w", encoding='utf-8')
                album_file.write(str(cider_apis.return_vars("song_album")))
                album_file.close()
            except Exception as e:
                print(f"album file failed: {e}")


if len(sys.argv) > 1:
    # Loop through the command line arguments
    for arg1 in sys.argv[1:]:
        arg = arg1
        # this is the normal mode, will see errors print out in console if there are some
        if arg1 == "-ws":
            print("main.py: starting using cider's websocket api...")
            cider_apis.set_mode("")
            time.sleep(1)
            cider_apis_thread = threading.Thread(target=cider_apis.start_mode)

            # create and set thread targets
            update_art_thread = threading.Thread(target=update_art_ws)
            update_text_thread = threading.Thread(target=update_text_ws)

            # start threads
            cider_apis_thread.start()

            # wait a few secs for update vars to update
            time.sleep(2)

            update_art_thread.start()
            update_text_thread.start()

        # for debugging with more info and some reduced text
        elif arg1 == "-t":
            # debug uses only
            print("main.py: starting using cider's websocket api w/ Testing Prints...")
            print("setting api mode to: " + arg1)
            cider_apis.set_mode("test")
            time.sleep(1)
            print("setting cider apis thread")
            cider_apis_thread = threading.Thread(target=cider_apis.start_mode)

            # create and set thread targets
            print("setting update art thread")
            update_art_thread = threading.Thread(target=update_art_ws)
            print("setting update text thread")
            update_text_thread = threading.Thread(target=update_text_ws)

            # start threads
            print("cider apis thread start")
            cider_apis_thread.start()

            # wait a few secs for update vars to update
            time.sleep(2)

            print("update art thread start")
            update_art_thread.start()
            print("update text thread start")
            update_text_thread.start()

        # for debugging with everything printing thats been set to print
        elif arg1 == "-t+":
            # debug uses only
            print("main.py: starting using cider's websocket api w/ Testing Prints + Extra Prints")
            print("setting api mode to: " + arg1)
            cider_apis.set_mode("test+")
            time.sleep(1)
            print("setting cider apis thread")
            cider_apis_thread = threading.Thread(target=cider_apis.start_mode)

            # create and set thread targets
            print("setting update art thread")
            update_art_thread = threading.Thread(target=update_art_ws)
            print("setting update text thread")
            update_text_thread = threading.Thread(target=update_text_ws)
            
            # start threads
            print("cider apis thread start")
            cider_apis_thread.start

            # wait a few secs for update vars to update
            time.sleep(2)

            print("update art thread start")
            update_art_thread.start
            print("update text thread start")
            update_text_thread.start

        else:
            print(f"Unknown argument: {arg}")
            print("Closing...")
            quit()
else:
    print("No command line arguments provided.")
    print("Closing...")
    quit()

