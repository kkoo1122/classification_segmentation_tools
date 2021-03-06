# match train data and label
import os
import glob
import shutil

from IPython import embed

mode = 'copy'

# target path
path_target = '/media/kevintsai/cef8b40c-14d2-4a8f-a359-9da3eeceb1d4/Projects/potato/spatial_data/gtFine/val/'

# move target to direction
move_dir_target = '/media/kevintsai/cef8b40c-14d2-4a8f-a359-9da3eeceb1d4/Projects/potato/Work/potato_original/'

# target2 path
path_target2 = '/media/kevintsai/cef8b40c-14d2-4a8f-a359-9da3eeceb1d4/Projects/potato/Work/potato_original/'

# move target2 to direction
move_dir_target2 ='/media/kevintsai/cef8b40c-14d2-4a8f-a359-9da3eeceb1d4/Projects/potato/spatial_data/leftImg8bit/val/'

filename_image = os.listdir(path_target)
filename_image.sort()

filename_label = os.listdir(path_target2)
filename_label.sort()

for index, f in enumerate(filename_image):
    if f in filename_label:
        print(index+1, f)
        if mode == 'copy':
            #shutil.copyfile(path_target+f, move_dir_target+f)
            shutil.copyfile(path_target2+f, move_dir_target2+f)
        elif mode == 'move':
            shutil.move(path_target+f, move_dir_target+f)
            #shutil.move(path_target2+f, move_dir_target2+f)
        else:
            print("Please choose correct mode. (copy/move)")
            break
            
print("File match completed! ({})".format(mode))
