import sys
import keyboard

from os import listdir, mkdir, path
from time import sleep

from PythonMagick import Image
from SHD.utils.gm_utility import GmUtility


def main():
    # determine if application is a script file or frozen exe
    application_path = None
    if getattr(sys, 'frozen', False):
        # published executable
        application_path = path.dirname(sys.executable)
    elif __file__:
        # testing script
        application_path = path.join(path.dirname(__file__), "..", "..", "testdata/_orig")
    if application_path is None:
        exit(1)

    files_in_application_path = [path.join(application_path, f) for f in listdir(application_path)]

    # Rename file extension to lowercase
    GmUtility.lowercase_filenames(files_in_application_path, ["JPG", "PNG", "TIF"])

    # Convert all images to JPG
    GmUtility.convert_filetype(files_in_application_path, "JPG", ["PNG", "TIF"])

    # Modify the images
    modify_images(application_path)

    # Output on shutting down the application
    print()
    print("\t--------------------------------------------------------------------")
    print()
    print("\tDie Verarbeitung ist beendet und dieses Fenster wird in Kürze geschlossen ...")
    print("\tVielen Dank für die Nutzung dieses Tools!")
    print()
    sleep(3)


def modify_images(application_path):
    output_dirs = [path.join(application_path, "..", "512"), path.join(application_path, "..", "150")]
    count_files = 0
    override = None

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

        if path.isfile(path.join(output_dirs[0], filename)):
            if override is None:
                print("Sollen die bereits vorhandenen Bilder überschrieben werden? \t [ j | N ]\n")

                # TODO: get keyboard niput running
                while True:
                    if keyboard.is_pressed('j'):
                        override = True
                        break
                    elif keyboard.is_pressed('n'):
                        override = False
                        break
                    else:
                        pass

            if not override:
                continue

        img = Image(path.join(application_path, filename))
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

        img = Image(path.join(output_dirs[0], filename))
        img.resize("150x150>")
        img.write(path.join(output_dirs[1], filename))

        print("\t" + filename + "\t erfolgreich erstellt.")

        count_files += 1

    print()
    print("\tInsgesamt wurden " + str(count_files) + " Bilder in der Größe \"150px\" erzeugt.")


if __name__ == '__main__':
    main()
