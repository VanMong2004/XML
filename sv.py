from lxml import etree

# Đọc file XML
tree = etree.parse("sv.xml")
root = tree.getroot()

# 1. Lấy tất cả sinh viên
print("Tất cả sinh viên: ", root.xpath("//student"))

# 2. Liệt kê tên tất cả sinh viên
print("\nTên sinh viên: ", root.xpath("//student/name/text()"))

# 3. Lấy tất cả id của sinh viên
print("\nID sinh viên: ", root.xpath("//student/id/text()"))

# 4. Lấy ngày sinh của sinh viên có id = 'SV01'
print("\nNgày sinh SV01: ", root.xpath("//student[id='SV01']/date/text()"))

# 5. Lấy các khóa học
print("\nKhóa học: ", root.xpath("//enrollment/course/text()"))

# 6. Lấy toàn bộ thông tin của sinh viên đầu tiên
print("\nSinh viên đầu tiên: ", [el.text for el in root.xpath("//student[1]/*")])

# 7. Lấy mã sinh viên đăng ký khóa học 'Vatly203'
print("\nMã sinh viên học Vatly203:")
print(root.xpath("//enrollment[course='Vatly203']/studentRef/text()"))

# 8. Lấy tên sinh viên học môn 'Toan101'
print("\nTên sinh viên học Toan101: ", root.xpath("//student[id=//enrollment[course='Toan101']/studentRef]/name/text()"))

# 9. Lấy tên sinh viên học môn 'Vatly203'
print("\nTên sinh viên học Vatly203: ", root.xpath("//student[id=//enrollment[course='Vatly203']/studentRef]/name/text()"))

# 10. Lấy ngày sinh SV01
print("\nNgày sinh SV01: ", root.xpath("//student[id='SV01']/date/text()"))

# 11. Lấy tên + ngày sinh sinh viên sinh năm 1997
print("\nSinh viên sinh năm 1997:")
print(root.xpath("//student[starts-with(date,'1997')]/name/text()"))
print(root.xpath("//student[starts-with(date,'1997')]/date/text()"))

# 12. Lấy tên sinh viên sinh trước 1998
print("\nSinh viên sinh trước 1998: ", root.xpath("//student[number(substring(date,1,4)) < 1998]/name/text()"))

# 13. Đếm tổng số sinh viên
print("\nTổng số sinh viên: ", root.xpath("count(//student)"))

# 14. Lấy tất cả sinh viên chưa đăng ký môn nào
print("\nSinh viên chưa đăng ký môn nào: ", root.xpath("//student[not(id=//enrollment/studentRef)]/name/text()"))

# 15. Lấy <date> ngay sau <name> của SV01
print("\nDate ngay sau name của SV01: ", root.xpath("//student[id='SV01']/name/following-sibling::date/text()"))

# 16. Lấy <id> ngay trước <name> của SV02
print("\nID ngay trước name của SV02: ", root.xpath("//student[id='SV02']/name/preceding-sibling::id/text()"))

# 17. Lấy toàn bộ <course> của enrollment có SV03
print("\nCourse của SV03: ", root.xpath("//enrollment[studentRef='SV03']/course/text()"))

# 18. Lấy sinh viên có họ 'Trần'
print("\nSinh viên họ Trần: ", root.xpath("//student[starts-with(name,'Trần')]/name/text()"))

# 19. Lấy năm sinh SV01
print("\nNăm sinh SV01: ", root.xpath("substring(//student[id='SV01']/date,1,4)"))
