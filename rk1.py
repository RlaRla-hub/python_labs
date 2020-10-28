# используется для сортировки
from operator import itemgetter

class Schoolchild:
    "Школьники"
    def __init__(self, id, fio, averege_mark, class_id):
        self.id = id
        self.fio = fio
        self.averege_mark = averege_mark
        self.class_id = class_id

class School_Class:
    "Школьный класс"
    def __init__(self, id, number, letter):
        self.id = id
        self.number = number
        self.letter=letter

class Schoolchild__School_Class:
    """Связь многие-ко-многим Школьник-Класс"""
    def __init__(self, Schoolchild_id,School_Class_id):
        self.Schoolchild_id = Schoolchild_id
        self.School_Class_id = School_Class_id


Schoolchild_list = [
    Schoolchild(1, "Давыдов Алексей Иванович", 5, 3),
    Schoolchild(2, "Степанова Анастасия Александровна", 3, 4),
    Schoolchild(3, "Карелин Владислав Вячеславович", 4.6, 4),
    Schoolchild(4, "Зубина Алина Владимировна", 3.8, 1),
    Schoolchild(5, "Уменко Михаил Викторович", 2.9, 3),
    Schoolchild(6, "Решётникова Марина Витальевна", 4, 2),
    Schoolchild(7, "Бережков Кирилл Кириллович", 5, 2),
    Schoolchild(8, "Ромашина Юлия Николаевна", 5, 1)
]

listSchool_Classes = [
    School_Class(1, 10, "A"),
    School_Class(2, 11, "A"),
    School_Class(3, 10, "Б"),
    School_Class(4, 11, "Б")
]

listSchoolchild_SchoolClass = [
    Schoolchild__School_Class(3, 3),
    Schoolchild__School_Class(8, 2),
    Schoolchild__School_Class(4, 1),
    Schoolchild__School_Class(7, 3),
    Schoolchild__School_Class(2, 3),
    Schoolchild__School_Class(1, 1),
    Schoolchild__School_Class(6, 4),
    Schoolchild__School_Class(5, 4),
    
]


    # Соединение данных один-ко-многим 
one_to_many = list((School_Class, Schoolchild) 
    for Schoolchild in Schoolchild_list 
    for School_Class in listSchool_Classes 
    if (Schoolchild.class_id==School_Class.id))


many_to_many_temp = list((p.number, p.letter, d.School_Class_id, d.Schoolchild_id) 
        for p in listSchool_Classes 
        for d in listSchoolchild_SchoolClass 
        if (p.id==d.School_Class_id))
    
many_to_many = list((e.fio, e.class_id, number, letter, Schoolchild_id) 
        for number, letter,School_Class_id,Schoolchild_id  in many_to_many_temp
        for e in Schoolchild_list
        if (e.id==Schoolchild_id))

    
print('Задание E1')
for i in one_to_many:
    if "A" in i[0].letter:
        print(i[1].fio)

print('Задание E2')
Marks_Avg_List = list()
for i in listSchool_Classes:
    Schoolchild_list=list(filter(lambda x: x[0].id==i.id, one_to_many))
    Marks_Avg=0
    for item in Schoolchild_list:
        Schoolchild=item[1]
        Marks_Avg+=Schoolchild.averege_mark
    Marks_Avg=round(Marks_Avg/len(Schoolchild_list),2)
    Marks_Avg_List.append((i.number, i.letter, Marks_Avg))
    for item in sorted(Marks_Avg_List, key=lambda x: x[0]):
        print("Средняя оценка в классе: ", item[0], item[1], "составляет", item[2])


print('Задание E3')
m=''
for i in many_to_many:
    str_1=i[0]
    for j in range(len(str_1)):
       if j==0 and str_1[j]=='Р':
          m=m+str_1+', class_id='+str(i[1])+'\n'
          #print(m)
          break
       else:
          break
print(m)


   
