#!/usr/bin/env python3
"""Understanding dictionaries """

def main():
    """runtime function"""

marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"Hulk":
  {"real name": "bruce banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
        }

    cn = input("what's your name? ")
    cn = cn.capitalize()
    
    cs = inout("what's stat? ")
    
    print(marvelchars.get(cn).get(cs))
    print(cn + "'s", cs, "is:", marvelchars.get(cn).get(cs))


if __name__ == "__main__":
    main()
