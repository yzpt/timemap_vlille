import os
import imageio

path = 'img_BYG_400px_portland/'

initial_files = os.listdir(path)
images = sorted([img for img in os.listdir(path) if img.endswith(".png")])
image_files = [imageio.imread(path + '/' + img) for img in images]

imageio.mimsave('output/' + path[:-1] + '.mp4', image_files, fps=24)  # fps specifies the frames per second