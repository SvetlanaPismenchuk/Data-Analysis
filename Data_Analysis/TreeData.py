"""
Extract_data function 
creates 4 lists.
Opens the filename.
Skips headline.
Appends index to lists.
Returns the four lists.
"""
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
'''
Average_tree_height function takes the sum of the tree heights and divides it by the number of trees.
'''

def average_tree_height(height):
    return sum(height) / len(height)

'''
Tree_deviation function creates a deviation list
and appends the deviation using height - average 
height
'''
def tree_deviation(avg, height):
    deviation = []
    for h in height:
        deviation.append(h - avg)
    return deviation


'''

Writes a new CSV file.
Adds a header line.
Loops through all tree data.
Writes id, location, height, and deviation to the file.

'''

ids, lat, lon, height = extract_data("tree_data.csv")

avg = average_tree_height(height)
deviation = tree_deviation(avg, height)

with open("tree_data_edit.csv", "w") as outfile:
    outfile.write("id,lat,lon,height,deviation\n")
    
    for i in range(len(ids)):
        outfile.write(f"{ids[i]},{lat[i]},{lon[i]},{height[i]},{deviation[i]}\n")
input()
