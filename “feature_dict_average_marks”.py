mark_dict={}
more_students = "yes"
while more_students == 'yes':
  name = input("Please enter the student's name: ")
  marks = int(input("Please enter that student's marks: "))
  mark_dict[name] = marks
  print(mark_dict)
  more_students = input("Are there any more students whose scores need to be tracked? (yes/no) ")
  # calculating average
  dict_sum = sum(mark_dict.values())
  print(dict_sum)
  #dict_avg = sum(len(dictionary[name]))
  dict_avg = dict_sum/len(mark_dict)
  print(dict_avg)

