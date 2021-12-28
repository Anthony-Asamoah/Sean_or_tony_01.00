import time

while True:
    start = input("\nStart Timer?\n reply with 'y' / 'n'\n\t->")
    if start in ['y', 'n']:
        if start == 'n':
            break
        else:
            Mins = input("enter Minutes as integer: ")
            secs = input("enter seconds as integer: ")

            total  = (int(Mins) * 60 )+ int(secs)

            print(f"\n\n Timer started for {total}secons")
            time.sleep(total)
            print("Timer up!\n\n")

            continue
    else:
        print("\nInvalid Input!\n")    
    
print("\nLater then...")

# todo: add a ringtone/beep/alert
