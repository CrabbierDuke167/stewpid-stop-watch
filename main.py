# Stewpid Stop Watch v2.0
# Fuck AI
# v1.0 made in 30mins lessgo (; 
# v2.0 made in 30 + 20 mins 
# cooler TUI
# works for mac and linux
import time, os, sys, textwrap

# Global Vars
hr, min, sec = 0, 0, 0
ascii_art = textwrap.dedent('''
    ███████╗████████╗███████╗██╗    ██╗██████╗ ██╗██████╗
    ██╔════╝╚══██╔══╝██╔════╝██║    ██║██╔══██╗██║██╔══██╗
    ███████╗   ██║   █████╗  ██║ █╗ ██║██████╔╝██║██║  ██║
    ╚════██║   ██║   ██╔══╝  ██║███╗██║██╔═══╝ ██║██║  ██║
    ███████║   ██║   ███████╗╚███╔███╔╝██║     ██║██████╔╝
    ╚══════╝   ╚═╝   ╚══════╝ ╚═╝╚═╝ ╚═╝     ╚═╝╚═════╝
''')


# StopWatch BluePrint
class StopWatch:
    def __init__(self):
        self.isRunning = False

    def updateStatus(self):
        self.isRunning = not self.isRunning


# UI renderer function
def renderUI():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("------------------------------------------------------------------------")
    for line in ascii_art.splitlines(): # ascii art centered
        print("\033[31m" + line.center(72) + "\033[0m")
    print("========================================================================")
    print("\tInput anything to start the timer.")
    print("\tPress Ctrl+C to stop the timer.")
    print("========================================================================\n")

    try:
        userInp = input("Ready when you are ↓ \n")
        Inp = True if userInp else True

        stopwatch.isRunning = True if Inp else False
        c = Start()
        os.system('cls' if os.name == 'nt' else 'clear')


        while stopwatch.isRunning:
            current_time = next(c)

            formatted_time = f"{current_time[0]} hr / {current_time[1]} min / {current_time[2]} sec"

            print("------------------------------------------------------------------------")
            print("\033[91mTimer Running // Ctrl+C to stop\033[0m")
            print("------------------------------------------------------------------------")
            for line in ascii_art.splitlines(): # ascii art centered
                print("\033[34m" + line.center(72) + "\033[0m")
            print("========================================================================")
            print(formatted_time.center(72))
            print("========================================================================")

            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')

    except KeyboardInterrupt:
        stopwatch.isRunning = False
        print("========================================================================")
        print("Timer Stopped".center(72))
        print("========================================================================")
        sys.exit()

# Start Timer function
def Start():
    global hr
    global min
    global sec

    try:
        while stopwatch.isRunning:
            sec += 1

            (min, sec) = (min + 1, 0) if sec >= 60 else (min, sec)
            (hr, min) = (hr + 1, 0) if min >= 60 else (hr, min)

            yield (hr, min, sec)

    except KeyboardInterrupt:
        stopwatch.isRunning = False
        sys.exit()


# Create a stopwatch
stopwatch = StopWatch()


if __name__ == "__main__":
    renderUI()