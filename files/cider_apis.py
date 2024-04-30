import json
import os
import requests
import threading
import time
import wget
import sys
import asyncio
import websockets

# urls | change this if cider ever changes this for some reason :/
cider_rest_url = "http://localhost:10769"
cider_websocket_url = "ws://localhost:10766/ws"

# REST commands
isPlaying_REST = "/isPlaying"
currentPlayingSong_REST = "/currentPlayingSong"

# variables to store cider values
# json
json_data = {}
info_json_data = {}
data_json_data = {}
# song info
status = ""
song_name = ""
song_artist = ""
song_album = ""
song_link = ""
current_playback_time = float
duration_in_ms = float
# websockets specific values
type_data = str
# misc
status_code = ""  # used for debug if for some reason a status code is needed.


def start_mode(arg=""):
    if arg == "rest" or "r":
        print("cider_apis.py: starting rest...")
    if arg == "webs" or "ws":
        print("cider_apis.py: starting websockets...")


def rest_request(url="http://localhost:10769", command="/active"):
    global json_data, status_code, info_json_data

    response = requests.get(url + command)
    status_code = response.status_code
    try:
        json_data = response.json()
    except Exception as e:
        print(f"json_data error: {e}")
    try:
        info_json_data = json_data.get("info")
    except Exception as e:
        print(f"info_json_data error: {e}")



def rest_update_vars():
    global cider_rest_url, currentPlayingSong_REST,

    # currently only implementing variables that im ACTUALLY using so..
    # feel free to add anymore that seem needed, and make PR for it
    # a shit ton of try(ies) to find root of any variable issue -_-
    try:
        rest_request(cider_rest_url, currentPlayingSong_REST)
    except Exception as e:
        print(f"requests error: {e}")


def rest_thread_func():
    while True:
        rest_update_vars()
        time.sleep(1)
