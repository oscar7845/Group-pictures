import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import file
import shutil

def test_image_resize():
    album_path = "./images/"
    target_path = "./target/"

    width = 640
    height = 480
    fx = 0.5
    fy = 0.5

    d1 = file.transform_images_size(album_path, target_path, width,height,fx,fy,file.ResizeMode.CROP)
    assert(len(file.find_images(album_path)) == len(file.find_images(d1)))
    d2 = file.transform_images_size(album_path, target_path, width,height,fx,fy,file.ResizeMode.RESIZE)
    assert(len(file.find_images(album_path)) == len(file.find_images(d2)))
    d3 = file.transform_images_size(album_path, target_path, width,height,fx,fy,file.ResizeMode.SCALE)
    assert(len(file.find_images(album_path)) == len(file.find_images(d3)))
   
    target_path = "./target/"
    if os.path.exists(target_path):
        shutil.rmtree(target_path)