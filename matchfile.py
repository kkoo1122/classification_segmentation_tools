# match train data and label
import os
import glob
import shutil

from IPython import embed

path_train = '/media/kevintsai/cef8b40c-14d2-4a8f-a359-9da3eeceb1d4/Projects/potato/images_new/leftImg8bit/train/'

move_dir_train = '/media/kevintsai/cef8b40c-14d2-4a8f-a359-9da3eeceb1d4/Projects/potato/Work/leftImg8bit/train/'

path_label = '/media/kevintsai/cef8b40c-14d2-4a8f-a359-9da3eeceb1d4/Projects/potato/Work/gtFine/train/'

move_dir_label ='/media/kevintsai/cef8b40c-14d2-4a8f-a359-9da3eeceb1d4/Projects/potato/images_new/gtnotFine/train/'

filename_image = os.listdir(path_train)
filename_image.sort()

filename_label = os.listdir(path_label)
filename_label.sort()

for index, f in enumerate(filename_image):
    if f in filename_label:
        print(index+1, f)
        #shutil.copyfile(path_train+f, move_dir_train+f)
        shutil.copyfile(path_label+f, move_dir_label+f)

print("File match completed!")
