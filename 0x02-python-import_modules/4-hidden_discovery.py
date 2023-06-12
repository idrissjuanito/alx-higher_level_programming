#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    mod_content = sorted(dir(hidden_4))
    for n in mod_content:
        if not n.startswith("__"):
            print(n)
