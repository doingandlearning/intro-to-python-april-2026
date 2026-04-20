# 1. Top Performers
top_performers = exam & project
print("Top performers:", top_performers)

# 2. Count unique participants
print("Total unique participants:", len(exam | project))

# 3. Another class comparison
other_class_exam = {'Kirsty', 'Stuart', 'Alice', 'Jon'}
print("Common between both classes:", exam & other_class_exam)
print("Unique to either class:", exam ^ other_class_exam)

# 4. Add extra students
exam.add(input("Add a student to exam: "))
project.add(input("Add a student to project: "))
print("Updated exam set:", exam)
print("Updated project set:", project)
print("Updated both:", exam & project)
print("Only exam:", exam - project)
print("Only project:", project - exam)

# 5. Set symmetry check
if len(exam) == len(project):
    print("Both sets have the same number of students.")
elif len(exam) > len(project):
    print("More students took the exam.")
else:
    print("More students submitted the project.")
