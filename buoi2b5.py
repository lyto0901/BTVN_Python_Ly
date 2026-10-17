# Tạo set emails = {"a@gmail.com", "b@gmail.com", "a@gmail.com"}.
emails = {"a@gmail.com", "b@gmail.com", "a@gmail.com"}
# Quan sát kết quả khi in set ra.
print(emails)

# Thêm "c@gmail.com".
emails.add("c@gmail.com")
print(emails)

# Thử xóa "d@gmail.com" bằng remove và bằng discard, giải thích sự khác nhau."
emails.discard("d@gmail.com")
print(emails)
emails.remove("d@gmail.com")
print(emails)