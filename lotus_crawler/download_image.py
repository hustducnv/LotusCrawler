import requests
import os
from pandas import read_csv
import threading
import numpy as np
from tqdm import tqdm
from configs import *


def download_image(url, save_to):
    try:
        res = requests.get(url)
        if res.ok:
            with open(save_to, 'wb') as f:
                f.write(res.content)
        else:
            print('----------FAIL-------------------: fail to get image at {}'.format(url))
    except:
        print('----------FAIL-------------------: fail to get image at {}'.format(url))


def download_image_multithreading(df):
    save_dir = GetImageConfig.SAVE_DIR
    n_threads = len(df) - 1
    threads = []
    for i in range(n_threads):
        post_id, thumbnail_url = df.iloc[i]
        save_path = os.path.join(save_dir, str(post_id))
        _thread = threading.Thread(target=download_image, args=(thumbnail_url, save_path))
        threads.append(_thread)

    for _thread in threads:
        _thread.start()

    for _thread in threads:
        _thread.join()


def crawl_thumb():
    post_thumb_link_path = GetImageConfig.POST_THUMB_LINK_PATH
    df = read_csv(
        post_thumb_link_path,
        dtype={'post_id': str, 'thumbnail_url': str}
    )
    start_idx = GetImageConfig.START_IDX
    end_idx = GetImageConfig.END_IDX
    df = df[start_idx:end_idx]

    n_threads = GetImageConfig.N_THREADS
    n_posts = len(df)
    if n_threads == 1:
        for i in tqdm(range(n_posts)):
            post_id, thumbnail_url = df.iloc[i]
            download_image(thumbnail_url, post_id)
    else:
        for i in tqdm(range(int(np.ceil(n_posts/n_threads)))):
            start = i*n_threads
            end_idx = (i+1)*n_threads
            if end_idx > n_posts:
                end_idx = n_posts
            download_image_multithreading(df[start_idx:end_idx])




