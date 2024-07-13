import csv

CSV_FILE = 'moviecollectionsystem.csv'

def read_csv():
    with open(CSV_FILE, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        return list(reader)
    
def write_csv(data):
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['movie_id', 'movie_name', 'released_year', 'genre', 'ticket_payment'])
        writer.writeheader()
        writer.writerows(data)

def add_movie(movie_id, movie_name=None, released_year=None, genre=None, ticket_payment=None): 
    data = read_csv()
    new_data = {
        'movie_id': movie_id, 
        'movie_name': movie_name, 
        'released_year': released_year, 
        'genre': genre, 
        'ticket_payment': ticket_payment
    }
    data.append(new_data)
    write_csv(data)
    print("Movie added successfully!")

def view_movies():
    movies = read_csv()
    if not movies:
        print("No movie data found")
        return 
    
    headers = ['movie_id', 'movie_name', 'released_year', 'genre', 'ticket_payment']
    col_widths = {header: len(header) for header in headers}

    for movie in movies:
        for header in headers:
            col_widths[header] = max(col_widths[header], len(movie[header.lower().replace(' ', '_')]))
    
    header_row = '| ' + ' | '.join([header.ljust(col_widths[header]) for header in headers]) + ' |'
    print(header_row)
    
    for movie in movies:
        row = '| ' + ' | '.join([movie[header.lower().replace(' ', '_')].ljust(col_widths[header]) for header in headers]) + ' |'
        print(row)

def update_movie(movie_id, movie_name=None, released_year=None, genre=None, ticket_payment=None):
    data = read_csv()
    for movie in data:
        if movie['movie_id'] == movie_id:
            if movie_name:
                movie['movie_name'] = movie_name
            if released_year:
                movie['released_year'] = released_year
            if genre:
                movie['genre'] = genre
            if ticket_payment:
                movie['ticket_payment'] = ticket_payment
            break
    write_csv(data)
    print("Movie updated successfully!")

def delete_movie(movie_id):
    data = read_csv()
    data = [movie for movie in data if movie['movie_id'] != movie_id]
    write_csv(data)
    print("Movie deleted successfully!")
