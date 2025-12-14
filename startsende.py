with open("file.txt") as f:
    for line in f:
        s = line.strip()
        if s.startswith('s') and s.endswith('e'):
            print(s)
