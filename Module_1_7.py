grades = [[5, 3, 3, 5, 4],
          [2, 2, 2, 3],
          [4, 5, 5, 2],
          [4, 4, 3],
          [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
average_score = {}
list_studnts = list(students)
list_studnts.sort()
count_grades = 0
for name in list_studnts:
    tmp_grades = grades[count_grades]
    tmp_len = len(tmp_grades)
    tmp_average = sum(tmp_grades)/tmp_len
    average_score[list_studnts[count_grades]] = tmp_average
    count_grades += 1
print(average_score)

