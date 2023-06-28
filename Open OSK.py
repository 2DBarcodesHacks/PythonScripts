###################################################################
# The following Python script generates a 2D barcode that         #
# comprises a series of commands to perform the following         #
# actions:                                                        #
# 1. Open the Windows Start menu                                  #
# 2. Search and execute the on-screen keyboard                    #
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
# 1. Open the Windows Start menu                                  #
# 2. Search and execute the on-screen keyboard                    #
###################################################################

# View active applications. This action was added because sending Ctrl-Esc was not always working
TxString = (Ctrl+Alt+Tab+CtrlRelease+AltRelease+ 
            Ctrl+Alt+Tab+CtrlRelease+AltRelease)

# Add delay, waiting for the view to open
if (ControlCodes.upper() == "HONEYWELL") | (ControlCodes.upper() == "EYOYO"):
    TxString = TxString + Ins * (2 * 8)
else: TxString = TxString + Ins * (8 * 8)

# Open the Windows Start menu
TxString = (TxString +
            Ctrl+Esc+ # Press Ctrl-Esc to open the Windows Start menu
            CtrlRelease) # Release the Ctrl

# Add delay, waiting for the Start menu to open
if (ControlCodes.upper() == "HONEYWELL") | (ControlCodes.upper() == "EYOYO"):
    TxString = TxString + Ins * (2 * 8)
else: TxString = TxString + Ins * (10 * 8)

# Add search string for the On-Screen Keyboard
TxString = TxString + 'osk' # Search string for the On-Screen Keyboard

# Add delay, waiting for the search to be performed
if (ControlCodes.upper() == "HONEYWELL") | (ControlCodes.upper() == "EYOYO"):
    TxString = TxString + Ins * (7 * 8)
else: TxString = TxString + Ins * (28 * 8)
    
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
widthOffset = 100
heightOffset = 30
imgwidth, imgheight = img.size
imgWithText = Image.new(img.mode, (imgwidth + widthOffset, imgheight + heightOffset), 'white')
imgWithText.paste(img, (0, heightOffset))
img = imgWithText

# Add Text to the image
draw = ImageDraw.Draw(img)
draw.text((0, 0), ControlCodes + ':' + 'Open On Screen Keyboard',fill = 'black', font = font)

# Display the barcode in Spyder
plt.imshow(img)

# Display the barcode in Windows
img.show()



