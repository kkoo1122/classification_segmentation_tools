# match train data and label
import os
import glob
import shutil

from IPython import embed

mode = 'copy'

# original image path
path_train = '/auto/shared/client_data/wada/potato_images/raws/yellow_raws_dec_2019/'

# original image direction
move_dir_train = '/media/kevintsai/cef8b40c-14d2-4a8f-a359-9da3eeceb1d4/Projects/potato/Work/potato_original/'

# label path
path_label = '/media/kevintsai/cef8b40c-14d2-4a8f-a359-9da3eeceb1d4/Projects/potato/Work/potato_masks/ok_using/'

# label direction
move_dir_label ='/media/kevintsai/cef8b40c-14d2-4a8f-a359-9da3eeceb1d4/Projects/potato/images_new/gtFine/train/'

filename_image = os.listdir(path_train)
filename_image.sort()

filename_label = os.listdir(path_label)
filename_label.sort()

for index, f in enumerate(filename_image):
    if f in filename_label:
        print(index+1, f)
        if mode == 'copy':
            shutil.copyfile(path_train+f, move_dir_train+f)
            #shutil.copyfile(path_label+f, move_dir_label+f)
            print("File match completed! (copy)")
        elif mode == 'move':
            shutil.move(path_train+f, move_dir_train+f)
            #shutil.move(path_label+f, move_dir_label+f)
            print("File match completed! (move)")
        else:
            print("Please choose correct mode. (copy/move)")
            break
