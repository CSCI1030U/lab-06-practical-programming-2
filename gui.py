# Part 2 (STRETCH) - a small graphical interface (GUI) with tkinter: a tip calculator.
#
# The window and its widgets are built for you. Write the `calculate` function so that,
# when the button is clicked, it reads the bill amount, works out a 15% tip and the
# total, and shows them in the result label.
#
# There is no automated test for this part (a GUI can't be checked that way) - show it
# to your lab instructor.

import tkinter as tk


def calculate():
    # TODO: read the bill amount with entry.get() and turn it into a float. Work out
    #   a 15% tip and the total (bill + tip). Then show them, e.g.:
    #       result.config(text="Tip: $1.50   Total: $11.50")
    pass


root = tk.Tk()
root.title("Tip Calculator")

tk.Label(root, text="Bill amount:").pack(padx=10, pady=(10, 0))
entry = tk.Entry(root)
entry.pack(padx=10, pady=4)

tk.Button(root, text="Calculate 15% tip", command=calculate).pack(padx=10, pady=4)

result = tk.Label(root, text="Tip: $0.00   Total: $0.00", font=("Arial", 12))
result.pack(padx=10, pady=10)

root.mainloop()
