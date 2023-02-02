with open("Input/Names/invited_names.txt") as names:
    names.read()

    with open("Input/Letters/starting_letter.txt") as starting_letter:
        default_writings = starting_letter.read()

        names_list = names.readlines()
        for name in names_list:

            name = name.strip()
            name_lower = name.lower()

            with open(f"Output/ReadyToSend/{name_lower}_letter.txt") as unique_letter:
                unique_writings = default_writings.replace("[name]", name)
                unique_letter.write(unique_writings)