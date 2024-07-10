import csv
CSV_FILE = 'data/moviecollection1.csv'
def read_csv():
    """
    Reads moviecollection1 data from a CSV file.
    Returns:
        list: List of dictionaries, each representing a moviecollection1 record.
    """
    with open(CSV_FILE, mode='r', newline='') as file:
         reader = csv. DictReader(file)
         return list(reader)
    
def write_csv(data):
     """
     Writes moviecollection1 data to a CSV file.
     Args:
     data (list): List of dictionaries representing moviecollection1 records.
     """
     with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['movie_id', 'movie_name', 'released_year', 'genre', 'rating', 'collection'])
        writer.writeheader()
        writer.writerows(data)


def create_moviecollection1(movie_id, movie_name, released_year,genre, rating, collection):
    """
    Creates a new moviecollection1 record and writes it to the CSV file.
    Args:
        movie_id (str): movie id of the movie.
        movie_name (str):movie Name of the movie.
        released_year (str): released year of the movie.
        genre(str):genre of the movie.
        rating (float): rating of the movie.
        collection (float): Total collection score of the movie.
    """
    data =read_csv()
    collection = rating (rating)
    new_movie = {'movie_id': movie_id, 'movie_name': movie_name, 'released_year': released_year, 'genre':genre, 'rating': rating, 'collection': collection}
    data.append(new_movie)
    write_csv(data)

    def read_students():
Reads and displays all student records from the CSV file in a tabular format.
students = read_csv()
if not students:

    print("No student data found.")
return
# Determine the maximum width for each column
headers = ['Roll', 'Name', 'City', 'Class', 'Total Percentage', 'Grade'] col_widths = (header: len(header) for header in headers)
for student in students:
for header in headers:
col_widths [header] = max(col_widths [header], len(student [header.lower().replace('','_')]))
# Create a horizontal separator
separator = headers]) + +- +-+-'.join(['-'* col_widths [header] for header in
# Create the header row
header_row = ' ' + ' | '.join([header.ljust(col_widths [header]) for header in headers]) +
print(separator)
print(header_row)
print(separator)
# Print each student record
for student in students:
row = '| '+' | '.join([student[header.lower().replace(' ', '_')].ljust(col_widths [header]) for header in headers]) +
print(row)
print(separator)
def update_student(roll, name=None, city=None, student_class=None, total_percentage=None):
Updates an existing student record in the CSV file.
Args:
roll (str): Roll number of the student to update.
name (str): New name of the student (optional).
city (str): New city of the student (optional).
student_class (str): New class of the student (optional).

total_percentage (float): New total percentage score of the student (optional).
data = read_csv()
for student in data:
if student['roll'] == roll:
1f name:
student['name'] = name
if city:
student['city'] = city
if student_class:
student['class'] = student_class
if total_percentage is not None:
student['total_percentage'] = total_percentage
student['grade'] = calculate_grade(total_percentage)
break
write_csv(data)
def delete_student(roll):
Deletes a student record from the CSV file.
Args:
roll (str): Roll number of the student to delete.
data = read_csv()
data = [student for student in data if student['roll'] != roll] write_csv(data)
