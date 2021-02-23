# 2.จงเขียนตารางสูตรคูณให้ผลลัพท์ที่ออกมาเป็นแบบตัวอย่างด้านล่างโดยใช้คำสั่ง for
for i in range(13): # กำหนดให้วน 13 รอบ เริ่มจาก 0
    if i == 0:
        continue
    elif i == 1:
        continue
    print("(**", i, "**)")
    a = 1


    for a in range(13):
        print(i, "*", a, "=", i * a)
        a += 1
    i += 1