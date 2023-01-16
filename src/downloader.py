import random
import requests
from pytube import YouTube
import os
from moviepy.editor import VideoFileClip, concatenate_videoclips


def get_random_timestamp(video_url) -> list:
    '''
    Get random timestamp from a video.
    '''
    # Get video length
    yt = YouTube(video_url)
    video_length = yt.length

    # Get random timestamp
    random_timestamp = random.randint(0, video_length)

    # Get random timestamp in the middle of the video
    random_timestamp = random_timestamp + (video_length - random_timestamp) // 2
    
    return [random_timestamp, video_length]


def download_random_videos(channel_urls):
    # Download random videos from each channel
    # First, get all videos from channel
    for channel_url in channel_urls:
        channel_id = channel_url.split('/')[-1]
        key = ''
        with open('.env.local', 'r') as f:
            key = f.read().split('=')[1]
        response = requests.get(
            f'https://www.googleapis.com/youtube/v3/search?part=snippet&channelId={channel_id}&maxResults=50&order=date&type=video&key={key}')
        # Get random video from channel
        videos = response.json()['items']
        random_video = random.choice(videos)
        video_id = random_video['id']['videoId']

        # Download video with pytube
        yt = YouTube(f'https://www.youtube.com/watch?v={video_id}')
        yt.streams.filter(progressive=True, file_extension='mp4').order_by(
            'resolution').desc().first().download('build')


def combine_videos(final_name):
    '''
    Combine videos in the build directory into one video.
    '''
    video_clips = []
    for video in os.listdir('build'):
        video_clips.append(VideoFileClip(f'build/{video}'))
    final_clip = concatenate_videoclips(video_clips)
    final_clip.write_videofile(f'output/{final_name}.mp4')
