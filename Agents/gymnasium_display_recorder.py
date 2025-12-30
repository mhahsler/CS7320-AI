import gymnasium as gym

from gymnasium.wrappers import RecordVideo
import glob
import io
import base64
from IPython.display import HTML
from IPython import display as ipythondisplay
from pyvirtualdisplay import Display

import os
os.environ['PYVIRTUALDISPLAY_DISPLAYFD'] = '0'

# Start virtual display
display = Display(visible=0, size=(640, 480))
display.start()

def gym_make(env_name, run_name, render_fps=30):
    """
    Create a Gym environment with video recording enabled.
    
    :param env_name: Description
    :param video_folder: Description
    :param render_fps: Description
    """
    env = gym.make(env_name, render_mode="rgb_array")
    env.metadata['render_fps'] = render_fps

    env = RecordVideo(env, 
                      video_folder='./videos', 
                      episode_trigger=lambda episode_id: True,
                      name_prefix=f'video_{run_name}')
    
    #env.reset()
    return env

def show(run_name, episode_id=0):
    """
    Display the recorded video in a Jupyter notebook.
    
    :param video_folder: Description
    """
    video = io.open(glob.glob(f'./videos/video_{run_name}*{episode_id}.mp4')[0], 'r+b').read()
    encoded = base64.b64encode(video)
    ipythondisplay.display(HTML(data='''
        <video width="640" height="480" controls>
            <source src="data:video/mp4;base64,{0}" type="video/mp4" />
        </video>
    '''.format(encoded.decode('ascii'))))