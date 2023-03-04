import tkinter as tk
import utils

window = utils.create_form()
frame_1, frame_2 = utils.create_frame(window)
listbox = utils.create_scrolledtext(frame_1)
entry = utils.create_entry(frame_2)

tk.mainloop()
