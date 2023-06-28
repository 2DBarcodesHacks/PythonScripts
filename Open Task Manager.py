###################################################################
# The following Python script generates a 2D barcode that         #
# comprises a series of commands to perform the following         #
# actions:                                                        #
#                                                                 #
# For the Honeywell and Eyoyo barcode scanners:                   #
# 1. Press Ctrl-Alt-Del                                           #
# 2. Select the Task Manager in the User Account Control window   #
#                                                                 #
# For the Datalogic barcode scanner:                              #
# 1. Press Ctrl-Shift-Esc                                         #
#                                                                 #
# The script was created by Paz Hameiri in 2022 and released      #
# in 2023                                                         #
#                                                                 #
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL   #
# WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED   #
# WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL    #
# THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR      #
# CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM  #
# LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, #
# NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN       #
# CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.        #
###################################################################

# Tested on DELL P62F001 laptop Windows 10, Version 10.0.19043.1237
# Tested on Asus G731GU  laptop Windows 10, Version 10.0.19043.1237
# Tested on Asus G731GU  laptop Windows 11, Version 10.0.22000.282

# Tested with:
# * Honeywell Voyager 1400G
# * Datalogic QuickScan QW2420
# * Eyoyo EY-L5

import segno # Note: segno-pil also needs to be installed
from pylibdmtx.pylibdmtx import encode
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import matplotlib.pyplot as plt

###################################################################
# Select barcode scanner                                          #
###################################################################

# Define barcode scanner model:
# Honeywell
# Datalogic
# Eyoyo
ControlCodes = "Honeywell"

# Select 2D barcode output:
# QRCode
# DataMatrix
SelectedBarcode = 'QRCode'

# Link between functions and ASCII codes (Barcode scanner dependent)
if (ControlCodes.upper() == "HONEYWELL") | (ControlCodes.upper() == "EYOYO"):
    # Declare barcode scanner ASCII codes for Honeywell and Eyoyo:
    Alt         = chr(0x03)
    AltRelease  = chr(0x04)
    Ctrl        = chr(0x05)
    CtrlRelease = chr(0x06)
    Tab         = chr(0x09)
    Del         = chr(0x0C)
    Enter       = chr(0x0D)
    Ins         = chr(0x0E)
    Esc         = chr(0x0F)
    BackTab     = chr(0x14)
    AltBackTab  = Alt+BackTab+AltRelease
    
else:
    # Declare barcode scanner ASCII codes for Datalogic:
    Alt         = chr(0x9B)
    AltRelease  = chr(0x9C)
    Ctrl        = chr(0x9D)
    CtrlRelease = chr(0x9E)
    Tab         = chr(0x09)
    Enter       = chr(0x0D)
    Ins         = chr(0x83)
    Esc         = chr(0x1B)
    Shift       = chr(0x81)
    ShiftRelease = chr(0x82)
    AltBackTab  = Shift+Alt+Tab+ShiftRelease+AltRelease

###################################################################
# Generate a 2D barcode that comprises a series of commands to    #
# perform the following actions:                                  #
#                                                                 #
# For the Honeywell and Eyoyo barcode scanners:                   #
# 1. Press Ctrl-Alt-Del                                           #
# 2. Select the Task Manager in the User Account Control window   #
#                                                                 #
# For the Datalogic barcode scanner:                              #
# 1. Press Ctrl-Shift-Esc                                         #
###################################################################

if (ControlCodes.upper() == "HONEYWELL") | (ControlCodes.upper() == "EYOYO"):
    # Open Windows Security window
    TxString = (Ctrl+Alt+Del+ # Press Ctrl-Alt-Del to open the Windows Security window
                CtrlRelease+ # Release the Ctrl
                AltRelease) # Release the Alt
    
    # Add delay, waiting for the Windows Security window to take control
    TxString = TxString + Ins * (4 * 8)
    
    # Add Press Tab three times at Windows Security window to get to the Task Manager option
    # and press Enter to select the option
    TxString = (TxString+Tab+Tab+Tab+Enter)
else: 
    # Open the Task Manager window
    TxString = (Ctrl+Shift+Esc+ # Press Ctrl-Shift-Esc to open the Task Manager window
                ShiftRelease+ # Release the Shift
                CtrlRelease) # Release the Ctrl

# Add Enter in Honeywell case
if ControlCodes.upper() == "HONEYWELL":
    TxString = TxString + Enter # Execute the command

###################################################################
# Generate the 2D barcode                                         #
###################################################################
    
# Generate QR Code or Data Matrix barcode
if SelectedBarcode.upper() == "QRCODE":
    # Generate QR code
    qr = segno.make(TxString, mode='byte', encoding='ISO 8859-1') # Image creation with segno, encoding ISO 8859-1 for ASCII codes 128-255
    img = qr.to_pil(scale = 10)
    
    # Set image font
    font = ImageFont.truetype("arial.ttf", 28, encoding="unic")
else:
    # Generate Data Matrix
    encoded_data = encode(TxString.encode('ISO 8859-1'), scheme='Base256') # schemes: 'Ascii', 'AutoBest', 'AutoFast', 'Base256', 'C40', 'Edifact', 'Text', 'X12'
    img = Image.frombytes('RGB', (encoded_data.width, encoded_data.height), encoded_data.pixels)
    
    # Set image font
    font = ImageFont.truetype("arial.ttf", 16, encoding="unic")

# Change the image canvas size to add text above the image
widthOffset = 150
heightOffset = 30
imgwidth, imgheight = img.size
imgWithText = Image.new(img.mode, (imgwidth + widthOffset, imgheight + heightOffset), 'white')
imgWithText.paste(img, (0, heightOffset))
img = imgWithText

# Add Text to the image
draw = ImageDraw.Draw(img)
draw.text((0, 0), ControlCodes + ':' + 'Open Task Manager',fill = 'black', font = font)

# Display the barcode in Spyder
plt.imshow(img)

# Display the barcode in Windows
img.show()



