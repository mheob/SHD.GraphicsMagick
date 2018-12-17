from os import path

from PythonMagick import Image

from SHD.utils.file_utilities import FileUtilities


class GmUtilities:
    @staticmethod
    def convert_filetype(input_files, output_type, extensions):
        out_type = "." + output_type.lower()
        is_no_image = True

        for file in input_files:
            for extension in extensions:
                if path.splitext(file)[1] == "." + extension.lower():
                    is_no_image = False
                    break
                else:
                    is_no_image = True

            if is_no_image or path.splitext(file)[1] == out_type:
                continue

            FileUtilities.backup_file(file)
            img = Image(file)
            img.write(path.splitext(file)[0] + out_type)
            FileUtilities.remove_original_file(file)
