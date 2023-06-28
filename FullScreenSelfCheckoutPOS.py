###################################################################
# A simple self-checkout point-of-sale system software demo.      #
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

# Import the tkinter library
import tkinter as tk

# Create an instance of tkinter frame
win = tk.Tk()

# Add a text label, font property and foreground color to it
label= tk.Label(win, text= "Self checkout point of sale system", font=('Times New Roman bold',72), foreground="blue")
label.pack(padx=10, pady=10)

# Create a windows in full-screen mode
win.attributes('-fullscreen', True)

# Assign the ESC button to enable to user to get out of the full-screen mode
win.bind("<Escape>", lambda event: win.attributes("-fullscreen", False))

# Add a text box
text_box = tk.Text( win, height=15, width=40, font=('Times New Roman bold',20))
text_box.pack(expand=True)
text_box.config(state='normal')

win.mainloop()