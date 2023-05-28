import sys
import random
from pyfiglet import Figlet

def print_usage_and_exit():
    print("Usage: python figlet.py [-f|--font <font_name>]")
    sys.exit(1)

def select_random_font():
    figlet = Figlet()
    available_fonts = figlet.getFonts()
    random_font = random.choice(available_fonts)
    return random_font

def print_text_in_font(text, font):
    figlet = Figlet(font=font)
    rendered_text = figlet.renderText(text)
    print(rendered_text)

if len(sys.argv) == 1:
    font = select_random_font()
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    font = sys.argv[2]
else:
    print_usage_and_exit()

user_input = input("Enter a text: ")

print_text_in_font(user_input, font)
