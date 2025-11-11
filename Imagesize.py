# --------------------------------------
# Import libraries
# --------------------------------------

# Fix the ImportError on original line 6
import math

# --------------------------------------
# Constants
# --------------------------------------
BITS_PER_BYTE = 8

# fix the logic error on original line 14
BYTES_PER_KIBIBYTE = 1024

# --------------------------------------
# Global variables
# --------------------------------------
imageWidth = 0
imageHeight = 0
imageBitsPerPx = 0
numberOfBytes = 0


# --------------------------------------
# Subprograms
# --------------------------------------
def calcImageSize(pWidth, pHeight, pBitsPerPixel):
    bits = pWidth * pHeight * pBitsPerPixel
    bytes = math.ceil(bits / BITS_PER_BYTE)
    return bytes

    # Fix the logic error to return the number of bytes for the image


# --------------------------------------
# Main program
# --------------------------------------

imageWidthPx = int(input("Image width in pixels (e.g. 800): "))
imageHeightPx = int(input("Image height in pixels (e.g. 600): "))
imageBitsPerPx = int(input("Number of bits per pixel (e.g. 24): "))

# Fix the syntax error on original line 42
numberOfBytes = calcImageSize(imageWidthPx, imageHeightPx,imageBitsPerPx)

# Fix the logic error on original line 45
numberOfKiB = numberOfBytes / BYTES_PER_KIBIBYTE
print("The image file size is", numberOfBytes, "bytes or", numberOfKiB, "KiB")
