import tkinter as tk

# Simple Calculator with Grey & Black Theme

def on_click(btn_text):
    if btn_text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif btn_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, btn_text)

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.config(bg="#2b2b2b")  # Dark background

entry = tk.Entry(root, font=("Arial", 20), justify="right", bg="#3c3c3c", fg="white", bd=5)
entry.pack(fill=tk.X, padx=10, pady=10)

btn_frame = tk.Frame(root, bg="#2b2b2b")
btn_frame.pack()

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for row in buttons:
    frame_row = tk.Frame(btn_frame, bg="#2b2b2b")
    frame_row.pack()
    for btn_text in row:
        btn = tk.Button(frame_row, text=btn_text, font=("Arial", 16), width=5, height=2,
                         bg="#4b4b4b", fg="white", activebackground="#5c5c5c",
                         command=lambda t=btn_text: on_click(t))
        btn.pack(side=tk.LEFT, padx=5, pady=5)

root.mainloop()