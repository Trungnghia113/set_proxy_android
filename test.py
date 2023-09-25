# -*- coding: utf-8 -*-
from CBAutoHelper import LDPlayer
from unidecode import unidecode
import time, random, imaplib, re, email, os, shutil, win32gui, requests
from PyQt5 import QtCore
from lxml import html
class RegTikTokLD:
    ref = None
    def __init__(self, index: str, mail: str, key: str, row: int):
        super().__init__()
        self.index = index
        self.mail = mail
        self.key = key
        self.row = row
    def __CreatePassword(self):
        self.pwd = unidecode(self.firstname.lower()).replace(" ", "").capitalize()+random.choice("!,@,#,$,%,&,~".split(","))+str(random.randint(10000, 99999))
    def __GetListLastNameVN(self):
        self.lastname = random.choice(["Nguyễn", "Trần", "Lê", "Phạm", "Hoàng", "Huỳnh", "Phan", "Vũ", "Võ", "Đặng", "Bùi", "Đỗ", "Hồ", "Ngô", "Dương", "Lý", "Lê Nguyễn ", "Nguyễn Lê", "Lê Phạm", "Nguyễn Trần", "Phạm Nguyễn ", "Lê Vũ", "Lê Ngọc", "Võ Thị", "Huỳnh Thị", "Hồ Thị", "Trần Ánh"])
    def __GetListFirstNameVN(self):
        self.firstname = random.choice(["Ái Hồng", "Ái Khanh", "Ái Linh", "Ái Nhân", "Ái Nhi", "Ái Thi", "Ái Thy", "Ái Vân", "An Bình", "An Di", "An Hạ", "An Hằng", "An Nhàn", "An Nhiên", "Anh Chi", "Ánh Dương", "Ánh Hoa", "Ánh Hồng", "Anh Hương", "Ánh Lệ", "Ánh Linh", "Anh Mai", "Ánh Mai", "Ánh Ngọc", "Ánh Nguyệt", "Anh Phương", "Anh Thảo", "Anh Thi", "Anh Thơ", "Ánh Thơ", "Anh Thư", "Anh Thy", "Ánh Trang", "Ánh Tuyết", "Ánh Xuân", "Bạch Cúc", "Bạch Hoa", "Bạch Kim", "Bạch Liên", "Bạch Loan", "Bạch Mai", "Bạch Quỳnh", "Bạch Trà", "Bạch Tuyết", "Bạch Vân", "Bạch Yến", "Ban Mai", "Băng Băng", "Băng Tâm", "Bảo Anh", "Bảo Bình", "Bảo Châu", "Bảo Hà", "Bảo Hân", "Bảo Huệ", "Bảo Lan", "Bảo Lễ", "Bảo Ngọc", "Bảo Phương", "Bảo Quyên", "Bảo Quỳnh", "Bảo Thoa", "Bảo Thúy", "Bảo Tiên", "Bảo Trâm", "Bảo Trân", "Bảo Trúc", "Bảo Uyên", "Bảo Vân", "Bảo Vy", "Bích Châu", "Bích Chiêu", "Bích Dào", "Bích Duyên", "Bích Hà", "Bích Hải", "Bích Hằng", "Bích Hạnh", "Bích Hảo", "Bích Hậu", "Bích Hiền", "Bích Hồng", "Bích Hợp", "Bích Huệ", "Bích Lam", "Bích Liên", "Bích Loan", "Bích Nga", "Bích Ngà", "Bích Ngân", "Bích Ngọc", "Bích Như", "Bích Phượng", "Bích Quân", "Bích Quyên", "Bích San", "Bích Thảo", "Bích Thoa", "Bích Thu", "Bích Thủy", "Bích Ty", "Bích Vân", "Bội Linh", "Cẩm Hạnh", "Cẩm Hiền", "Cẩm Hường", "Cẩm Liên", "Cẩm Linh", "Cẩm Ly", "Cẩm Nhi", "Cẩm Nhung", "Cam Thảo", "Cẩm Thúy", "Cẩm Tú", "Cẩm Vân", "Cẩm Yến", "Cát Cát", "Cát Linh", "Cát Ly", "Cát Tiên", "Chi Lan", "Chi Mai", "Dã Lan", "Dạ Lan", "Dạ Nguyệt", "Dã Thảo", "Dạ Thảo", "Dạ Thi", "Dạ Yến", "Di Nhiên", "Diễm Châu", "Diễm Chi", "Diễm Hằng", "Diễm Hạnh", "Diễm Hương", "Diễm Khuê", "Diễm Kiều", "Diễm Liên", "Diễm Lộc", "Diễm My", "Diễm Phúc", "Diễm Phước", "Diễm Phương", "Diễm Phượng", "Diễm Quyên", "Diễm Quỳnh", "Diễm Thảo", "Diễm Thư", "Diễm Thúy", "Diễm Trang", "Diễm Trinh", "Diễm Uyên", "Diên Vỹ", "Diệp Anh", "Diệp Vy", "Diệu Ái", "Diệu Anh", "Diệu Hằng", "Diệu Hạnh", "Diệu Hiền", "Diệu Hoa", "Diệu Hồng", "Diệu Hương", "Diệu Huyền", "Diệu Lan", "Diệu Linh", "Diệu Loan", "Diệu Nga", "Diệu Ngà", "Diệu Ngọc", "Diệu Nương", "Diệu Thiện", "Diệu Thúy", "Diệu Vân", "Duy Hạnh", "Duy Mỹ", "Duy Uyên", "Duyên Hồng", "Duyên My", "Duyên Mỹ", "Duyên Nương", "Dinh Hương", "Doan Thanh", "Doan Trang", "Dông Nghi", "Dông Nhi", "Dông Trà", "Dông Tuyền", "Dông Vy", "Gia Hân", "Gia Khanh", "Gia Linh", "Gia Nhi", "Gia Quỳnh", "Giáng Ngọc", "Giang Thanh", "Giáng Tiên", "Giáng Uyên", "Giao Kiều", "Giao Linh", "Hà Giang", "Hà Liên", "Hà Mi", "Hà My", "Hà Nhi", "Hà Phương", "Hạ Phương", "Hà Thanh", "Hà Tiên", "Hạ Tiên", "Hạ Uyên", "Hạ Vy", "Hạc Cúc", "Hải Ân", "Hải Anh", "Hải Châu", "Hải Dường", "Hải Duyên", "Hải Miên", "Hải My", "Hải Mỹ", "Hải Ngân", "Hải Nhi", "Hải Phương", "Hải Phượng", "Hải San", "Hải Sinh", "Hải Thanh", "Hải Thảo", "Hải Uyên", "Hải Vân", "Hải Vy", "Hải Yến", "Hàm Duyên", "Hàm Nghi", "Hàm Thơ", "Hằng Anh", "Hạnh Chi", "Hạnh Dung", "Hạnh Linh", "Hạnh My", "Hạnh Nga", "Hạnh Phương", "Hạnh San", "Hạnh Thảo", "Hạnh Trang", "Hạnh Vi", "Hảo Nhi", "Hiền Chung", "Hiền Hòa", "Hiền Mai", "Hiền Nhi", "Hiền Nương", "Hiền Thục", "Hiếu Giang", "Hiếu Hạnh", "Hiếu Khanh", "Hiếu Minh", "Hiểu Vân", "Hồ Diệp", "Hoa Liên", "Hoa Lý", "Họa Mi", "Hoa Thiên", "Hoa Tiên", "Hoài An", "Hoài Giang", "Hoài Hương", "Hoài Phương", "Hoài Thương", "Hoài Trang", "Hoàn Châu", "Hoàn Vi", "Hoàng Cúc", "Hoàng Hà", "Hoàng Kim", "Hoàng Lan", "Hoàng Mai", "Hoàng Miên", "Hoàng Oanh", "Hoàng Sa", "Hoàng Thư", "Hoàng Yến", "Hồng Anh", "Hồng Bạch Thảo", "Hồng Châu", "Hồng Dào", "Hồng Diễm", "Hồng Diệp", "Hồng Hà", "Hồng Hạnh", "Hồng Hoa", "Hồng Khanh", "Hồng Khôi", "Hồng Khuê", "Hồng Lâm", "Hồng Liên", "Hồng Linh", "Hồng Mai", "Hồng Nga", "Hồng Ngân", "Hồng Ngọc", "Hồng Như", "Hồng Nhung", "Hồng Oanh", "Hồng Phúc", "Hồng Phương", "Hồng Quế", "Hồng Tâm", "Hồng Thắm", "Hồng Thảo", "Hồng Thu", "Hồng Thư", "Hồng Thúy", "Hồng Thủy", "Hồng Vân", "Hồng Xuân", "Huệ An", "Huệ Hồng", "Huệ Hương", "Huệ Lâm", "Huệ Lan", "Huệ Linh", "Huệ My", "Huệ Phương", "Huệ Thương", "Hương Chi", "Hương Giang", "Hương Lâm", "Hương Lan", "Hương Liên", "Hương Ly", "Hương Mai", "Hương Nhi", "Hương Thảo", "Hương Thu", "Hương Thủy", "Hương Tiên", "Hương Trà", "Hương Trang", "Hương Xuân", "Huyền Anh", "Huyền Diệu", "Huyền Linh", "Huyền Ngọc", "Huyền Nhi", "Huyền Thoại", "Huyền Thư", "Huyền Trâm", "Huyền Trân", "Huyền Trang", "Huỳnh Anh", "Khả Ái", "Khả Khanh", "Khả Tú", "Khải Hà", "Khánh Chi", "Khánh Giao", "Khánh Hà", "Khánh Hằng", "Khánh Huyền", "Khánh Linh", "Khánh Ly", "Khánh Mai", "Khánh My", "Khánh Ngân", "Khánh Quyên", "Khánh Quỳnh", "Khánh Thủy", "Khánh Trang", "Khánh Vân", "Khánh Vi", "Khuê Trung", "Kiết Hồng", "Kiết Trinh", "Kiều Anh", "Kiều Diễm", "Kiều Dung", "Kiều Giang", "Kiều Hạnh", "Kiều Hoa", "Kiều Khanh", "Kiều Loan", "Kiều Mai", "Kiều Minh", "Kiều Mỹ", "Kiều Nga", "Kiều Nguyệt", "Kiều Nương", "Kiều Thu", "Kiều Trang", "Kiều Trinh", "Kim Anh", "Kim Ánh", "Kim Chi", "Kim Cương", "Kim Dung", "Kim Duyên", "Kim Hoa", "Kim Hương", "Kim Khanh", "Kim Lan", "Kim Liên", "Kim Loan", "Kim Ly", "Kim Mai", "Kim Ngân", "Kim Ngọc", "Kim Oanh", "Kim Phượng", "Kim Quyên", "Kim Sa", "Kim Thanh", "Kim Thảo", "Kim Thoa", "Kim Thu", "Kim Thư", "Kim Thủy", "Kim Thy", "Kim Trang", "Kim Tuyến", "Kim Tuyền", "Kim Tuyết", "Kim Xuân", "Kim Xuyến", "Kim Yến", "Kỳ Anh", "Kỳ Duyên", "Lam Hà", "Lam Khê", "Lam Ngọc", "Lâm Nhi", "Lâm Oanh", "Lam Tuyền", "Lâm Tuyền", "Lâm Uyên", "Lan Anh", "Lan Chi", "Lan Hương", "Lan Khuê", "Lan Ngọc", "Lan Nhi", "Lan Phương", "Lan Thương", "Lan Trúc", "Lan Vy", "Lệ Băng", "Lệ Chi", "Lệ Hoa", "Lệ Huyền", "Lệ Khanh", "Lệ Nga", "Lệ Nhi", "Lệ Quân", "Lệ Quyên", "Lê Quỳnh", "Lệ Thanh", "Lệ Thu", "Lệ Thủy", "Liên Chi", "Liên Hoa", "Liên Hương", "Liên Như", "Liên Phương", "Liên Trân", "Liễu Oanh", "Linh Châu", "Linh Chi", "Linh Dan", "Linh Duyên", "Linh Giang", "Linh Hà", "Linh Lan", "Linh Nhi", "Linh Phương", "Linh Phượng", "Linh San", "Linh Trang", "Loan Châu", "Lộc Uyên", "Lục Bình", "Lưu Ly", "Ly Châu", "Mai Anh", "Mai Châu", "Mai Chi", "Mai Hà", "Mai Hạ", "Mai Hiền", "Mai Hương", "Mai Khanh", "Mai Khôi", "Mai Lan", "Mai Liên", "Mai Linh", "Mai Loan", "Mai Ly", "Mai Nhi", "Mai Phương", "Mai Quyên", "Mai Tâm", "Mai Thanh", "Mai Thảo", "Mai Thu", "Mai Thy", "Mai Trinh", "Mai Vy", "Mậu Xuân", "Minh An", "Minh Châu", "Minh Duyên", "Minh Hà", "Minh Hằng", "Minh Hạnh", "Minh Hiền", "Minh Hồng", "Minh Huệ", "Minh Hương", "Minh Huyền", "Minh Khai", "Minh Khuê", "Minh Loan", "Minh Minh", "Minh Ngọc", "Minh Nguyệt", "Minh Nhi", "Minh Như", "Minh Phương", "Minh Phượng", "Minh Tâm", "Minh Thảo", "Minh Thu", "Minh Thư", "Minh Thương", "Minh Thúy", "Minh Thủy", "Minh Trang", "Minh Tuệ", "Minh Tuyết", "Minh Uyên", "Minh Vy", "Minh Xuân", "Minh Yến", "Mộc Miên", "Mộng Diệp", "Mộng Hằng", "Mộng Hoa", "Mộng Hương", "Mộng Lan", "Mộng Liễu", "Mộng Nguyệt", "Mộng Nhi", "Mộng Quỳnh", "Mộng Thi", "Mộng Thu", "Mộng Tuyền", "Mộng Vân", "Mộng Vi", "Mộng Vy", "Mỹ Anh", "Mỹ Diễm", "Mỹ Dung", "Mỹ Duyên", "Mỹ Hạnh", "Mỹ Hiệp", "Mỹ Hoàn", "Mỹ Huệ", "Mỹ Hường", "Mỹ Huyền", "Mỹ Khuyên", "Mỹ Kiều", "Mỹ Lan", "Mỹ Lệ", "Mỹ Loan", "Mỹ Lợi", "Mỹ Nga", "Mỹ Ngọc", "Mỹ Nhi", "Mỹ Nương", "Mỹ Phụng", "Mỹ Phương", "Mỹ Phượng", "Mỹ Tâm", "Mỹ Thuần", "Mỹ Thuận", "Mỹ Trâm", "Mỹ Trang", "Mỹ Uyên", "Mỹ Vân", "Mỹ Xuân", "Mỹ Yến", "Ngân Anh", "Ngân Hà", "Ngân Thanh", "Ngân Trúc", "Nghi Dung", "Nghi Minh", "Nghi Xuân", "Ngọc Ái", "Ngọc Anh", "Ngọc Ánh", "Ngọc Bích", "Ngọc Cầm", "Ngọc Dàn", "Ngọc Dào", "Ngọc Diệp", "Ngọc Diệp", "Ngọc Dung", "Ngọc Hà", "Ngọc Hạ", "Ngọc Hân", "Ngọc Hằng", "Ngọc Hạnh", "Ngọc Hiền", "Ngọc Hoa", "Ngọc Hoan", "Ngọc Hoàn", "Ngọc Huệ", "Ngọc Huyền", "Ngọc Khanh", "Ngọc Khánh", "Ngọc Khuê", "Ngọc Lam", "Ngọc Lâm", "Ngọc Lan", "Ngọc Lệ", "Ngọc Liên", "Ngọc Linh", "Ngọc Loan", "Ngọc Mai", "Ngọc Nhi", "Ngọc Nữ", "Ngọc Oanh", "Ngọc Phụng", "Ngọc Quế", "Ngọc Quyên", "Ngọc Quỳnh", "Ngọc San", "Ngọc Sương", "Ngọc Tâm", "Ngọc Thi", "Ngọc Thơ", "Ngọc Thy", "Ngọc Trâm", "Ngọc Trinh", "Ngọc Tú", "Ngọc Tuyết", "Ngọc Uyên", "Ngọc Uyển", "Ngọc Vân", "Ngọc Vy", "Ngọc Yến", "Nguyên Hồng", "Nguyên Thảo", "Nguyết Ánh", "Nguyệt Anh", "Nguyệt Ánh", "Nguyệt Cầm", "Nguyệt Cát", "Nguyệt Hà", "Nguyệt Hồng", "Nguyệt Lan", "Nguyệt Minh", "Nguyệt Nga", "Nguyệt Quế", "Nguyệt Uyển", "Nhã Hồng", "Nhã Hương", "Nhã Khanh", "Nhã Lý", "Nhã Mai", "Nhã Sương", "Nhã Thanh", "Nhã Trang", "Nhã Trúc", "Nhã Uyên", "Nhã Ý", "Nhã Yến", "Nhan Hồng", "Nhật Ánh", "Nhật Hà", "Nhật Hạ", "Nhật Lan", "Nhật Linh", "Nhật Mai", "Nhật Phương", "Nhất Thương", "Như Anh", "Như Bảo", "Như Hoa", "Như Hồng", "Như Loan", "Như Mai", "Như Ngà", "Như Ngọc", "Như Phương", "Như Quân", "Như Quỳnh", "Như Tâm", "Như Thảo", "Oanh Thơ", "Oanh Vũ", "Phi Nhung", "Phi Yến", "Phụng Yến", "Phước Bình", "Phước Huệ", "Phương An", "Phương Anh", "Phượng Bích", "Phương Châu", "Phương Chi", "Phương Diễm", "Phương Dung", "Phương Giang", "Phương Hạnh", "Phương Hiền", "Phương Hoa", "Phương Lan", "Phượng Lệ", "Phương Liên", "Phượng Liên", "Phương Linh", "Phương Loan", "Phượng Loan", "Phương Mai", "Phượng Nga", "Phương Nghi", "Phương Ngọc", "Phương Nhi", "Phương Nhung", "Phương Quân", "Phương Quế", "Phương Quyên", "Phương Quỳnh", "Phương Tâm", "Phương Thanh", "Phương Thảo", "Phương Thi", "Phương Thùy", "Phương Thủy", "Phượng Tiên", "Phương Trà", "Phương Trâm", "Phương Trang", "Phương Trinh", "Phương Uyên", "Phượng Uyên", "Phượng Vũ", "Phượng Vy", "Phương Yến", "Quế Anh", "Quế Chi", "Quế Lâm", "Quế Linh", "Quế Phương", "Quế Thu", "Quỳnh Anh", "Quỳnh Chi", "Quỳnh Dung", "Quỳnh Giang", "Quỳnh Giao", "Quỳnh Hà", "Quỳnh Hoa", "Quỳnh Hương", "Quỳnh Lam", "Quỳnh Lâm", "Quỳnh Liên", "Quỳnh Nga", "Quỳnh Ngân", "Quỳnh Nhi", "Quỳnh Như", "Quỳnh Nhung", "Quỳnh Phương", "Quỳnh Sa", "Quỳnh Thanh", "Quỳnh Thơ", "Quỳnh Tiên", "Quỳnh Trâm", "Quỳnh Trang", "Quỳnh Vân", "Sao Băng", "Sao Mai", "Sơn Ca", "Sơn Tuyền", "Sông Hà", "Sông Hương", "Song Oanh", "Song Thư", "Sương Sương", "Tâm Hằng", "Tâm Hạnh", "Tâm Hiền", "Tâm Khanh", "Tâm Linh", "Tâm Nguyên", "Tâm Nguyệt", "Tâm Nhi", "Tâm Như", "Tâm Thanh", "Tâm Trang", "Thạch Thảo", "Thái Chi", "Thái Hà", "Thái Hồng", "Thái Lâm", "Thái Lan", "Thái Tâm", "Thái Thanh", "Thái Thảo", "Thái Vân", "Thanh Bình", "Thanh Dân", "Thanh Giang", "Thanh Hà", "Thanh Hằng", "Thanh Hạnh", "Thanh Hảo", "Thanh Hiền", "Thanh Hiếu", "Thanh Hoa", "Thanh Hồng", "Thanh Hương", "Thanh Hường", "Thanh Huyền", "Thanh Kiều", "Thanh Lam", "Thanh Lâm", "Thanh Lan", "Thanh Loan", "Thanh Mai", "Thanh Mẫn", "Thanh Nga", "Thanh Ngân", "Thanh Ngọc", "Thanh Nguyên", "Thanh Nhã", "Thanh Nhàn", "Thanh Nhung", "Thanh Phương", "Thanh Tâm", "Thanh Thanh", "Thanh Thảo", "Thanh Thu", "Thanh Thư", "Thanh Thúy", "Thanh Thủy", "Thanh Trang", "Thanh Trúc", "Thanh Tuyền", "Thanh Tuyết", "Thanh Uyên", "Thanh Vân", "Thanh Vy", "Thanh Xuân", "Thanh Yến", "Thảo Hồng", "Thảo Hương", "Thảo Linh", "Thảo Ly", "Thảo Mai", "Thảo My", "Thảo Nghi", "Thảo Nguyên", "Thảo Nhi", "Thảo Quyên", "Thảo Trang", "Thảo Uyên", "Thảo Vân", "Thảo Vy", "Thi Cầm", "Thi Ngôn", "Thi Thi", "Thi Xuân", "Thi Yến", "Thiên Di", "Thiên Duyên", "Thiên Giang", "Thiên Hà", "Thiên Hương", "Thiên Khánh", "Thiên Kim", "Thiên Lam", "Thiên Lan", "Thiên Mai", "Thiên Mỹ", "Thiện Mỹ", "Thiên Nga", "Thiên Nương", "Thiên Phương", "Thiên Thanh", "Thiên Thảo", "Thiên Thêu", "Thiên Thư", "Thiện Tiên", "Thiên Trang", "Thiên Tuyền", "Thiều Ly", "Thiếu Mai", "Thơ Thơ", "Thu Duyên", "Thu Giang", "Thu Hà", "Thu Hằng", "Thu Hậu", "Thu Hiền", "Thu Hoài", "Thu Hồng", "Thu Huệ", "Thu Huyền", "Thư Lâm", "Thu Liên", "Thu Linh", "Thu Loan", "Thu Mai", "Thu Minh", "Thu Nga", "Thu Ngà", "Thu Ngân", "Thu Ngọc", "Thu Nguyệt", "Thu Nhiên", "Thu Oanh", "Thu Phong", "Thu Phương", "Thu Phượng", "Thu Sương", "Thư Sương", "Thu Thảo", "Thu Thuận", "Thu Thủy", "Thu Trang", "Thu Vân", "Thu Việt", "Thu Vọng", "Thu Yến", "Thuần Hậu", "Thục Anh", "Thục Dào", "Thục Dình", "Thục Doan", "Thục Khuê", "Thục Nhi", "Thục Oanh", "Thục Quyên", "Thục Tâm", "Thục Trang", "Thục Trinh", "Thục Uyên", "Thục Vân", "Thương Huyền", "Thương Nga", "Thương Thương", "Thúy Anh", "Thùy Anh", "Thụy Dào", "Thúy Diễm", "Thùy Dung", "Thùy Dương", "Thùy Giang", "Thúy Hà", "Thúy Hằng", "Thủy Hằng", "Thúy Hạnh", "Thúy Hiền", "Thủy Hồng", "Thúy Hương", "Thúy Hường", "Thúy Huyền", "Thụy Khanh", "Thúy Kiều", "Thụy Lâm", "Thúy Liên", "Thúy Liễu", "Thùy Linh", "Thủy Linh", "Thụy Linh", "Thúy Loan", "Thúy Mai", "Thùy Mi", "Thúy Minh", "Thủy Minh", "Thúy My", "Thùy My", "Thúy Nga", "Thúy Ngà", "Thúy Ngân", "Thúy Ngọc", "Thủy Nguyệt", "Thùy Nhi", "Thùy Như", "Thụy Nương", "Thùy Oanh", "Thúy Phượng", "Thúy Quỳnh", "Thủy Quỳnh", "Thủy Tâm", "Thủy Tiên", "Thụy Trâm", "Thủy Trang", "Thụy Trinh", "Thùy Uyên", "Thụy Uyên", "Thúy Vân", "Thùy Vân", "Thụy Vân", "Thúy Vi", "Thúy Vy", "Thy Khanh", "Thy Oanh", "Thy Trúc", "Thy Vân", "Tiên Phương", "Tiểu Quỳnh", "Tịnh Lâm", "Tịnh Nhi", "Tịnh Như", "Tịnh Tâm", "Tịnh Yên", "Tố Loan", "Tố Nga", "Tố Nhi", "Tố Quyên", "Tố Tâm", "Tố Uyên", "Trà Giang", "Trà My", "Trâm Anh", "Trầm Hương", "Trâm Oanh", "Trang Anh", "Trang Dài", "Trang Linh", "Trang Nhã", "Trang Tâm", "Triệu Mẫn", "Triều Nguyệt", "Triều Thanh", "Trúc Chi", "Trúc Dào", "Trúc Lam", "Trúc Lâm", "Trúc Lan", "Trúc Liên", "Trúc Linh", "Trúc Loan", "Trúc Ly", "Trúc Mai", "Trúc Phương", "Trúc Quỳnh", "Trúc Vân", "Trúc Vy", "Từ Ân", "Tú Anh", "Tú Ly", "Tú Nguyệt", "Tú Quyên", "Tú Quỳnh", "Tú Sương", "Tú Tâm", "Tú Trinh", "Tú Uyên", "Tuệ Lâm", "Tuệ Mẫn", "Tuệ Nhi", "Tường Vi", "Tường Vy", "Tùy Anh", "Tùy Linh", "Túy Loan", "Tuyết Anh", "Tuyết Băng", "Tuyết Chi", "Tuyết Hân", "Tuyết Hoa", "Tuyết Hương", "Tuyết Lâm", "Tuyết Lan", "Tuyết Loan", "Tuyết Mai", "Tuyết Nga", "Tuyết Nhi", "Tuyết Nhung", "Tuyết Oanh", "Tuyết Tâm", "Tuyết Thanh", "Tuyết Trầm", "Tuyết Trinh", "Tuyết Vân", "Tuyết Vy", "Tuyết Xuân", "Uyển Khanh", "Uyển My", "Uyển Nghi", "Uyển Nhã", "Uyên Nhi", "Uyển Nhi", "Uyển Như", "Uyên Phương", "Uyên Thi", "Uyên Thơ", "Uyên Thy", "Uyên Trâm", "Uyên Vi", "Vân Anh", "Vân Chi", "Vân Du", "Vân Hà", "Vân Hương", "Vân Khanh", "Vân Khánh", "Vân Linh", "Vân Ngọc", "Vân Nhi", "Vân Phi", "Vân Thanh", "Vân Thường", "Vân Thúy", "Vân Tiên", "Vân Trang", "Vân Trinh", "Vàng Lưu", "Vành Khuyên", "Vi Quyên", "Việt Hà", "Việt Hương", "Việt Khuê", "Việt Mi", "Việt Nga", "Việt Nhi", "Việt Thi", "Việt Trinh", "Việt Tuyết", "Việt Yến", "Vũ Hồng", "Vy Lam", "Vy Lan", "Xuân Bảo", "Xuân Dung", "Xuân Hân", "Xuân Hạnh", "Xuân Hiền", "Xuân Hoa", "Xuân Hương", "Xuân Lâm", "Xuân Lan", "Xuân Lan", "Xuân Liễu", "Xuân Linh", "Xuân Loan", "Xuân Mai", "Xuân Nghi", "Xuân Ngọc", "Xuân Nhi", "Xuân Nương", "Xuân Phương", "Xuân Tâm", "Xuân Thanh", "Xuân Thảo", "Xuân Thu", "Xuân Thủy", "Xuân Trang", "Xuân Uyên", "Xuân Vân", "Xuân Yến", "Xuyến Chi", "Yến Dan", "Yến Hồng", "Yến Loan", "Yên Mai", "Yến Mai", "Yến My", "Yên Nhi", "Yến Nhi", "Yến Oanh", "Yến Phương", "Yến Phượng", "Yến Thanh", "Yến Thảo", "Yến Trâm", "Yến Trinh"])
    def __CreateUserId(self):
        self.userid = unidecode(self.firstname.lower()).replace(" ", "")+str(random.randint(100000, 999999))
    def __CheckBirthday(self):
        if self.CheckXml(CountRepeat=3, element='//node[@content-desc="Ngày sinh của bạn là ngày nào?"]', index=0): return True
        return False
    def __BirthDay(self):
        ld = self.ld
        pos = ld.GetPosXml('//node[@class="com.bytedance.ies.xelement.pickview.LynxPickerViewColumn"]')
        for month in range(random.randint(0, 3)):
            month = pos[0]
            ld.Click(month[0], month[1]) # 1click 3 tháng
        for day in range(random.randint(0, 5)):
            day = pos[1]
            ld.Click(day[0], day[1]) # 1click 3 ngày
        for year in range(random.randint(8, 13)):
            year = pos[2]
            ld.Click(year[0], year[1]) # 1click 3 năm
    def __GetCodeOutlook(self):
        email_user, email_pass = self.mail.split("|")[0], self.mail.split("|")[1]
        try:
            mail = imaplib.IMAP4_SSL('outlook.office365.com')
            mail.login(email_user, email_pass)
            status, messages = mail.select("INBOX")
            messages = int(messages[0])
            for num in range(messages, messages-3, -1):
                __, data = mail.fetch(str(num), '(RFC822)')
                for response in data:
                    if isinstance(response, tuple):
                        msg = email.message_from_bytes(response[1])
                        k = re.findall('<p style=3D"font-family:arial;color:blue;font-size:20px;">  .*?   <p>', str(msg))
                        if k != []:
                            code = re.findall('\d{6}', k[0])[0]
                            return code
                        else:
                            return []
            mail.close()
            mail.logout()
        except:
            return []
    def CheckImage(self, path, index=1):
        for i in range(10):
            x, y = self.ld.FindImg(path)
            if x:
                for j in range(index):
                    self.ld.Click(x, y)
                    # print("Đã click image", path, (x, y))
                return True
        return False
    def CheckXml(self, CountRepeat=15, element=None, index=0, Xoffsetplus=0, Yoffsetplus=0):
        for i in range(CountRepeat):
            pos = self.ld.GetPosXml(element)
            if pos != []:
                pos = pos[index]
                self.ld.Click(pos[0]+Xoffsetplus, pos[1]+Yoffsetplus)    
                # print("Đã click", element)
                return True
        return False
    def FindElement(self, element, index, attribute):
        try:
            tree = html.parse(f"window_dump_{self.index}.xml").xpath(element)[index].attrib[attribute]
            return tree
        except:
            return False
    def __GetProxy(self, key):
        if self.ref.ref.chooseproxy.currentText() == "Tinsoft":
            while True:
                ip = requests.get(f"http://proxy.tinsoftsv.com/api/changeProxy.php?key={key}&location=0").json()
                if ip["success"]:
                    return ip["proxy"]
                else:
                    if "wrong key!" in str(ip):
                        return "KEYEXPIRED"
                    for ll in range(ip["next_change"], -1, -1):
                        self.ref.show.emit(self.row, 3, f"Vui lòng đợi {str(ll)} để đổi ip lần nữa")
                        time.sleep(1) 
        elif self.ref.ref.chooseproxy.currentText() == "TMProxy":
            while True:
                ip = requests.post(f"https://tmproxy.com/api/proxy/get-new-proxy", data='{"api_key": "%s","id_location": 0}'%key).json()
                if ip["code"] == 0:
                    return ip["data"]["https"]
                elif ip["code"] == 6:
                    return "KEYEXPIRED"
                else:  
                    for ll in range(ip["data"]["next_request"], -1, -1):
                        self.ref.show.emit(self.row, 3, f"Vui lòng đợi {str(ll)} để đổi ip lần nữa")
                        time.sleep(1)
        elif self.ref.ref.chooseproxy.currentText() == "Proxy.shoplike.vn":
            while True:
                ip = requests.get(f"http://proxy.shoplike.vn/Api/getNewProxy?access_token={key}&location=&provider=").json()
                print(ip)
                if ip["status"] == "success":
                    return ip["data"]["proxy"]
                else:  
                    if "Key khong ton tai hoac da het han" in str(ip):
                        return "KEYEXPIRED"
                    if "Het proxy, thu lai sau" in str(ip):
                        for t in range(60, -1, -1):
                            self.ref.show.emit(self.row, 3, f"Hết Proxy đang đợi {t} giây lấy lại")
                            time.sleep(1)
                        continue
                    for ll in range(int(ip["nextChange"]), -1, -1):
                        self.ref.show.emit(self.row, 3, f"Vui lòng đợi {str(ll)} để đổi ip lần nữa")
                        time.sleep(1)
    def __SetProxy(self, proxy, username=None, password=None):
        self.ld.RemoveProxy()
        try:
            ld = self.ld
            self.ref.show.emit(self.row, 3, "Đang setproxy......")
            ip, port = proxy.split(":")[0], proxy.split(":")[1]
            ld.OpenApp('com.cell47.College_Proxy')
            time.sleep(5)
            # caanf 1 cais thooi vi nos hien het r
            self.CheckXml(CountRepeat=50, element='//node[@resource-id="com.cell47.College_Proxy:id/editText_address"]')
            if self.FindElement('//node[@resource-id="com.cell47.College_Proxy:id/editText_address"]', index=0, attribute="text") != "": ld.KeyEvent('KEYCODE_DPAD_DOWN')
            self.__DeleteText(20)
            ld.SendText(VN=ip)
            pos = ld.GetPosXml('//node[@resource-id="com.cell47.College_Proxy:id/editText_port"]')[0]
            ld.Click(pos[0], pos[1])
            if self.FindElement('//node[@resource-id="com.cell47.College_Proxy:id/editText_port"]', index=0, attribute="text") != "": ld.KeyEvent('KEYCODE_DPAD_DOWN')
            self.__DeleteText(5)
            ld.SendText(VN=port)
            if username != None and password != None:
                pos = ld.GetPosXml('//node[@resource-id="com.cell47.College_Proxy:id/editText_username"]')[0]
                ld.Click(pos[0], pos[1])
                ld.SendText(username)
                pos = ld.GetPosXml('//node[@resource-id="com.cell47.College_Proxy:id/textView_password"]')[0]
                ld.Click(pos[0], pos[1])
                ld.SendText(password)
            pos = ld.GetPosXml('//node[@text="START PROXY SERVICE"]')[0]
            ld.Click(pos[0], pos[1])
            self.CheckXml(element='//node[@resource-id="android:id/button1"]')
            pos = ld.GetPosXml('//node[@text="OK"]')
            if pos != []:
                pos = pos[0]
                ld.Click(pos[0], pos[1])
            time.sleep(10)
            self.CheckXml(element='//node[@resource-id="android:id/button1"]')
        except:
            return "FAIL"
    def __PublicTym(self):
        ld = self.ld
        self.ref.show.emit(self.row, 3, "Đang public tym......")
        self.CheckImage("./images/tuychon.png")
        if self.CheckXml(element='//node[@text="Quyền riêng tư" or @text="Privacy"]') != True: return
        time.sleep(1)
        ld.Swipe(300, 400, 300, -1000)
        if self.CheckXml(element='//node[@text="Video đã thích" and @class="com.lynx.tasm.behavior.ui.text.UIText"]') != True: return 
        if self.CheckXml(element='//node[@text="Mọi người" and @class="com.lynx.tasm.behavior.ui.text.FlattenUIText"]') != True: return
        for i in range(3):
            ld.KeyEvent("KEYCODE_BACK")
    def __RandomPictures(self):
        if os.path.exists(self.ref.ref.folderavt.text()) == False:
            return "NO_PATH_IMAGE"
        image = random.choice(os.listdir(self.ref.ref.folderavt.text()))
        string = ""
        char = "qwertyuiopasdfghmcnvxbcz"
        for i in range(10):
            string += char[random.randint(0, len(char)-1)]
        self.document = os.path.expanduser('~\Documents')+"\\LDPlayer\\Applications\\"+string
        os.mkdir(self.document)
        shutil.copyfile(self.ref.ref.folderavt.text()+'/'+image, self.document+"\\"+image)
        return string
    def __RemoveImage(self):
        try: shutil.rmtree(self.document)
        except: pass
    def __DeleteText(self, repeat):
        string = "KEYCODE_DEL"
        for i in range(repeat-1):
            string += " KEYCODE_DEL"
        self.ld.KeyEvent(string) # xóa tên hiện tại
    def __ChangeName(self):
        self.ref.show.emit(self.row, 3, "Đang thay tên......")
        time.sleep(1)
        self.CheckImage("./images/suahoso.png")
        time.sleep(1)
        self.CheckXml(element='//node[@text="Tên"]')
        self.__DeleteText(35)
        self.ld.SendText(VN=self.lastname+" "+self.firstname)
        time.sleep(1)
        self.CheckXml(element='//node[@text="Lưu" and @class="com.lynx.tasm.behavior.ui.text.FlattenUIText"]')
        self.ld.KeyEvent("KEYCODE_BACK")
        self.ld.KeyEvent("KEYCODE_BACK")
        time.sleep(3)
    def __ChangeUserId(self):
        self.ref.show.emit(self.row, 3, "Đang sửa userid......")
        time.sleep(1)
        # self.CheckXml(element='//node[@class="com.lynx.tasm.ui.image.UIImage"]', index=-1)
        self.__DeleteText(35)
        self.ld.SendText(VN=self.userid)
        time.sleep(1)
        self.CheckXml(element='//node[@text="Đăng ký" and @class="com.lynx.tasm.behavior.ui.view.UIView"]', index=-1, Xoffsetplus=10, Yoffsetplus=10)
        time.sleep(1)
        for swipe in range(5):
            self.ld.Swipe(100, 500, 100, -1000)
    def __UpAvatar(self):
        file = self.__RandomPictures()
        if file == "NO_PATH_IMAGE": 
            self.ref.show.emit(self.row, 3, file)
            return 
        self.ref.show.emit(self.row, 3, "Đang upavatar......")
        time.sleep(1)
        self.CheckImage("./images/suahoso.png")
        self.CheckXml(element='//node[@class="com.lynx.tasm.ui.image.UIImage"]')
        self.CheckImage("./images/chontuthuvien.png")
        time.sleep(1)
        self.CheckXml(CountRepeat=1, element='//node[@resource-id="com.android.documentsui:id/toolbar"]', Xoffsetplus=10)
        self.CheckXml(element='//node[@text="File Manager"]')
        self.CheckXml(element='//node[@text="Applications"]')
        for i in range(20):
            if self.CheckXml(CountRepeat=1,element=f'//node[@text="{file}"]') != True: self.ld.Swipe(100, 400, 100, 200) 
            else: break
        self.CheckXml(element='//node[@resource-id="com.cyanogenmod.filemanager:id/navigation_view_item_name" and @text!=".."]')
        time.sleep(1)
        self.CheckXml(element='//node[@class="android.view.View"]', index=-1, Xoffsetplus=10, Yoffsetplus=10)
        time.sleep(5)
        if self.CheckXml(CountRepeat=1,element='//node[@class="android.view.View"]', index=-1, Xoffsetplus=10, Yoffsetplus=10): self.ld.KeyEvent("KEYCODE_BACK") 
        self.ld.KeyEvent("KEYCODE_BACK")
    def __EditProfile(self):
        if self.ref.ref.upavt.isChecked():
            self.__UpAvatar()
        if self.ref.ref.changename.isChecked():
            self.__ChangeName()
        if self.ref.ref.publictim.isChecked():
            self.__PublicTym()
        if self.ref.ref.upavt.isChecked():
            self.__RemoveImage()
        return "SUCCESS"
    def Reg(self):
        checkbirthday = True
        ld = self.ld
        if self.key != "": 
            proxy = self.__GetProxy(self.key)
            if proxy == "KEYEXPIRED": return "KEYEXPIRED"
            self.ref.show.emit(self.row, 3, proxy)
            if self.__SetProxy(proxy) == "FAIL": return "FAIL"
        self.ref.show.emit(self.row, 3, "Đang reg......")
        ld.DeleteCache("com.zhiliaoapp.musically.go")
        ld.OpenTikTokLite()
        time.sleep(15)
        self.ld.TapImage('./images/dangky.png')
        if self.CheckXml(element='//node[@content-desc="Bạn không có tài khoản? Đăng ký" and @class="com.bytedance.ies.xelement.text.text.LynxTextUI"]', Xoffsetplus=10, Yoffsetplus=10) != True: return "FAIL"
        if self.CheckXml(element='//node[@content-desc="Sử dụng số điện thoại hoặc email" and @class="com.lynx.tasm.behavior.ui.text.FlattenUIText" and @text="Sử dụng số điện thoại hoặc email"]', index=1) != True: return "FAIL"
        time.sleep(3)
        if self.__CheckBirthday():
            checkbirthday = False
            self.__BirthDay()
            self.CheckXml(element='//node[@class="com.lynx.tasm.behavior.ui.text.FlattenUIText" and @content-desc="Tiếp"]')
        if self.CheckXml(element='//node[@content-desc="Email" and @class="com.ss.android.ugc.aweme.bullet.ui.LynxRipple"]', Xoffsetplus=10) != True: return "FAIL"
        ld.SendText(VN=self.mail.split("|")[0])
        self.CheckXml(element='//node[@class="com.lynx.tasm.behavior.ui.text.FlattenUIText" and @content-desc="Tiếp"]', index=1)
        # if self.CheckXml(element='//node[@class="com.lynx.tasm.ui.image.UIImage"]', index=-1, Yoffsetplus=-100, Xoffsetplus=10) != True: return "FAIL"
        ld.DumXml()
        if self.FindElement('//node[@text="Bạn đã đăng ký"]', index=0, attribute="text") == "Bạn đã đăng ký": return "REGISTERED"
        if self.FindElement('//node[@text="Email này đã được sử dụng"]', index=0, attribute="text") == "Email này đã được sử dụng": return "ERROR_MAIL"
        ld.SendText(VN=self.pwd)
        self.CheckXml(element='//node[@class="com.lynx.tasm.behavior.ui.text.FlattenUIText" and @content-desc="Tiếp"]')
        time.sleep(6)
        if checkbirthday:
            self.__BirthDay()
            self.CheckXml(element='//node[@class="com.lynx.tasm.behavior.ui.text.FlattenUIText" and @content-desc="Tiếp"]')
        ld.DumXml()
        if self.FindElement('//node[@text="Bạn đang gửi quá nhiều mã xác minh. Hãy thử lại sau."]', index=0, attribute="text") == "Bạn đang gửi quá nhiều mã xác minh. Hãy thử lại sau.": return "ERROR_SEND_CODE"
        time.sleep(10)
        codetiktok = self.__GetCodeOutlook()
        if codetiktok == []:
            time.sleep(10)
            codetiktok = self.__GetCodeOutlook()
            if codetiktok == []:
                return "ERROR_CODE"
        print(codetiktok)
        ld.SendText(VN=codetiktok)
        time.sleep(2)
        self.ld.DumXml()
        if self.FindElement('//node[@text="Bạn truy cập dịch vụ của chúng tôi quá thường xuyên."]', index=0, attribute="text"): return "Too many attempts please try again later"
        if self.FindElement('//node[@text="Mã xác minh email đã hết hạn"]', index=0, attribute="text"): return "ERROR_CODE_HOTMAIL"
        time.sleep(5)
        self.__ChangeUserId()
        # if self.CheckXml(element='//node[@content-desc="Bỏ qua" and @class="com.lynx.tasm.behavior.ui.text.FlattenUIText"]') != True: return "FAIL"
        self.CheckXml(element='//node[@text="Tôi"]')
        if self.__EditProfile() == "SUCCESS":
            return "SUCCESS"
    def SetPosLDPlayer(self, title, index, index2=0):
        hwnd = win32gui.FindWindow(None, title)
        if self.ref.ref.ldviewer.isChecked():
            # win32gui.MoveWindow(hwnd, 245*index, 410*index2, 245, 410, True)
            win32gui.SetParent(hwnd, self.ref.ref.view.hwnd[index])
            # win32gui.MoveWindow(hwnd, -2, -38, 273, 430, True)
            win32gui.MoveWindow(hwnd, -19, -38, 273, 430, True)
        else:
            win32gui.MoveWindow(hwnd, 245*index, 410*index2, 245, 410, True)
    def Stop(self):
        try:
            self.ld.Close()
        except:
            pass
        self.ref.show.emit(self.row, 3, "Stoped")
        self.terminate()
    def run(self):
        before = time.time()
        index2 = 0
        number = 1
        self.__GetListFirstNameVN()
        self.__GetListLastNameVN()
        self.pwd = self.ref.ref.password.text()
        if self.ref.ref.randompass.isChecked(): self.__CreatePassword()
        self.__CreateUserId()
        self.ld = LDPlayer()
        self.ld.pathLD = self.ref.ref.folderldplayer.text()
        self.ld.Info("index", self.index)
        self.ref.show.emit(self.row, 3, "Đang changeinfo......")
        title = self.ld.ChangeInfo()
        print(title)
        self.ref.show.emit(self.row, 3, "Đang mở ld......")
        self.ld.Start()
        time.sleep(1)
        if self.ld.IsDevice_Running() != True:
            time.sleep(5)
        if int(self.index) > 5*number:
            index2 += 1
            number += 1
        self.SetPosLDPlayer(title, index=int(self.index), index2=index2)
        for t in range(self.ref.ref.delayopenld.value(), -1, -1):
            self.ref.show.emit(self.row, 3, f"Vui lòng đợi {t} giây...")
            time.sleep(1)
        self.ref.show.emit(self.row, 2, self.mail.split("|")[0])
        self.ref.show.emit(self.row, 0, self.userid)
        self.ref.show.emit(self.row, 1, self.pwd)
        check = self.Reg()
        if check == "SUCCESS":
            after = time.time()
            open("accounts.txt", 'a+').write("%s|%s|%s\n"%(self.userid, self.pwd, self.mail))
            self.ref.show.emit(self.row, 3, f"Success in {int((after-before)/60.0)} minutes")
            self.ref.checksuccess.emit(True, self.mail)
        else:
            self.ref.show.emit(self.row, 3, check)
            self.ref.checksuccess.emit(False, self.mail)
            open("hotmailfail.txt", "a+").write(self.mail+"\n")
        self.ld.Close()
        return
