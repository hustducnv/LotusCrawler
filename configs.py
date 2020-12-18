import os

BASE_DIR = os.path.dirname(__file__)
CORE_DATA_DIR = os.path.join(BASE_DIR, 'data')
IMAGES_BASE_DIR = os.path.join(CORE_DATA_DIR, 'post_images')
START_IDX = 0
# END_IDX = 380879
END_IDX = 5
IMAGES_DIR = os.path.join(IMAGES_BASE_DIR, '{0}-{1}'.format(START_IDX, END_IDX))
if not os.path.exists(IMAGES_DIR):
    os.mkdir(IMAGES_DIR)
