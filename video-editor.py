from moviepy.editor import *
import tkinter as tk
from tkinter import filedialog

def import_video():
    file_path = filedialog.askopenfilename(title="Select Video File")
    return VideoFileClip(file_path)

def export_video(clip):
    file_path = filedialog.asksaveasfilename(title="Save Video As", defaultextension=".mp4")
    clip.write_videofile(file_path)

def trim_video(clip, start_time, end_time):
    return clip.subclip(start_time, end_time)

# Main code
root = tk.Tk()
root.withdraw()

video_clip = import_video()

# Trim video from 5s to 10s
trimmed_clip = trim_video(video_clip, 5, 10)

# Export trimmed video
export_video(trimmed_clip)
