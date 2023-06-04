# PythonScripts
"Barcode scanners are disguised windows to your Windows" BSidesTLV 2023 Talk Python scripts.

# Description
The following python scripts generates 2D barcodes that comprises a series of commands and data.
Each script perform a different action.

The scripts were tested tested with the following barcode scanners:
- Honeywell Voyager 1400G
- Datalogic QuickScan QW2420
- Eyoyo EY-L5

The tests were made with the following laptops and operating systems:
- DELL P62F001 laptop Windows 10, Version 10.0.19043.1237
- Asus G731GU  laptop Windows 10, Version 10.0.19043.1237
- Asus G731GU  laptop Windows 11, Version 10.0.22000.282

The script were created by Paz Hameiri in 2022 and released in 2023

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL
WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL
THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR
CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT,
NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN
CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

# Open CMD.py
The Python script generates a 2D barcode that comprises a series of commands to perform the following actions:
1. Open the Windows Start menu
2. Search and execute a command-line window

# Open PowerShell.py
The Python script generates a 2D barcode that comprises a series of commands to perform the following actions:
1. Open the Windows Start menu
2. Search and execute a PowerShell window

# Open Task Manager.py
The Python script generates a 2D barcode that comprises a series of commands to perform the following actions:

For the Honeywell and Eyoyo barcode scanners:
1. Press Ctrl-Alt-Del
2. Select the Task Manager in the User Account Control window

For the Datalogic barcode scanner:
1. Press Ctrl-Shift-Esc

# Open CMD via Task Manager.py
The Python script generates a 2D barcode that comprises a series of commands to perform the following actions:

For the Honeywell and Eyoyo barcode scanners:
1. Press Ctrl-Alt-Del
2. Select the Task Manager in the User Account Control window
3. Choose to run a new task
4. Run cmd.exe to open a command-line window

For the Datalogic barcode scanner:
1. Press Ctrl-Shift-Esc
2. Choose to run a new task
3. Run cmd.exe to open a command-line window

# Open System Information.py
The Python script generates a 2D barcode that comprises a series of commands to perform the following actions:
1. Open the Windows Start menu
2. Search and execute the System Information tool

# Open OSK.py
The Python script generates a 2D barcode that comprises a series of commands to perform the following actions:
1. Open the Windows Start menu
2. Search and execute the on-screen keyboard

# Hide CMD.py
The Python script generates a 2D barcode that comprises a series of commands to perform the following actions:
1. Open the Windows Start menu
2. Search and execute a command-line window
3. Minimize the size of the window
4. Hide the command-line windows behind an active software

# Open CMD as Admin.py
The Python script generates a 2D barcode that comprises a series of commands to perform the following actions:
1. Open the Windows Start menu
2. Search and execute a PowerShell window
3. Open a command-line window as an administrator
4. Approve the command at the User Account Control window

# Open PowerShell as Admin.py
The Python script generates a 2D barcode that comprises a series of commands to perform the following actions:
1. Open the Windows Start menu
2. Search and execute a PowerShell window
3. Open a PowerShell window as an administrator
4. Approve the command at the User Account Control window

# Download file with CMD and PS.py
The Python script generates a 2D barcode that comprises a series of commands to perform the following actions:
1. Open the Windows Start menu
2. Search and execute a command-line window
3. Minimize the size of the window
4. Download a file
5. Execute the file
6. Approve the execution at the User Account Control window

# Upload and run file - Base64 encoding.py
The Python script generates 2D barcodes that comprises a series of commands to perform the following actions:

The first barcode:
1. Open the Windows Start menu
2. Search and execute a command-line window
3. Minimize the size of the window
4. Upload the first part of a file (Base64 encoded) to the host
Each following barcode:
5. Upload the following file part (Base64 encoded) to the host
The last barcode:
6. Upload the last file part (Base64 encoded) to the host
7. Decode the uploaded file and delete it
8. Unzip the decoded file and delete it
9. Execute the unzipped files

# Upload and run file - Hex encoding.py
The Python script generates 2D barcodes that comprises a series of commands to perform the following actions:

The first barcode:
1. Open the Windows Start menu
2. Search and execute a command-line window
3. Minimize the size of the window
4. Upload the first part of a file (hex-encoded) to the host
Each following barcode:
5. Upload the following file part (hex-encoded) to the host
The last barcode:
6. Upload the last file part (hex-encoded) to the host
7. Decode the uploaded file and delete it
8. Unzip the decoded file and delete it
9. Execute the unzipped files

# Upload and run file - Base64 encoding with PS.py
The Python script generates 2D barcodes that comprises a series of commands to perform the following actions:

The first barcode:
1. Open the Windows Start menu
2. Search and execute a PowerShell window
3. Minimize the size of the window
4. Upload the first part of a file (Base64 encoded) to the host
Each following barcode:
5. Upload the following file part (Base64 encoded) to the host
The last barcode:
6. Upload the last file part (Base64 encoded) to the host
7. Decode the uploaded file and delete it
8. Unzip the decoded file and delete it
9. Execute the unzipped files

# FullScreenSelfCheckoutPOS.py
A simple self-checkout point-of-sale system software demo.

# Hide CMD with POS entry.py
The Python script generates a 2D barcode that comprises a series of commands to perform the following actions:
1. Open the Windows Start menu
2. Search and execute a command-line window
3. Minimize the size of the window
4. Hide the command-line windows behind a point-of-sale software
5. Enter an item code in the point-of-sale software

# Download file with CMD and PS with POS entry.py
The Python script generates a 2D barcode that comprises a series of commands to perform the following actions:
1. Enter an item code in a POS software
2. Open the Windows Start menu
3. Search and execute a command-line window
4. Minimize the size of the window
5. Download a file
6. Execute the file
7. Approve the execution at the User Account Control window

# Upload and run file - Base64 encoding with POS entry.py
The Python script generates 2D barcodes that comprises a series of commands to perform the following actions:

The first barcode:
1. Open the Windows Start menu
2. Search and execute a command-line window
3. Minimize the size of the window
4. Upload the first part of a file (Base64 encoded) to the host
5. Enter an item code in a point-of-sale software
Each following barcode:
6. Upload the following file part (Base64 encoded) to the host
7. Enter an item code in a point-of-sale software
The last barcode:
8. Upload the last file part (Base64 encoded) to the host
9. Decode the uploaded file and delete it
10. Unzip the decoded file and delete it
11. Execute the unzipped files
12. Enter an item code in a point-of-sale software
