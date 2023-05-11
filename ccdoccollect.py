from trafilatura import fetch_url, extract 

link_file = open("cclinks.txt", "r")
links = link_file.readlines()
z = 0

for i in range(len(links)): 
    print(i + 1) 
    outdir = "outdir/" 
    write_addr = "doc" + str(z) + ".txt"
    addr = outdir + write_addr
    z += 1
    outfile = open(addr , "a")
    url = links[i].strip()
    result = extract(fetch_url(url))
    if (result is None):
        print("error")
        continue
    out_file.write(result +"\n")
    print("done")