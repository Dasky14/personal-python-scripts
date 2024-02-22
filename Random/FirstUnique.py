def first_unique_character():
    s = "dddccdbba"
    with open("message.txt") as f:
        s = "".join(f.readlines())
    blacklist = []
    i = 0
    for c in s:
        if c not in blacklist:
            if s.find(c, i+1) == -1:
                return c
            else:
                blacklist.append(c)
        i += 1

    return -1

print(first_unique_character())