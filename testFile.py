import os
for file in os.listdir('/home/linaro/Desktop/PhotoLibrary'):
    print file
    print file[:len(file)-4]
