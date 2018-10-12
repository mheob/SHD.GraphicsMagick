import os

from pgmagick import Image, GravityType, CompositeOperator

testDir = os.path.curdir + "/testdata/"

layer = Image(testDir + "New_256x256.png")

outputDir = testDir + input("Bitte den Speicherort angeben (Ordner reicht): ")

if not os.path.isdir(outputDir):
    os.mkdir(outputDir)

for file in os.listdir(testDir):
    if file.endswith(".jpg"):
        img = Image(testDir + file)
        img.composite(layer, GravityType.NorthEastGravity, CompositeOperator.OverCompositeOp)
        img.write(outputDir + "\\" + file)
