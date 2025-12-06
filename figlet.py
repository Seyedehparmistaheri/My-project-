from pyfiglet import Figlet
import random
import sys

figlet = Figlet()
fonts = figlet.getFonts()

if len (sys.argv) == 1:
    s = input("Input: ")
    random_Font = random.choice(fonts)
    figlet.setFont(font=random_Font)



elif len(sys.argv) == 2:
    print("Invalid usage")
    sys.exit(1)



elif len(sys.argv) == 3:
    a = [ "-f" , "--font"]
    fonts = figlet.getFonts()
    if sys.argv[1] in a and sys.argv[2] in fonts:
        s = input("Input: ")
        figlet.setFont(font=sys.argv[2])
    elif sys.argv[1] not in a or sys.argv[2] not in fonts:
        print("Invalid usage")
        sys.exit(1)

print(f"Output:\n{figlet.renderText(s)}")
