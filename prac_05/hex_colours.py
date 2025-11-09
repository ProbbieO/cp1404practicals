"""
Practical 05
"""

COLOUR_TO_CODE = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Beige": "#f5f5dc",
    "BlueViolet": "#8a2be2",
    "CadetBlue": "#5f9ea0",
    "CornflowerBlue": "#6495ed",
    "DarkGoldenRod": "#b8860b",
    "DeepPink": "#ff1493",
    "FireBrick": "#b22222"
}

def main():
    """hex codes for given colour names"""
    colour_name = input("Enter a colour name: ").strip()
    while colour_name != "":

        formatted_name = colour_name.replace(" ", "").title()
        try:
            print(f"{formatted_name} is {COLOUR_TO_CODE[formatted_name]}")
        except KeyError:
            print("Invalid colour name")
        colour_name = input("Enter a colour name: ").strip()
    print("Goodbye!")

main()
