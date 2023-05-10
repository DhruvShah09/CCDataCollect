from trafilatura import fetch_url, extract 

link_file = open("clinks.txt", "r")
links = link_file.readlines()
for i in range(len(links)): 
    print(i + 1) 
    result = extract(fetch_url(links[i]))
    print("done")
