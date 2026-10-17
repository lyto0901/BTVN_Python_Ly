# Cho chuỗi số điện thoại:
messy_phone = " 090-123 4567 "
 
# Dùng strip() để bỏ khoảng trắng.
print(messy_phone.strip())
# Dùng replace() để bỏ dấu - và khoảng trắng.
print(messy_phone.replace("-",""))
# In ra số điện thoại chuẩn hóa: 0901234567.
print(messy_phone.strip().replace("-","").replace(" ",""))