import os

path = "H:/workspace/Image/2018-02-02/xml"
i = 1
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path, file)):
        name = os.path.splitext(file)[0]
        num = "%06d" % (i)
        if name != num:
            print("the lack num is : %d" % (i))
            i += 1
        i += 1
print("no error!!")
