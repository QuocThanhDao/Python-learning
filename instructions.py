#Một số chỉ dẫn cũng như review cho bài exercise1.py

#File: Mở - đọc - viết - đóng

readfile = open("dictionary.txt", "r")  #<-- mode: r - đọc, w - viết, a - thêm vào (tạo mới khi không thấy tên)
a_list = []
#Đọc trong file dictionary, từ nào có chữ A thì lưu vào a_list, sau đó ghi ra file mới

for line in readfile:
    line = readfile.readline()          #Đọc từng dòng
    if "a" in line:
        a_list.append(line)             #Lưu vào a_list

readfile.close()                        #Đóng file lại
#Viết a_list vô file mới:
writefile = open("a_file.txt",'w')

for item in a_list:
    writefile.write(item)               #Viết từng dòng vô file mới tên a_file

writefile.close()                       #Đóng file




