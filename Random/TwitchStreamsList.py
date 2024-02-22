import requests
from tkinter import *
import threading

channels = ["CHANNEL_1", "CHANNEL_2", "CHANNEL_3"]
my_client_id = "YOUR_CLIENT_ID"

def get_streaming_channels(channels):
    streaming_channels = []
    for channel in channels:
        url = f"https://api.twitch.tv/kraken/streams/{channel}"
        headers = {"Accept": "application/vnd.twitchtv.v5+json", "Client-ID": my_client_id}
        response = requests.get(url, headers=headers)
        data = response.json()
        if data["stream"]:
            game = data["stream"]["game"]
            streaming_channels.append((channel, game))
    return streaming_channels

def update_streaming_channels(root, label_list, channels):
    streaming_channels = get_streaming_channels(channels)
    for label in label_list:
        label.destroy()
    label_list.clear()
    for i, (channel, game) in enumerate(streaming_channels):
        label = Label(root, text=f"{channel} is streaming {game}")
        label.grid(row=i, column=0)
        label_list.append(label)
    root.after(15000, update_streaming_channels, root, label_list, channels)

def show_streaming_channels(channels):
    root = Tk()
    root.title("Streaming Channels")
    label_list = []
    update_streaming_channels(root, label_list, channels)
    root.mainloop()

show_streaming_channels(channels)