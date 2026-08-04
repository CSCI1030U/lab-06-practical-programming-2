# Part 1 - a menu-driven text interface (TUI) for a simple "piggy bank".
#
# This is a terminal program: it shows a menu, reads a choice, does something, and
# loops until the user quits. The menu loop is written for you - fill in the three
# TODO branches. Keep the exact wording shown (the tests look for it).

def main():
    balance = 0.0
    while True:
        print("1) Deposit")
        print("2) Withdraw")
        print("3) Balance")
        print("4) Quit")
        choice = input("Choice: ").strip()

        if choice == "1":
            # TODO: ask "Amount: ", read it as a float, add it to balance, then print
            #   "New balance: <balance>" with the balance shown to 2 decimal places.
            pass
        elif choice == "2":
            # TODO: ask "Amount: " and read it as a float. If it is MORE than balance,
            #   print "Insufficient funds". Otherwise subtract it from balance and
            #   print "New balance: <balance>" (2 decimal places).
            pass
        elif choice == "3":
            # TODO: print "Current balance: <balance>" (2 decimal places).
            pass
        elif choice == "4":
            print("Goodbye")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
