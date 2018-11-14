import sys

from os import listdir, mkdir, path, rename
from time import sleep

import PythonMagick


def main():
    # determine if application is a script file or frozen exe
    application_path = None
    if getattr(sys, 'frozen', False):
        # published executable
        application_path = path.dirname(sys.executable)
    elif __file__:
        # testing script
        application_path = path.join(path.dirname(__file__), "testdata/_orig")

    if application_path is None:
        exit(1)

    # Rename file extension to lowercase (JPG only)
    lowercase_file_extension(application_path)

    # Modify the images
    modify_images(application_path)

    # Out on shutting down the application
    print()
    print("\t--------------------------------------------------------------------")
    print()
    print("\tDie Verarbeitung ist beendet und dieses Fenster wird in Kürze geschlossen ...")
    print("\tVielen Dank für die Nutzung dieses Tools!")
    print()
    sleep(3)


def lowercase_file_extension(application_path):
    print()
    print("\tÜberprüfe die Dateinamen nach Großbuchstaben:")
    print()

    count_files = 0

    for filename in listdir(application_path):
        if not path.splitext(filename)[1] == ".JPG":
            continue

        full_filename = path.join(application_path, filename)
        rename(full_filename, full_filename.lower())

        print("\t" + filename + "\t wurde zu \t" + filename.lower() + "\t korrigiert")

        count_files += 1

    print()

    if count_files > 0:
        print("\tInsgesamt wurden " + str(count_files) + " Dateien umbenannt.")
    else:
        print("\tEs mussten keine Dateien umbenannt werden.")


def modify_images(application_path):
    output_dirs = [path.join(application_path, "..", "512"), path.join(application_path, "..", "150")]
    count_files = 0

    print()
    print("\t--------------------------------------------------------------------")
    print()
    print("\tErstelle die benötigten Ordner, falls sie noch nicht vorhanden sind:")
    print()

    for directory in output_dirs:
        if not path.isdir(directory):
            mkdir(directory)
            print("\tDer Ordner " + path.realpath(directory) + " wurde erstellt.")
        else:
            print("\tDer Ordner " + path.realpath(directory) + " war bereits vorhanden.")

    print()
    print("\t--------------------------------------------------------------------")
    print()
    print("\tErstelle die Bilder in der Größe \"512px\":")
    print()

    for filename in listdir(application_path):
        if not filename.endswith(".jpg"):
            continue

        img = PythonMagick.Image(path.join(application_path, filename))
        # noinspection PyArgumentList
        img.strip()
        # noinspection PyArgumentList
        img.trim()
        img.quality(80)
        img.resize("512x512>")
        img.write(path.join(output_dirs[0], filename))

        print("\t" + filename + "\t erfolgreich erstellt.")

        count_files += 1

    print()
    print("\tInsgesamt wurden " + str(count_files) + " Bilder in der Größe \"512px\" erzeugt.")
    print()
    print("\t--------------------------------------------------------------------")
    print()
    print("\tErstelle die Bilder in der Größe \"150px\":")
    print()

    count_files = 0

    for filename in listdir(output_dirs[0]):
        if not filename.endswith(".jpg"):
            continue

        img = PythonMagick.Image(path.join(output_dirs[0], filename))
        img.resize("150x150>")
        img.write(path.join(output_dirs[1], filename))

        print("\t" + filename + "\t erfolgreich erstellt.")

        count_files += 1

    print()
    print("\tInsgesamt wurden " + str(count_files) + " Bilder in der Größe \"150px\" erzeugt.")


if __name__ == '__main__':
    main()
