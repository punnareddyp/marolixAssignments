class School:
    def __init__(self, name, location, num_students, num_teachers, rating):
        self.name = name
        self.location = location
        self.num_students = num_students
        self.num_teachers = num_teachers
        self.rating = rating

# Creating 10 objects of the School class
school1 = School("rama School", "Hyderabad", 100, 10, 4.5)
school2 = School("punna School", "Bangalore", 200, 20, 4.0)
school3 = School("gopi School", "Mumbai", 300, 30, 4.2)
school4 = School("hanimi School", "Chennai", 400, 40, 4.1)
school5 = School("sit School", "Delhi", 500, 50, 4.3)
school6 = School("siva School", "Kolkata", 600, 60, 4.4)
school7 = School("naga School", "Pune", 700, 70, 4.6)
school8 = School("baragavu School", "Ahmedabad", 800, 80, 4.7)
school9 = School("raja School", "Jaipur", 900, 90, 4.8)
school10 = School("mani School", "Lucknow", 1000, 100, 4.9)

# Accessing the attributes of each object
print(school1.name, school1.location, school1.num_students, school1.num_teachers, school1.rating)
print(school2.name, school2.location, school2.num_students, school2.num_teachers, school2.rating)
print(school3.name, school3.location, school3.num_students, school3.num_teachers, school3.rating)
print(school4.name, school4.location, school4.num_students, school4.num_teachers, school4.rating)
print(school5.name, school5.location, school5.num_students, school5.num_teachers, school5.rating)
print(school6.name, school6.location, school6.num_students, school6.num_teachers, school6.rating)
print(school7.name, school7.location, school7.num_students, school7.num_teachers, school7.rating)
print(school8.name, school8.location, school8.num_students, school8.num_teachers, school8.rating)
print(school9.name, school9.location, school9.num_students, school9.num_teachers, school9.rating)
print(school10.name, school10.location, school10.num_students, school10.num_teachers, school10.rating)
