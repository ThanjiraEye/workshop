#2.จงเขียนตารางสูตรคูณให้ผลลัพท์ที่ออกมาเป็นแบบตัวอย่างด้านล่างโดยใช้คำสั่ง for
for number in range(2, 13):
    for i in range(1, 13):
        result = number*i
        print("%d x %d = %d" % (number, i, result))
        print("  ")
    print("-------------------------------------------------------")
