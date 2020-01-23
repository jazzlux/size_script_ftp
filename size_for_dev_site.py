from PIL import Image
import glob, os


def size_change(file_path, w, h):

    size = w, h
    for items in glob.glob(file_path):
        file = os.path.splitext(items)

        photo = Image.open(items)
        photo.thumbnail(size)
        photo.save("%s.jpg" %(file[0]))

# size_change("../../stronyWWW/Coder/files/uploads/600x400/*.jpg", 600, 400)

size_change("../../stronyWWW/Coder/files/uploads/1680x1100/*.jpg", 1680, 1100 )
