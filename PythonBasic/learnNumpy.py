import numpy as np

# a = np.array([1, 2, 3, 4, 5])
# print(a)          # → [1 2 3 4 5]
# print(a.shape)    # → (5,)  มี 5 ตัว

# # 2D array (matrix)
# m = np.array([[1, 2, 3],
#               [4, 5, 6]])
# print(m.shape)    # → (2, 3)  2 แถว 3 คอลัมน์




scores = np.array([85, 90, 78, 92, 88])

# print(scores.mean())   # → 86.6  (ค่าเฉลี่ย)
# print(scores.max())    # → 92
# print(scores.min())    # → 78
# print(scores.sum())    # → 433
print(scores.std())    # → ค่า standard deviation

# คำนวณทุกตัวพร้อมกัน
# print(scores * 2)      # → [170 180 156 184 176]
# print(scores + 5)      # → [90 95 83 97 93]





# scores = np.array([85, 90, 78, 92, 88])

# # หาตัวที่ > 85
# print(scores[scores > 85])   # → [90 92 88]

# # นับจำนวนที่ผ่านเกณฑ์
# print((scores > 85).sum())   # → 3