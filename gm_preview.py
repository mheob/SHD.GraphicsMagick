import os


def main():
    # Current directory
    directory = os.path.curdir + "/testdata/"

    # Rename file extension to lowercase (JPG only)
    for filename in os.listdir(directory):
        if os.path.splitext(filename)[1] == ".JPG":
            src = directory + "/" + filename
            dist = directory + "/" + os.path.splitext(filename)[0] + ".jpg"
            os.rename(src, dist)


if __name__ == '__main__':
    main()
