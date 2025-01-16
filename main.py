with open("books/frankestein.txt") as f:
    file_contents = f.read()
    lowered = file_contents.lower()
    map = {}
    for letter in lowered:
        if letter.isalpha():
            if letter in map:
                map[letter] += 1
            else:
                map[letter] = 1
    print(map)
    for key, value in map.items():
        print(f"The '{key}' character was found {value} times")