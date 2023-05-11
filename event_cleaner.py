with open("cclinks.txt", "r") as input_file:
    lines = input_file.readlines()

with open("cclinksnoevent.txt", "w") as output_file:
    for line in lines:
        if "https://www.cc.gatech.edu/news/" not in line:
            output_file.write(line)