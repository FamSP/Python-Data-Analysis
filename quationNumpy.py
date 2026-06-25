import numpy as np

# # โจทย์ที่ 1 — Basic Array & Stats
# # โจทย์: มีคะแนนสอบของนักเรียน 8 คน จงหา ค่าเฉลี่ย, คะแนนสูงสุด, คะแนนต่ำสุด และจำนวนคนที่ได้คะแนน >= 80
# scores = np.array([72, 85, 90, 61, 88, 77, 95, 83])

# # เขียนคำตอบตรงนี้

# print(scores.mean())
# print(scores.max())
# print(scores.min())
# print(scores.max())
# print(scores[scores >= 80])


# # โจทย์ที่ 2 — np.where
# # โจทย์: จากคะแนนชุดเดิม ให้สร้าง array ใหม่ที่บอกว่าแต่ละคน "pass" หรือ "fail" (เกณฑ์ >= 75)
# pythonscores = np.array([72, 85, 90, 61, 88, 77, 95, 83])

# # เขียนคำตอบตรงนี้
# result = np.where(pythonscores >= 75, 'pass' , 'fail')

# print(result)

# # โจทย์ที่ 3 — Filter
# # โจทย์: จากราคาสินค้า ให้ดึงเฉพาะสินค้าที่ราคาอยู่ระหว่าง 100-500 บาท
# pythonprices = np.array([50, 120, 450, 800, 99, 300, 1200, 250])

# # เขียนคำตอบตรงนี้

# condition = (pythonprices >=100) & (pythonprices <=500)
# result=pythonprices[condition]

# print(result)

# โจทย์ที่ 4 — arange + คำนวณ
# โจทย์: สร้าง array ตัวเลข 1-10 แล้วคำนวณ ผลรวม และค่าเฉลี่ย โดยไม่ต้องพิมพ์ตัวเลขเอง
# เขียนคำตอบตรงนี้

number = np.array([ 1,2,3,4,5,6,7,8,9,10])

print(number.sum())
print(number.mean())