from os import path, rename

from PythonMagick import Image


class GmUtility:
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

            rename(file, file.lower())

            print("\t" + file + "\t wurde zu \t" + file.lower() + "\t korrigiert")

            count_files += 1

        print()

        if count_files > 0:
            print("\tInsgesamt wurden " + str(count_files) + " Dateien umbenannt.")
        else:
            print("\tEs mussten keine Dateien umbenannt werden.")

    @staticmethod
    def convert_filetype(input_files, output_type, extensions):
        out_type = "." + output_type.lower()
        is_no_image = True

        for file in input_files:
            for extension in extensions:
                if path.splitext(file)[1] == "." + extension.lower():
                    is_no_image = False
                    break

            if is_no_image or path.splitext(file)[1] == out_type:
                continue

            img = Image(file)
            img.write(path.splitext(file)[0] + out_type)
