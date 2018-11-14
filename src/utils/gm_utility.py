from os import listdir, path, rename


class GmUtility:
    @staticmethod
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
