exam_points = {
  "Mariusz":30,
  "Mateusz":55,
  "Marta":76,
  "Roman":30,
  "Arleta":59,
  "Adrian": 96,
  "Monika":91,
  "Andrzej":22,
  "Krzysztof":83,
  "Krystyna":93,
  "Piotr":44,
  "Dawid":10,
  "Agnieszka":15
}

#failed_students = [grade for grade in exam_points.values() if grade < 46]  sprawdzić jak wyciągnąć items

failed_students = []
top_students = []
best_student = ("",0)

print(failed_students)
max_score = 0

for student,score in exam_points.items():
    if score <= 45:
        failed_students.append(student)
    elif score >= 91:
        top_students.append(student)

    if score > max_score:
        max_score = score
        best_student = (student,score)

print("Nie zdali egzaminu:" ,failed_students)
print("Zdali na bardzo dobry:", top_students)
print("Najlepszy wynik studenta:", best_student)