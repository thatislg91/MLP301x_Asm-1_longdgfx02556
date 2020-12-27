# ---------------------------------------------------------------------------
# Project Name: MLP301x_1.1-A_EN Assignment1
# Author: Dương Gia Long
# Start Date: 2020/12/23
# Finish Date:
# Editor: Notepad++ v7.9.1, Visual Studio Code v1.5.1
# Compiler: Python 3.9.1 64 bit
#----------------------------------------------------------------------------

##--------------- Task 1 ----------------------------------------------------
# Hàm Task1 nhận tên file và kiểm tra xem file có tồn tại ko.
# Nếu có sẽ trả về nội dung file, nếu không sẽ thông báo lỗi
def Task1():
	canTest = 0                                                     # Cờ kiểm tra đã nhập chính xác tên file chưa. Mặc định là 0 = chưa đúng

	while (canTest == 0):                                           # Tạo vòng lặp nhập cho đến khi đúng tên file
		try:
			filename = input("Enter a filename: ") 					# Nhận tên file
			opening_file = open(filename, 'r') 						# Sử dụng chế độ read cho file
			df = opening_file.read() 								# Lấy dữ liệu trong file
			print(df) 												# In dữ liệu trong file ra
			print('Successfully opened file {}'.format(filename)) 	# Kiểm tra file hoàn thành
			canTest = 1 											# Xác nhận nhập file đã đúng
			result = opening_file 									# Lấy nội dung file
			opening_file.close() 									# Đóng file
			return result, filename									# Giá trị trả về
		except ValueError as e:										# Báo lỗi file
			print("Sorry, I can't find this {} file. Error: {}".format(filename, e))
			canTest = 0
		except IOError as e:										# Báo lỗi IOError
			print("Sorry, IOError: {}".format(e))
			canTest = 0
		except EOFError as e:										# Báo lỗi EOFError
			print("Sorry, EOFrror: {}".format(e))
			canTest = 0
		except:														# Báo ko rõ lỗi gì
			print("Unknown Error")
			canTest = 0


##--------------- Task 2 ----------------------------------------------------
# Hàm Task 2 làm những nhiệm vụ sau:
# 1. Đếm số dòng có trong file
# 2. Kiểm tra xem dữ liệu nhập vào đã chuẩn chưa
#    1 dòng sẽ có 26 giá trị phân cách bởi dấu ,
#    Mã sinh viên bao gồm chữ N sẽ có 8 ký tự số phía sau. Tổng là 9 ký tự
# 3. Báo cáo số dòng lỗi cho người nhập dữ liệu

### Để xây dựng Task2, tạo thêm 1 số task nhỏ xử lý dữ liệu

# Hàm countNumberOfLine('tên file sẽ đếm số dòng')) đếm số dòng có trong file
def countNumberOfLine(filename):
	numberOfLine = len(open(filename, 'r').readlines())
	return numberOfLine

# Hàm check valid của 1 dòng
def checkValidOfLine(filename):
	# Mở file với chế độ r, đọc dưới lệnh readlines
	opening_file_line = open(filename, 'r').readlines()
	valid_line, invalid_line = 0, 0
	listNoError = []						# Lưu trữ danh sách ko lỗi
	for line in opening_file_line:      	# Check từng dòng trong file
		line = list(line.split(','))    	# Tách dòng thành list các kí tự, sử dụng ký hiệu phân cách ",", và lệnh split()
		temp_invalid, temp_valid = 0, 0 	# Số lượng dòng lỗi, k có lỗi

		# Loại bỏ ký tự xuống dòng "\n" lẫn trong các item của list
		lastIndex = len(line) - 1 			# Lấy index của item cuối cùng
		line[lastIndex] = line[lastIndex].rstrip("\n") # Khử "\n" trong item này nếu có
		listError = [] 						# Lưu trữ lỗi

		check_validOfStudentID, listError = checkStudentId(line[0]) # Check mã sinh viên
		if check_validOfStudentID == True: 	# Check mã sinh viên không có lỗi -> Check kết quả nhập đáp án
			amountOfAnswer = len(line) - 1 	# Số lượng đáp án được nhập = số phần tử - phần tử ID
			if amountOfAnswer == 25:	   	# Số lượng đáp án = 25 ok
				temp_valid  += 1
				listNoError.append(line)
			else:     	# Số lượng đáp án != 25 loại				
				temp_invalid += 1			
		else:			
			temp_invalid += 1
			
		if temp_invalid != 0:              	# Tính số dòng lỗi và xác định loại lỗi
			invalid_line += temp_invalid
			if amountOfAnswer != 25:
				error = 'This line is invalid, number of the answer({}) is difference from 25. Line items are {}'.format(amountOfAnswer, line)
				listError.append(error)
				print(listError)
			else:
				error = 'This line is invalid. Line items are {}'.format(line)
				listError.append(error)
				print(listError)
		else:                               # Tính số dòng không lỗi
			valid_line += temp_valid

	return valid_line, invalid_line, listNoError # Trả về số line lỗi và ko lỗi

