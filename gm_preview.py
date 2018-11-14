import os
import sys

import PythonMagick


def main():
    # determine if application is a script file or frozen exe
    application_path = None
    if getattr(sys, 'frozen', False):
        # published executable
        application_path = os.path.dirname(sys.executable)
    elif __file__:
        # testing script
        application_path = os.path.join(os.path.dirname(__file__), "testdata/_orig")

    if application_path is None:
        exit(1)

    # Rename file extension to lowercase (JPG only)
    lowercase_file_extension(application_path)

    # Modify the images
    modify_images(application_path)


def lowercase_file_extension(application_path):
    print()
    print("Überprüfe die Dateinamen nach Großbuchstaben:")
    print()

    count_files = 0

    for filename in os.listdir(application_path):
        if not os.path.splitext(filename)[1] == ".JPG":
            continue

        full_filename = os.path.join(application_path, filename)
        os.rename(full_filename, full_filename.lower())

        print(filename + "\t wurde zu \t" + filename.lower() + "\t korrigiert")

        count_files += 1

    print()

    if count_files > 0:
        print("Insgesamt wurden " + str(count_files) + " Dateien umbenannt")
    else:
        print("Es mussten keine Dateien umbenannt werden.")


def modify_images(application_path):
    output_dirs = [os.path.join(application_path, "..", "512"), os.path.join(application_path, "..", "150")]
    count_files = 0

    print()
    print("--------------------------------------------------------------------")
    print()
    print("Erstelle die benötigten Ordner, falls sie noch nicht vorhanden sind:")
    print()

    for directory in output_dirs:
        if not os.path.isdir(directory):
            os.mkdir(directory)
            print("Der Ordner " + os.path.realpath(directory) + " wurde erstellt.")
        else:
            print("Der Ordner " + os.path.realpath(directory) + " war bereits vorhanden.")

    print()
    print("--------------------------------------------------------------------")
    print()
    print("Erstelle die Bilder in der Größe \"512px\":")
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

        print(filename + "\t erfolgreich erstellt.")

        count_files += 1

    print()
    print("Insgesamt wurden " + str(count_files) + " Bilder in der Größe \"512px\" erzeugt.")
    print()
    print("--------------------------------------------------------------------")
    print()
    print("Erstelle die Bilder in der Größe \"150px\":")
    print()

    count_files = 0

    for filename in os.listdir(output_dirs[0]):
        if not filename.endswith(".jpg"):
            continue

        img = PythonMagick.Image(os.path.join(output_dirs[0], filename))
        img.resize("150x150>")
        img.write(os.path.join(output_dirs[1], filename))

        print(filename + "\t erfolgreich erstellt.")

        count_files += 1

    print()
    print("Insgesamt wurden " + str(count_files) + " Bilder in der Größe \"150px\" erzeugt.")
    print()
    print("--------------------------------------------------------------------")
    print()
    print("Die Verarbeitung ist beendet. Vielen Dank für die Nutzung dieses Tools!")
    print()


if __name__ == '__main__':
    main()
