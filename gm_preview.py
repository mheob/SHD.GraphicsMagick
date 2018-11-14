import os

import PythonMagick


def main():
    # Specify some variables
    input_dir = os.path.curdir + "/testdata/_orig/"

    # Rename file extension to lowercase (JPG only)
    lowercase_file_extension(input_dir)

    # Modify the images
    modify_images(input_dir)


def lowercase_file_extension(input_dir):
    for filename in os.listdir(input_dir):
        if not os.path.splitext(filename)[1] == ".JPG":
            continue

        full_filename = input_dir + "/" + filename
        os.rename(full_filename, full_filename.lower())


def modify_images(input_dir):
    output_dirs = [input_dir + "../512/", input_dir + "../150/"]

    for directory in output_dirs:
        if not os.path.isdir(directory):
            os.mkdir(directory)

    for filename in os.listdir(input_dir):
        if not filename.endswith(".jpg"):
            continue

        img = PythonMagick.Image(input_dir + filename)
        img.strip()
        img.trim()
        img.quality(80)
        img.resize("512x512>")
        img.write(output_dirs[0] + "/" + filename)

        print(filename + " in " + "512" + " erstellt.")

    for filename in os.listdir(output_dirs[0]):
        if not filename.endswith(".jpg"):
            continue

        img = PythonMagick.Image(output_dirs[0] + filename)
        img.resize("150x150>")
        img.write(output_dirs[1] + "/" + filename)

        print(filename + " in " + "150" + " erstellt.")


if __name__ == '__main__':
    main()