# Hàm check mã sinh viên
def checkStudentId(studentID):
	studentID = list(studentID) 			# Ép kiểu dữ liệu về list
	lenOfID = len(studentID)    			# Kiểm tra số lượng phần tử
	fst_Letter = studentID[0]				# Lấy phần tử đầu tiên
	CheckID_listError = []      			# Lưu trữ lỗi

	if lenOfID != 9:            			# Check số lượng ký tự của ID, nếu khác 9 loại
		error = 'StudentID was not inputed correctly, Length of ID: {} difference from 9'.format(lenOfID)
		CheckID_listError.append(error)
		return False, CheckID_listError
	elif fst_Letter != 'N':     			# Check ký tự đầu tiên của ID, khác N loại
		error = 'StudentID was not valid format, the 1st charracter {} was difference from N'.format(fst_Letter)
		CheckID_listError.append(error)
		return False, CheckID_listError
	else:# Kiểm tra các phần tử còn lại nếu khác số 0 - 9 loại, Nếu toàn bộ là số từ 0 - 9 thì ID đã chuẩn
		numberOfID = studentID[1:9] 		# Lấy các ký tự sau N
		numberOfWrong = 0 					# Số ký tự khác (0-9)
		listOfWrong = [] 					# Lưu trữ các ký tự nhập sai
		for i in numberOfID:
			indexOfI = numberOfID.index(i)
			try: 							# Check các số trong ID phải thuộc [0,9]
				if int(i) >= 0 and int(i) <= 9:
					numberOfWrong += 0
				else:
					numberOfWrong += 1
					listOfWrong.append(numberOfID[indexOfI])
			except: 						# Trường hợp các ký tự nhập khác chữ số
				numberOfWrong += 1
				listOfWrong.append(numberOfID[indexOfI])
				error = 'StudentID was not valid format. {}'.format(listOfWrong)
				CheckID_listError.append(error)
				return False, CheckID_listError

		if numberOfWrong != 0:				# Nếu số lượng ký tự sai > 0 -> loại
			error = 'StudentID was not valid format. {}'.format(listOfWrong)
			CheckID_listError.append(error)
			return False, CheckID_listError
		else:								# Ngược lại là ok
			return True, CheckID_listError

# Hàm báo lỗi cho người nhập dữ liệu

##--------------- Task 3 ----------------------------------------------------
def student_Result(filename):
	# Lấy dữ liệu từ file
	valid_line, invalid_line, listNoError = checkValidOfLine(filename)

	# Sử dụng dataframe để phân tích kết quả
	df = pd.DataFrame(listNoError, columns=['ID', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7',	'D8', 
											'D9', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'D16','D17', 
											'D18','D19', 'D20', 'D21', 'D22', 'D23', 'D24', 'D25'])

	df.set_index('ID')

	# Thiết lập mã chuẩn để chấm điểm
	answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
	answer_key = list(answer_key.split(','))

	# Đổi bảng kết quả thành bảng điểm
	for i  in range(0, valid_line):
		for j in range(1,26):
			temp = df.iloc[i, j]
			if temp == '' :
				df.iloc[i, j] = 0
			elif temp == answer_key[j-1]:
				df.iloc[i, j] = 4
			else:
				df.iloc[i, j] = -1

	# Tính toán kết quả từ bảng điểm
	df['Total']=df.drop('ID', axis=1).sum(axis=1)
	df_Analysis_Result = df[['ID', 'Total']].set_index('ID')
	total_Describe = df_Analysis_Result.describe()

	# Thông báo kết quả theo yêu cầu
	class_Mean = total_Describe.loc['mean', 'Total']
	class_Max = total_Describe.loc['max', 'Total']
	class_Min = total_Describe.loc['min', 'Total']
	class_Range = class_Max - class_Min
	class_Median= total_Describe.loc['50%', 'Total']
	print('Điểm TB:{}\nĐiểm cao nhất:{}\nĐiểm thấp nhất:{}\nRange: {}\nMode:{}'.format(class_Mean, class_Max, class_Min, class_Range, class_Median))
	
	# Trả về bảng kq tổng kết sử dụng cho in ra file
	return df_Analysis_Result
	
	
##--------------- Task 4 ----------------------------------------------------
def writeToFile(dataToWrite, filename):
	# Lấy tên class
	fileNum = str(filename[:6])

	# Tạo tên class mới theo yêu cầu
	new_filename = fileNum + "_grades.txt"

	# Tạo file với chế độ ghi đè
	open_new_filename = open(new_filename, 'w', encoding='UTF-8')
	with open_new_filename as f:
		dataToWrite.reset_index(inplace=True)	
		# Ghi dữ liệu
		f.writelines(u'Đây là kết quả của {}\n'.format(fileNum))	
		f.write(dataToWrite.to_string(header=True, index=True))
    
	# Đóng file
	open_new_filename.close()
	# Thông báo khi hoàn thành
	print('Write to file done!')



##--------------- Main ------------------------------------------------------
def main():
	df, filename = Task1()
	numberOfLine = countNumberOfLine(filename)
	print('File có {} dòng, và nội dung file là \n {}'.format(numberOfLine,df))

	valid_line, invalid_line, listNoError = checkValidOfLine(filename)
	print('Total valid line: {}. Total invalid line: {}'.format(valid_line, invalid_line))

	df_Analysis_Result = student_Result(filename)
	writeToFile(df_Analysis_Result, filename)

if __name__ == '__main__':
	import sys
	import pandas as pd
	import numpy as np
	main()
