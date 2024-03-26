user_input = input("Nhập chuỗi : ")
first_word = user_input.split()[0] if user_input.strip() else None
print("Từ đầu tiên trong chuỗi là : ", first_word if first_word else "Chuỗi không có từ.")

