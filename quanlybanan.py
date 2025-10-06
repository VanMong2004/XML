from lxml import etree

# Đọc file XML
tree = etree.parse("quanlybanan.xml")

# 1. Lấy tất cả bàn
print("Tất cả bàn:", tree.xpath("//BANS/BAN"))

# 2. Lấy tất cả nhân viên
print("Tất cả nhân viên:", tree.xpath("//NHANVIENS/NHANVIEN"))

# 3. Lấy tất cả tên món
print("Tất cả tên món:", tree.xpath("//MONS/MON/TENMON/text()"))

# 4. Lấy tên nhân viên có mã NV02
print("Tên nhân viên NV02:", tree.xpath('//NHANVIEN[MANV="NV02"]/TENV/text()'))

# 5. Lấy tên và số điện thoại của nhân viên NV03
print("Tên & SDT NV03:", tree.xpath('//NHANVIEN[MANV="NV03"]/TENV/text() | //NHANVIEN[MANV="NV03"]/SDT/text()'))

# 6. Lấy tên món có giá > 50,000
print("Món giá > 50,000:", tree.xpath("//MON[number(GIA) > 50000]/TENMON/text()"))

# 7. Lấy số bàn của hóa đơn HD03
print("Số bàn hóa đơn HD03:", tree.xpath('//HOADON[SOHD="HD03"]/SOBAN/text()'))

# 8. Lấy tên món có mã M02
print("Tên món M02:", tree.xpath('//MON[MAMON="M02"]/TENMON/text()'))

# 9. Lấy ngày lập của hóa đơn HD03
print("Ngày lập HD03:", tree.xpath('//HOADON[SOHD="HD03"]/NGAYLAP/text()'))

# 10. Lấy tất cả mã món trong hóa đơn HD01
print("Mã món trong HD01:", tree.xpath('//HOADON[SOHD="HD01"]/CTHDS/CTHD/MAMON/text()'))

# 11. Lấy tên món trong hóa đơn HD01
print("Tên món trong HD01:", tree.xpath('//MON[MAMON=//HOADON[SOHD="HD01"]/CTHDS/CTHD/MAMON]/TENMON/text()'))

# 12. Lấy tên nhân viên lập hóa đơn HD02
print("Tên NV lập HD02:", tree.xpath('//NHANVIEN[MANV=//HOADON[SOHD="HD02"]/MANV]/TENV/text()'))

# 13. Đếm số bàn
print("Số lượng bàn:", tree.xpath("count(//BANS/BAN)"))

# 14. Đếm số hóa đơn lập bởi NV01
print("Số hóa đơn lập bởi NV01:", tree.xpath('count(//HOADON[MANV="NV01"])'))

# 15. Lấy tên tất cả món có trong hóa đơn của bàn số 2
print("Món trong hóa đơn bàn số 2:", tree.xpath('//MON[MAMON=//HOADON[SOBAN="2"]/CTHDS/CTHD/MAMON]/TENMON/text()'))

# 16. Lấy tất cả nhân viên từng lập hóa đơn cho bàn số 3
print("Nhân viên lập hóa đơn bàn số 3:", tree.xpath('//NHANVIEN[MANV=//HOADON[SOBAN="3"]/MANV]/TENV/text()'))

# 17. Lấy tất cả hóa đơn mà nhân viên nữ lập
print("Hóa đơn do NV nữ lập:", tree.xpath('//HOADON[MANV=//NHANVIEN[GIOITINH="Nữ"]/MANV]/SOHD/text()'))

# 18. Lấy tất cả nhân viên từng phục vụ bàn số 1
print("Nhân viên phục vụ bàn số 1:", tree.xpath('//NHANVIEN[MANV=//HOADON[SOBAN="1"]/MANV]/TENV/text()'))

# 19. Lấy tất cả món được gọi nhiều hơn 1 lần trong các hóa đơn
print("Món gọi >1 lần:", tree.xpath('//MON[MAMON=//CTHD[number(SOLUONG) > 1]/MAMON]/TENMON/text()'))

# 20. Lấy tên bàn + ngày lập hóa đơn SOHD='HD02'
print("Tên bàn của HD02:", tree.xpath('//BAN[SOBAN=//HOADON[SOHD="HD02"]/SOBAN]/TENBAN/text()'))
print("Ngày lập HD02:", tree.xpath('//HOADON[SOHD="HD02"]/NGAYLAP/text()'))
