def extract_data(filename):
    ids = []
    lat = []
    lon = []
    height = []

    with open(filename, 'r') as infile:
        infile.readline()
        
        for line in infile:
            words = line.strip().split(',')
            
            ids.append(int(words[0]))
            lat.append(float(words[1]))
            lon.append(float(words[2]))
            height.append(float(words[3]))

    return ids, lat, lon, height


def average_tree_height(height):
    return sum(height) / len(height)


def tree_deviation(avg, height):
    deviation = []
    for h in height:
        deviation.append(h - avg)
    return deviation


ids, lat, lon, height = extract_data("tree_data.csv")

avg = average_tree_height(height)
deviation = tree_deviation(avg, height)

with open("tree_data_edit.csv", "w") as outfile:
    outfile.write("id,lat,lon,height,deviation\n")
    
    for i in range(len(ids)):
        outfile.write(f"{ids[i]},{lat[i]},{lon[i]},{height[i]},{deviation[i]}\n")
