mac_num = "112233445566"
mac_adress = ""

collon_count = 0
for num in range(0, len(mac_num), 2):
    mac_adress += mac_num[num] + mac_num[num + 1]
    if collon_count < 5:
        mac_adress += ":"
        collon_count += 1