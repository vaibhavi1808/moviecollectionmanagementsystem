from crudnew import add_movie, view_movies, update_movie, delete_movie
from Transactions import count_movies

def main():
    while True:
        print("||===================================================================||")
        print("||                  ........Movie Collection........                 ||")      
        print("||===================================================================||")
        print("||               1. Add New Movie                                    ||")
        print("||-------------------------------------------------------------------||")
        print("||               2. View All Movies                                  ||")
        print("||-------------------------------------------------------------------||")
        print("||               3. Update Movie                                     ||")
        print("||-------------------------------------------------------------------||")       
        print("||               4. Delete Movie                                     ||")     
        print("||-------------------------------------------------------------------||")
        print("||               5. Total Number of Movies                           ||")     
        print("||-------------------------------------------------------------------||")             
        print("||               6. Exit                                             ||")            
        print("||===================================================================||\n")

        ch = int(input("Enter your choice: "))
        
        if ch == 1:
            movie_id = input("Enter movie ID: ")
            movie_name = input("Enter movie name: ")
            released_year = input("Enter released year: ")
            genre = input("Enter genre: ")
            ticket_payment = input("Enter ticket payment: ")
            add_movie(movie_id, movie_name, released_year, genre, ticket_payment)

        elif ch == 2:
            view_movies()

        elif ch == 3:
            movie_id = input("Enter movie ID: ")
            movie_name = input("Enter new movie name (leave blank to keep current): ")
            released_year = input("Enter new released year (leave blank to keep current): ")
            genre = input("Enter new genre (leave blank to keep current): ")
            ticket_payment = input("Enter new ticket payment (leave blank to keep current): ")
            update_movie(movie_id, movie_name or None, released_year or None, genre or None, ticket_payment or None)

        elif ch == 4:
            movie_id = input("Enter movie ID: ")
            delete_movie(movie_id)

        elif ch == 5:
            count_movies()

        elif ch == 6:
            break

        else:
            print("Invalid choice!")
