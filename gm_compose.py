from os import listdir, mkdir, path

from pgmagick import Image, GravityType, CompositeOperator

test_dir = path.join(path.curdir, "testdata")

layer = Image(path.join(test_dir, "New_256x256.png"))

output_dir = path.join(test_dir, input("Bitte den Speicherort angeben (Ordner reicht): "))

if not path.isdir(output_dir):
    mkdir(output_dir)

for file in listdir(test_dir):
    if file.endswith(".jpg"):
        img = Image(path.join(test_dir, file))
        img.composite(layer, GravityType.NorthEastGravity, CompositeOperator.OverCompositeOp)
        img.write(output_dir + "\\" + file)
