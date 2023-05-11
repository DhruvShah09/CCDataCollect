from trafilatura import fetch_url, extract 

link_file = open("clinks.txt", "r")
links = link_file.readlines()
out_file = open("out.txt", "a")
for i in range(len(links)): 
    print(i + 1) 
    result = extract(fetch_url(links[i].strip()))
    if (result is none):
        print("error")
        continue
    out_file.write(result +"\n")
    print("done")
