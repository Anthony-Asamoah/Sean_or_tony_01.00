import time
from playsound import playsound

while True:
    start = input("\nStart Timer?\n reply with 'y' / 'n'\n\t->")
    if start in ['y', 'n']:
        if start == 'n':
            break
        else:
            while True:
                try:
                    Mins = int(input("\nEnter Minutes as integer (Max = 100): "))
                except ValueError:
                    print("kindly provide integers only...")
                    continue
                if Mins not in range(100):
                    print("Invalid input!")
                    continue
                else:
                    break

            while True:
                try:
                    secs = int(input("Enter seconds as integer: "))
                except ValueError:
                    print("kindly provide integers only...")
                    continue
                if secs not in range(10000):
                    print("Invalid input!")
                    continue
                else:
                    break

            total = (int(Mins) * 60) + int(secs)

            print(f"\n\nTimer started for {total} seconds")
            time.sleep(total)
            print("\nTime up!\n\n")
            playsound('./audio.mp3')
            continue
    else:
        print("\nInvalid Input!\n")    
    
print("\nLater then...")

