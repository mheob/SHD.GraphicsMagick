from os import mkdir, path, remove, rename
from shutil import copyfile


class FileUtilities:
    @staticmethod
    def lowercase_filenames(files, extensions):
        print()
        print("\tÜberprüfe die Dateinamen nach Großbuchstaben:")
        print()

        is_no_image = True
        count_files = 0

        for file in files:
            for extension in extensions:
                if path.splitext(file)[1] == "." + extension:
                    is_no_image = False
                    break

            if is_no_image or path.splitext(file)[1].islower():
                continue

            FileUtilities.backup_file(file)
            rename(file, file.lower())
            remove(file)

            filename = path.basename(file)
            print("\t" + filename + "\t wurde zu \t" + filename.lower() + "\t korrigiert")

            count_files += 1

        print()

        if count_files > 0:
            print("\tInsgesamt wurden " + str(count_files) + " Dateien umbenannt.")
        else:
            print("\tEs mussten keine Dateien umbenannt werden.")

    @staticmethod
    def create_needed_folder(output_dirs):
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

    @staticmethod
    def backup_file(file, backup_folder="backup"):
        backup_path = path.join(path.dirname(file), backup_folder)
        filename = path.basename(file)

        if not path.isdir(backup_path):
            mkdir(backup_path)
            print()
            print("\tBackupordner erstellt.")

        # TODO: Check if the file already exist ([ERRNO 13] Permission denied)
        copyfile(file, path.join(backup_path, filename))
        print("\t" + filename + "\t gesichert.")
