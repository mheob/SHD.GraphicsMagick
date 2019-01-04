from os import path, remove

from PythonMagick import Image, CompositeOperator

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
            flattened = Image("%sx%s" % (img.columns(), img.rows()), "#fff")
            flattened.composite(img, 0, 0, CompositeOperator.SrcOverCompositeOp)
            flattened.magick("JPG")
            flattened.write(path.splitext(file)[0] + out_type)
            remove(file)
