import os

import PythonMagick as pm


def main():
    # Specify some variables
    inputDir = os.path.curdir + "/testdata/"

    # Rename file extension to lowercase (JPG only)
    lowercaseFileExtension(inputDir)

    # Modify the images
    modifyImages(inputDir)


def lowercaseFileExtension(inputDir):
    for filename in os.listdir(inputDir):
        if not os.path.splitext(filename)[1] == ".JPG":
            continue

        fullFilename = inputDir + "/" + filename
        os.rename(fullFilename, fullFilename.lower())


def modifyImages(inputDir):
    outputDirs = [inputDir + "/../150", inputDir + "/../512"]

    for directory in outputDirs:
        if not os.path.isdir(directory):
            os.mkdir(directory)

    for filename in os.listdir(inputDir):
        if not filename.endswith(".jpg"):
            continue

        for outputDir in outputDirs:
            img = pm.Image(inputDir + filename)
            img.strip()
            img.trim()
            img.quality(80)
            img.resize("512x512>" if outputDir.endswith("512") else "150x150>")
            img.write(outputDir + "/" + filename)

            curSize = "150" if outputDir.endswith("150") else "512"
            print(filename + " in " + curSize + " erstellt.")


if __name__ == '__main__':
    main()
