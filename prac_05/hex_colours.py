"""
CP1404/CP5632 Practical
Hexadecimal colour lookup
"""

COLOR_TO_CODE = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque": "#ffe4c4",
    "black": "#000000",
    "blanchedalmond": "#ffebcd",
    "blue": "#0000ff",
    "blueviolet": "#8a2be2",
    "brown": "#a52a2a"
}


def main():
    """Look up hexadecimal colour codes from color names."""
    color_name = input("Enter color name: ").strip().lower()
    while color_name != "":
        try:
            print(f"The code for {color_name} is {COLOR_TO_CODE[color_name]}")
        except KeyError:
            print("Invalid color name")
        color_name = input("Enter color name: ").strip().lower()


main()
