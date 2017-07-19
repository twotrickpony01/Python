from Tkinter import Tk
r=Tk()

def string_sort(string_given):
    new_str = sorted(string_given.replace(",", "").split(), key=str.lower)
    newest_str = ""
    count = len(new_str)
    for i in new_str:
        if count > 1:
            newest_str += i
            newest_str += ", "
            count -= 1
        else:
            newest_str += i
    return newest_str

sorted_string = string_sort(Tk().clipboard_get())
r.withdraw()
r.clipboard_clear()
r.clipboard_append(sorted_string)
r.destroy()
