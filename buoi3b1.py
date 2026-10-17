# Cho chuỗi: text = "  hello world  "
text = "  hello world  "
# Dùng len() để đếm số ký tự (bao gồm cả khoảng trắng)
print(len(text))
# Dùng strip() để bỏ khoảng trắng đầu và cuối, sau đó in lại chiều dài.
subtext = text.strip()
print(len(subtext))
print(len(text.strip()))