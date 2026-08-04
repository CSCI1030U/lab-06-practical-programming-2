# These tests RUN your bank.py program and type answers into it, the same way you
# would at the keyboard, then check what it prints. Each `feed(...)` call is one full
# session; the final "4" always quits the program.
#
# (There is no test for gui.py - a graphical program is checked by your lab instructor.)

import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def feed(keystrokes):
    result = subprocess.run(
        [sys.executable, os.path.join(HERE, "bank.py")],
        input=keystrokes, capture_output=True, text=True)
    return result.stdout


def test_deposit_updates_balance():
    out = feed("1\n50\n3\n4\n")            # deposit 50, show balance, quit
    assert "New balance: 50.00" in out
    assert "Current balance: 50.00" in out
    assert "Goodbye" in out


def test_withdraw_subtracts():
    out = feed("1\n100\n2\n30\n3\n4\n")    # deposit 100, withdraw 30, show balance
    assert "New balance: 70.00" in out
    assert "Current balance: 70.00" in out


def test_withdraw_too_much_is_blocked():
    out = feed("1\n20\n2\n50\n3\n4\n")     # deposit 20, try to withdraw 50, show balance
    assert "Insufficient funds" in out
    assert "Current balance: 20.00" in out


def test_invalid_choice():
    out = feed("9\n4\n")                   # an option that isn't on the menu, then quit
    assert "Invalid choice" in out
    assert "Goodbye" in out
