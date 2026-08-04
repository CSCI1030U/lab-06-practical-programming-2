# Lab 06 - Practical Python: Text and Graphical Interfaces

In this lab, we'll build two kinds of interactive program from this week's lectures: a
**text-based interface (TUI)** that runs in the terminal with a menu loop, and a small
**graphical interface (GUI)** built with `tkinter`.

**Time:** this lab is meant to be finished in the 80-minute session. If you don't
finish, you may keep working during the week and submit any time up to the **first 10
minutes of next week's lab**.  After 10 minutes, though, the lab will not be accepted,
to avoid a cascade effect.

## Getting Started

Accept the GitHub Classroom assignment invitation in Canvas (the link is in the lab
assignment on Canvas), which will clone your own copy of the repository. In the folder
where you keep your CSCI 1030U labs:

```
git clone https://github.com/CSCI1030U/lab06-your-username
```

## Instructions

You'll finish two programs, `bank.py` (the core) and `gui.py` (the stretch). Look for
the `# TODO` comments in each.

### Part 1 - `bank.py` (a menu-driven "piggy bank")

`bank.py` already has the menu loop written for you. It repeatedly shows this menu and
reads a choice:

```
1) Deposit
2) Withdraw
3) Balance
4) Quit
```

Fill in the three branches so the program keeps track of a **balance** (which starts at
`0.00`):

- **Deposit** - ask `Amount: `, read the number, add it to the balance, and print
  `New balance: <balance>` (to two decimal places).
- **Withdraw** - ask `Amount: `. If it is **more** than the balance, print
  `Insufficient funds` and leave the balance alone. Otherwise subtract it and print
  `New balance: <balance>`.
- **Balance** - print `Current balance: <balance>` (to two decimal places).

Keep the wording exactly as shown - the automated tests look for those lines. A sample
session (what you type is after each `Choice:`/`Amount:` prompt):

```
1) Deposit
2) Withdraw
3) Balance
4) Quit
Choice: 1
Amount: 50
New balance: 50.00
...
Choice: 2
Amount: 20
New balance: 30.00
...
Choice: 3
Current balance: 30.00
...
Choice: 4
Goodbye
```

Hint: two decimal places comes from an f-string like `f"New balance: {balance:.2f}"`.

### Part 2 - `gui.py` (a tip-calculator window)  *(stretch - optional, spot-checked)*

`gui.py` builds a small window with a text box, a button, and a result label. Write the
`calculate` function so that when the button is clicked it:

1. reads the bill amount from the text box (`entry.get()`) and turns it into a float;
2. works out a **15% tip** and the **total** (bill + tip);
3. shows them in the result label, for example: `Tip: $1.50   Total: $11.50`.

Run it with `python gui.py`. **There is no automated test for this part** - a graphical
program can't be checked that way, so your lab instructor will look at it. Do it if you
have time.

## Verifying Correctness

Run the pre-written tests to check `bank.py`:

```
pytest
```

The tests actually **run your program** and type answers into it, then check what it
prints - so make sure your wording matches the examples exactly. (The tests only cover
`bank.py`; show `gui.py` to your instructor.)

## Getting Help

There is a lab instructor present for the whole session. Ask them whenever you're
stuck.

*The instructor will usually help you find the problem rather than tell you how to
fix it - the goal is for you to get better at diagnosing and fixing your own bugs.*

## How to Submit

Once your tests pass (or the session is ending), commit and push:

```
git add --all
git commit -m "Lab 06 completed"
git push origin main
```

You can confirm the autograder ran correctly by opening the **Actions** tab on your
repository page in GitHub. It can take a minute or two.

## Using AI

You may use an AI assistant to **explain ideas and help you learn** - but **not to
generate code you submit** in this half of the term. Use only a **free** model, and be
ready to explain every line you wrote; the lab instructor may ask you to walk through
your code.
