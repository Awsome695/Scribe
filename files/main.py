import threading
import time

import cider_apis
import sys


# if create_txts():
#    update_text()
#    update_text_thread.start()
#    update_art_thread.start()
#    time.sleep(15)
#    start_chat_bot()


def start_chat_bot():
    from twitch_bot import bot
    bot.run()
    print("Starting Chat bot...")


def update_art_r():
    prev_song = ""
    while True:
        time.sleep(1)
        name = cider_apis.return_name()
        if prev_song != name:
            print("update gui")
            prev_song = name
            cider_apis.get_album_art()


def update_text_r():
    # uses same order as the gui, most of this code was just copied and adjusted, and some actually new, first time
    # making something like this so if you got suggestions let me know!! make a issue or pull in github! ps its also
    # my first time using GitHub soooo.... hehe pardon my bad code and repo >_<

    # for some reason this variable somehow it worky
    song = str(cider_apis.return_name())

    song_file = open(os.getcwd() + "\\txts\\song.txt", "w", encoding='utf-8')
    song_file.write(song)
    song_file.close()

    artist_file = open(os.getcwd() + "\\txts\\artist.txt", "w", encoding='utf-8')
    artist_file.write(str(cider_apis.return_artistName()))
    artist_file.close()

    album_file = open(os.getcwd() + "\\txts\\album.txt", "w", encoding='utf-8')
    album_file.write(str(cider_apis.return_albumName()))
    artist_file.close()


def update_art_ws():
    prev_song = ""
    while True:
        time.sleep(1)
        name = cider_apis.return_name()
        if prev_song != name:
            print("update gui")
            prev_song = name
            cider_apis.get_album_art()


def update_text_ws():
    # uses same order as the gui, most of this code was just copied and adjusted, and some actually new, first time
    # making something like this so if you got suggestions let me know!! make a issue or pull in github! ps its also
    # my first time using GitHub soooo.... pardon my bad code and repo xd

    # for some reason this variable somehow it worky
    song = str(cider_apis.return_name())

    song_file = open(os.getcwd() + "\\txts\\song.txt", "w", encoding='utf-8')
    song_file.write(song)
    song_file.close()

    artist_file = open(os.getcwd() + "\\txts\\artist.txt", "w", encoding='utf-8')
    artist_file.write(str(cider_apis.return_artistName()))
    artist_file.close()

    album_file = open(os.getcwd() + "\\txts\\album.txt", "w", encoding='utf-8')
    album_file.write(str(cider_apis.return_albumName()))
    artist_file.close()


if len(sys.argv) > 1:
    # Loop through the command line arguments
    for arg in sys.argv[1:]:
        # Check if the argument is "-rest"
        if arg == "-rest":
            print("main.py: starting using cider's REST api")
            cider_apis.start_mode("rest")

            # run + thread on the side
            update_art_thread = threading.Thread(target=update_art_r)
            update_text_thread = threading.Thread(target=update_text_r)

        elif arg == "-websocket":
            print("main.py: starting using cider's websocket api")
            cider_apis.start_mode("web")
            # wait a few secs for update vars to update
            time.sleep(2)
            # run + thread on the side
            update_art_thread = threading.Thread(target=update_art_ws)
            update_text_thread = threading.Thread(target=update_text_ws)

        else:
            print(f"Unknown argument: {arg}")
            print("Closing...")
            quit()
else:
    print("No command line arguments provided.")
    print("Closing...")
    quit()
