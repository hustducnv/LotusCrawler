import os

BASE_DIR = os.path.dirname(__file__)
CORE_DATA_DIR = os.path.join(BASE_DIR, 'data')
IMAGES_BASE_DIR = os.path.join(CORE_DATA_DIR, 'post_images')


class GetUrlConfig:
    POST_LINK_PATH = os.path.join(CORE_DATA_DIR, 'post_link.csv')
    MAX_IDX = 98703
    START_IDX = 0
    END_IDX = 5000  # EXCLUSIVE


class GetImageConfig:
    POST_THUMB_LINK_PATH = os.path.join(CORE_DATA_DIR, 'post_thumb_link.csv')
    MAX_IDX = 98703
    START_IDX = 0
    END_IDX = 100  # EXCLUSIVE
    N_THREADS = 50
    SAVE_DIR = os.path.join(CORE_DATA_DIR, 'post_images', '{}_{}'.format(START_IDX, END_IDX))
    if not os.path.exists(SAVE_DIR):
        os.mkdir(SAVE_DIR)

