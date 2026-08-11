# Lab 06 - Practical Python: Text and Graphical Interfaces

In this lab, we'll build two kinds of interactive program from this week's lectures: a
**text-based interface (TUI)** that runs in the terminal with a menu loop, and a small
**graphical interface (GUI)** built with `tkinter`.

**Time:** this lab is meant to be finished in the 80-minute session. If you don't
finish, you may keep working during the week and submit any time up to the **first 10
minutes of next week's lab**.  After 10 minutes, though, the lab will not be accepted,
to avoid a cascade effect. The **Lab 06 quiz on Canvas** closes at that moment - that is
where you hand this lab in, so read [How to Submit](#how-to-submit) before you start.

## Getting Started

You should be a member of the **CSCI1030U** organization on GitHub, from the invitation
sent out after Lab 01. If you never accepted that invitation, do it now (check your email,
or go to <https://github.com/CSCI1030U>) - you can't create your lab repository until
you're a member. Tell your lab instructor if no invitation ever arrived.

Lab repositories are **templates**: you make your own copy with one click.

1. Open the **Lab 06 template** link in the Canvas lab quiz.
2. Click the green **Use this template** button, then **Create a new repository**.
3. Fill in the form:
   - **Owner:** `CSCI1030U` (the organization, *not* your own account)
   - **Repository name:** `lab06-your-username` - for example `lab06-jsmith2026`
   - **Visibility:** **Private**
4. Click **Create repository**.

Use **Use this template**, not **Fork** - a fork can never be made private, which would
show your solution to the whole class.

Then clone it. On your new repo's page, click the green **Code** button and copy the URL.
In the folder where you keep your CSCI 1030U labs:

```
git clone https://github.com/CSCI1030U/lab06-your-username
cd lab06-your-username
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

Handing in a lab is two steps: **push your work**, then **record it in the Canvas quiz**.
This is the same routine for every lab.

### Step 1 - Commit and push

Once your tests pass (or the session is ending):

```
git add --all
git commit -m "Lab 06 completed"
git push origin main
```

Then open your repository page on GitHub and check that your changed files are actually
there. That is your confirmation the push worked.

> **Check your own work with `pytest`, on your own machine.** Your repository has an
> autograder, but it does not run when you push - your instructor runs it during marking,
> against the commit hash you submit below. So `pytest` passing locally is the only
> pass/fail signal you get, and it is the one that counts. Don't submit without running it.

### Step 2 - Get the commit hash

Check that everything really is committed and pushed, then read the hash of that snapshot:

```
git status
git rev-parse HEAD
```

`git status` should say `nothing to commit, working tree clean` and that your branch is up
to date with `origin/main`. If it lists changes, go back to Step 1. Then `git rev-parse HEAD`
prints a 40-character hash, like `3f9a1c2e8b7d4056a1f2e3d4c5b6a7f8091a2b3c`.

### Step 3 - Submit the quiz

Open the **Lab 06 quiz on Canvas** and enter:

- your **repository URL**: `https://github.com/CSCI1030U/lab06-your-username`
- your **commit hash**, pasted exactly as `git rev-parse HEAD` printed it

Then answer the remaining questions and submit. **The Canvas submission time is your
submission time**, and the commit hash you give is the snapshot that gets marked - anything
you push afterwards is not seen. If you fix something important later, get the new hash and
resubmit if the quiz still allows it.

## Using AI

You may use an AI assistant to **explain ideas and help you learn** - but **not to
generate code you submit** in this half of the term. Use only a **free** model, and be
ready to explain every line you wrote; the lab instructor may ask you to walk through
your code.
