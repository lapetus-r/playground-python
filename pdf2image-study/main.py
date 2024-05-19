from pdf2image import convert_from_path

images = convert_from_path("files/datasheet-cc-8800-1.pdf")
images[1].save("datasheet-cc-8800-1.jpg", "JPEG")
