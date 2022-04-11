#zadanie 1
name_list = ["John", "Michael", "Terry", "Eric", "Graham"]
name_dictionary = {elem: len(elem) for elem in name_list}
print(name_dictionary)

print('=====================')

#zadanie 2
list = [1, 2, 3, 5, 6, 11, 12, 18, 19, 21]
for num in list:
   if num > 1:
       for i in range(2, num):
           if num % i == 0:
               break
       else:
           print(num)

print('=====================')

#zadanie 3
days = ['pon','śro','pią','sob']
days.insert (1,"wto")
days.insert (3,"czw")
days.append ("nie")
print(days)

print('=====================')

#zadanie 4
tea_instruction = {
  5: 'włącz czajnik', 
  1: 'znajdź opakowanie herbaty',
  6: 'zalej herbatę',
  4: 'nalej wody do czajnika',
  2: 'wyjmij kubek',
  3: 'włóż herbatę do kubka',
}
print(tea_instruction) 
print("After sorting \n") 
print(sorted(tea_instruction.items())) 
