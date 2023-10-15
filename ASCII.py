import cv2

# colorset = "MWN$@%#&B89EGA6mK5HRkbYT43V0JL7gpaseyxznocv?jIftr1li*=-~^`':;,. "
colorset = "@%#&*=-~^`':;,"

imgpath = input("Path:")
img = cv2.imread(imgpath)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.resize(gray, dsize=(int(gray.shape[1] / 2), int(gray.shape[0] / 2)))
output = ""

for gray2 in gray:
    output += "\n"
    for dark in gray2:
        output += colorset[dark // 85]*1 #255をどのくらい分けるか
        # output += colorset[dark // 4]

with open("output.txt", mode="w") as f:
    f.write(output)