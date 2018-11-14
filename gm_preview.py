import os
import sys

import PythonMagick


def main():
    # determine if application is a script file or frozen exe
    application_path = None
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    elif __file__:
        application_path = os.path.dirname(__file__)

    if application_path is None:
        exit(1)

    # Rename file extension to lowercase (JPG only)
    lowercase_file_extension(application_path)

    # Modify the images
    modify_images(application_path)


def lowercase_file_extension(application_path):
    print()
    print("Überprüfe die Dateinamen nach Großbuchstaben:")

    for filename in os.listdir(application_path):
        if not os.path.splitext(filename)[1] == ".JPG":
            continue

        full_filename = os.path.join(application_path, filename)
        os.rename(full_filename, full_filename.lower())

        print(full_filename.lower() + " wurde korrigiert")

    # TODO: Output


def modify_images(application_path):
    output_dirs = [os.path.join(application_path, "..", "512"), os.path.join(application_path, "..", "150")]

    print()
    print("--------------------------------------------------------------------")
    print()
    print("Erstelle die benötigten Ordner, falls sie noch nicht vorhanden sind:")
    print()

    for directory in output_dirs:
        if not os.path.isdir(directory):
            os.mkdir(directory)
            print("Ordner " + os.path.realpath(directory) + " erstellt.")

    print()
    print("--------------------------------------------------------------------")
    print()
    print("Erstelle zu erst die Bilder für die Größe 512px:")
    print()

    for filename in os.listdir(application_path):
        if not filename.endswith(".jpg"):
            continue

        img = PythonMagick.Image(os.path.join(application_path, filename))
        # noinspection PyArgumentList
        img.strip()
        # noinspection PyArgumentList
        img.trim()
        img.quality(80)
        img.resize("512x512>")
        img.write(os.path.join(output_dirs[0], filename))

        print(filename + " in 512 erstellt.")

    print()
    print("--------------------------------------------------------------------")
    print()
    print("Erstelle nun die Bilder für die Größe 150px:")
    print()

    for filename in os.listdir(output_dirs[0]):
        if not filename.endswith(".jpg"):
            continue

        img = PythonMagick.Image(os.path.join(output_dirs[0], filename))
        img.resize("150x150>")
        img.write(os.path.join(output_dirs[1], filename))

        print(filename + " in 150 erstellt.")

    print()
    print("--------------------------------------------------------------------")
    print()
    print("Alle Bilder wurden verarbeitet. Vielen Dank für die Nutzung!")
    print()


if __name__ == '__main__':
    main()
