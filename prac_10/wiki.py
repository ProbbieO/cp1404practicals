"""
CP1404
Wikipedia API
"""

import wikipedia


def main():
    print("Enter page titles to search (blank to quit)")

    while True:
        title = input("Enter page title: ").strip()
        if title == "":
            print("Thank you.")
            break

        try:
            # Try to get the page without autosuggest changing the title
            page = wikipedia.page(title, auto_suggest=False)

            print(page.title)
            print(page.summary)
            print(page.url)

        except wikipedia.exceptions.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)

        except wikipedia.exceptions.PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!')


if __name__ == "__main__":
    main()
