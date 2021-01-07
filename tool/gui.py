# GUI for sekiro-corrupt-save-fix
# https://github.com/z0gSh1u/sekiro-corrupt-save-fix

import os.path as path
dirname__ = path.dirname(path.abspath(__file__))

from tkinter import *
from tkinter import filedialog, ttk, messagebox
from fix import main as fix_main

root = Tk()
root.title('Sekiro Corrupt Save Fix')

sl2_path = ''
slot_index = 0

cbo_slot = ttk.Combobox(root)
lbl_path = lbl_path = Label(root, {
    'text': 'No S0000.sl2 selected.',
    'fg': 'red'
})
lbl_status = Label(root, {'text': 'Nothing now.'})
lbl_status_text = ''


def ask_open_file():
    global sl2_path, lbl_path
    temp_path = filedialog.askopenfilename(title='Open S0000.sl2',
                                           filetypes=[('sl2 file', '*.sl2')])
    if len(temp_path) > 0:
        sl2_path = temp_path
        lbl_path.configure(text=sl2_path, fg='blue')


def start_fixing():
    global sl2_path, slot_index, lbl_status, lbl_status_text
    if len(sl2_path) == 0:
        messagebox.showerror('Error', 'Please select path to save file first.')
        return
    try:
        lbl_status_text += 'Start fixing {} @ slot {}.\n'.format(
            sl2_path, slot_index)
        lbl_status.configure(text=lbl_status_text)
        fix_main(sl2_path, slot_index)
        lbl_status_text += 'The corrupt save has been backup with external name .fixbackup.\n'
        lbl_status.configure(text=lbl_status_text)
        lbl_status_text += 'Fixing done successfully!\n'
        lbl_status.configure(text=lbl_status_text)
    except Exception as ex:
        print(repr(ex))
        messagebox.showerror('Error', repr(ex))
        lbl_status.configure(text=repr(ex))
    lbl_status_text = ''


def combo_change(_):
    global slot_index, cbo_slot
    slot_index = int(cbo_slot.current())


# padding
Label(root).pack()

# introduction
Label(root, {
    'text': 'Site: https://github.com/z0gSh1u/sekiro-corrupt-save-fix'
}).pack()
Label(
    root, {
        'text':
        'CAUTION: MAKE SURE YOU HAVE READ THE INSTRUCTIONS AND DISCLAIMER BEFORE YOU START!',
        'fg': 'red'
    }).pack()

# path hint
Label(
    root, {
        'text':
        'Sekiro save file is at C:/Users/<Your Name>/AppData/Roaming/Sekiro/<Your Steam ID>/S0000.sl2'
    }).pack()

# browse button
Label(root, {'text': '----- [Step 1] Select save file S0000.sl2 -----'}).pack()
lbl_path.pack()
Button(root, {
    'text': 'Browse S0000.sl2',
    'command': ask_open_file,
}).pack()

# slot_index select
Label(root, {
    'text': '----- [Step 2] Select your save slot index -----'
}).pack()
cbo_slot['values'] = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
cbo_slot.current(0)
cbo_slot.bind('<<ComboboxSelected>>', combo_change)
cbo_slot.configure(state="readonly")
cbo_slot.pack()

# start button
Label(root, {'text': '----- [Step 3] Start fixing -----'}).pack()
Button(root, {
    'text': 'Start fixing',
    'command': start_fixing,
}).pack()

# status display
Label(root, {'text': '----- [Status Display] -----'}).pack()
lbl_status.pack()

# padding
Label(root).pack()

root.mainloop()
