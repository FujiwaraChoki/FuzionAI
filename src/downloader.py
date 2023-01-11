import random
from pytube import Channel
from moviepy.editor import VideoFileClip, concatenate_videoclips


def download_random_videos(channel_links):
    '''Download a random video from channels.

    Args:
        channel_link: A link to a YouTube channel.
    '''
    for channel in channel_links:
        channel = Channel(channel)
        videos = channel.video_urls
        random_video = random.choice(videos)
        # Download
        random_video.download('build/')
