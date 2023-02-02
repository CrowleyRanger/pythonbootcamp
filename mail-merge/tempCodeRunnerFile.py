        names_list = names.readlines()
        for name in names_list:

            name = name.strip()
            name_lower = name.lower()

            with open(f"Output/ReadyToSend/{name_lower}_letter.txt") as unique_letter:
                unique_writings = default_writings.replace("[name]", name)
                unique_letter.write(unique_writings)