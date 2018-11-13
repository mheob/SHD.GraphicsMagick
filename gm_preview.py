import os


def main():
    # Current directory
    directory = os.path.curdir + "/testdata/"

    # Rename file extension to lowercase (JPG only)
    lowercaseFileExtension(directory)


def lowercaseFileExtension(directory):
    for filename in os.listdir(directory):
        if not os.path.splitext(filename)[1] == ".JPG":
            continue
        fullFilename = directory + "/" + filename
        os.rename(fullFilename, fullFilename.lower())


if __name__ == '__main__':
    main()
