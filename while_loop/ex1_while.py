#1.จงเขียนตารางสูตรคูณให้ผลลัพท์ที่ออกมาเป็นแบบตัวอย่างด้านล่างโดยใช้คำสั่ง while
row = 1
while row <= 12: 
    num = 2  
    col = 2
    while col <= 12:
        print("%3dx%2d=%3d" % (num, row, num * row), end="")
        num += 1
        col += 1

    print("")
    row += 1

print("")