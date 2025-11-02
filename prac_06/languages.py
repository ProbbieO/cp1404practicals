"""
CP1404
Using the ProgrammingLanguage class
"""

from prac_06.programming_language import ProgrammingLanguage

def main():
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    languages = [python, ruby, vb]

    print(python)
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)

main()
