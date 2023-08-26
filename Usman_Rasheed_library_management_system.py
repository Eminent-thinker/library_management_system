import sys    # importing the module to interact with the system command

# Define the Book class
class Book:
    '''This class represents a book and its management within the library.'''
    def __init__(self, title, author, genre):  # Constructor to initialize attributes
        self.title = title
        self.author = author
        self.genre = genre
        self.is_borrowed = False   # Initialize book as not borrowed by default.
        self.borrower_card_number = None  # Patron's card number who borrowed the book, default is None.

    def is_book_available(self, title):
        '''Check if the book is available in the library.'''
        if self.is_borrowed:   # if not borrowed, book is available
            return True
        else:
            return False

    def borrow(self, patron_card_number):
        '''Borrow the book if it's available.'''
        if not self.is_borrowed:   # if the book is not borrowed, allow borrowing
            self.is_borrowed = True
            self.borrower_card_number = patron_card_number  # setting the variable borrower_card_number to the unique number given to the patron during registration.
            return True  
        return False

    def return_book(self):
        '''Return the borrowed book'''
        if self.is_borrowed:    # if book is borrowed, allow returning
            self.is_borrowed = False
            self.borrower_card_number = None   # setting the variable borrower_card_number to it its default value None
            return True
        return False

    

# Define the Patron class
class Patron:
    '''This class represents a patron and their interaction with books.'''
    def __init__(self, name, age, card_number):   # Constructor to initialize attributes
        self.name = name
        self.age = age
        self.info = {'name': name, 'age': age}
        self.card_number = card_number
        self.borrowed_books = []
        


    def borrow_book(self, book):
        '''Borrow a book from the library.'''
        self.borrowed_books.append(Book(book.title, book.author, book.genre)) # Append the borrowed book as the parameters defined in the Book class.
        if not book.is_borrowed:   # if the book is not borrowed, allow borrowing
            book.borrow(self.card_number)
            print(f"{self.info['name']} has successfully borrowed the book '{book.title}'.")
        else:
            print(f"The book '{book.title}' is already borrowed by another patron.")

            
    
    def returnBook(self, book):
        '''Return a book to the library.'''
        if book in self.borrowed_books:  # if the book is in the list of borrowed book, allow returning.
            book.return_book() 
            self.borrowed_books.remove(book)   # remove the book from the borrowed book list.
            print(f"{self.info['name']} has successfully returned the book '{book.title}'.")
        else:
            print(f"The book '{book.title}' is not borrowed by {self.info['name']}.")



    def displayUnavailableBooks(self):
        '''Display all the borrowed books in the library.'''
        print('The books we have out of our library are as follow: ')
        print('================================================')
        for book in self.borrowed_books:   # looping through the borrowed books in the library.
            print(f"{book.title} by {book.author}: {book.genre}")


# Define the Library class
class Library:
    '''This class represents a library and its book and patron management.'''
    def __init__(self):   # Constructor to initialize attributes
        self.availablebooks = []
        self.patrons = {}

    
    def add_book(self, title, author, genre):
        '''Add a new book to the library's collection.'''
        new_book = Book(title, author, genre)
        self.availablebooks.append(new_book)  # appending the book as the parameters define in the Book class
        print('The book has been successfully added to the Library.')


    # def is_book_available(self, title):
    #     '''Check if the book is available in the library.'''
    #     for book in self.availablebooks:  # looping through the available books in the library to know if the requested book is available.
    #         if book.title == title:
    #             return True
    #     return False
    

    # def borrow_book(self, patron_card_number, title):
    #     '''Allow a patron to borrow a book.'''
    #     for book in self.availablebooks:   # looping through the available books in the library to know if the requested book is available.
    #         if book.title == title and not book.is_borrowed:  # checking if the book's title is available and also checking if the book is not borrowed to allow borrowing.
    #             if book.borrow(patron_card_number):
    #                 print(f"Book with Title {title} has been successfully borrowed.")
    #             else:
    #                 print("Unable to borrow the book. It might already be borrowed.")
    #             return
    #     print('Sorry the book you have requested is currently not in the library')

    def register_patron(self, name, age, card_number):
        '''Register a new patron in the library.'''
        new_patron = Patron(name, age, card_number)   # Getting attributes of the Patron class
        self.patrons[new_patron.card_number] = new_patron   # Adding new patron to the Patrons dictionary using their unique card number
        print(f'You have succesfully registered: {new_patron.name}')


    def displayAvailableBooks(self):
        '''Display all the available books in the library.'''
        print('The books we have in our library are as follow: ')
        print('================================================')
        for book in self.availablebooks:   # looping through the available books in the library.
            if not book.is_borrowed:  # if the book is not borrowed i.e it's available to borrow.
                    print(f"{book.title} by {book.author}: {book.genre}")

    def display_registered_patrons(self):
        '''Display all the registered Patrons'''
        print('Our registerred patrons are: ')
        print('=============================')
        for card_number, info in self.patrons.items():  # looping through the patron's dictionary in the library.
            print(f"Name: {info.name}, Age: {info.age}, Card_Number: {card_number}")


            
    def display_books_borrowed_by_patron(self, patron_card_number):
        '''Display all the books borrowed by a specific patron.'''
        print(f"Books borrowed by Patron cardNumber: {patron_card_number}: ")
        for patron in self.patrons.values():   # looping through the patron's values in the dictionary.
            if patron.card_number == patron_card_number:  # compare if the provided card number is the same any card number found in the patron's data.
                for book in patron.borrowed_books:   # looping through the book in the borrowed book list
                    print('=========================================')
                    print(f"{book.title} by {book.author}: {book.genre}")
                return
        print(f"No patron found with cardNumber: {patron_card_number}")


class ReferenceBook(Book):
    '''This class represents a refrence book and it's inherited attributes from the parent class Book.'''
    def __init__(self, title, author, genre, reference_id):    # Constructor to initialize attributes
        super().__init__(title, author, genre) # Constructor to initialize attributes of the parent class.
        self.reference_id = reference_id

    def diplay_reference_id(self):
        '''Display reference ID'''
        print(f"Reference ID: {self.reference_id}")


# Define main function to excute all the classes based on the user choices.
def main():
    library = Library()
    
    # Adding initial books and patrons
    library.add_book('Use of English','Rasheed', 'genre1' )
    library.add_book('The Last Battle', 'AbdulRahman', 'genre2')
    library.add_book('The screwtape letters', 'Yusuf', 'genre3')
    library.add_book('The Great Divorce', 'Maryam', 'genre4')
    library.add_book('The Last War', 'AbdulRazaq', 'genre5')

    patron1 = Patron('Basheer', 24, "12345")
    patron2 = Patron("Ahmad", 34, "67890")
    patron3 = Patron("Shereefdeen", 27, "890123")

    library.patrons[patron1.card_number] = patron1
    library.patrons[patron2.card_number] = patron2
    library.patrons[patron3.card_number] = patron3



    done = False
    while done == False:
         # Display the library menu and get user's choice
        print("""
         ============= LIBRARY MENU =============
              1. Add book to the Library
              2. Return a book
              3. Borrow a book
              4. Register patron
              5. Display all available books
              6. Display all registered patrons
              7. Display all unavailable books borrowed by a specific patron
              8. Exit
              """)
        choice = int(input('Enter your choice: '))
        if choice not in range(1,9):
            print(f"{choice} is not a valid choice. Kindly check the Menu")
        else:
            # Handle user's choice
            if choice == 1:
                # Add book
                print("You are about to add a book, please answer the following correctly: ")
                title = input("Enter the book title: ")
                author = input("Enter the book's author: ")
                genre = input("Enter the book's genre: ")
                library.add_book(title, author, genre)


            if choice == 2:
                # Return book
                print("The following books are currently out of the library: ")
                for patron in library.patrons.values():
                    for book in patron.borrowed_books:
                        print(f"{book.title} by {book.author}: {book.genre}")
                print("You are about to return a book, please answer the following correctly: ")
                chooce_book = input("Enter the book title to return (Take note of the spelling): ")
                for patron in library.patrons.values():
                    if len(patron.borrowed_books) != 0:
                        for book in patron.borrowed_books:
                            if chooce_book == book.title:
                                book_to_return = book
                            else:
                                print("Please, write the book's title exactly the way you see it.")   
                    break
                
                try:
                    returner = input("Enter patron's name: ") 
                    for patron in library.patrons.values():
                        if patron.name == returner:
                            patron.returnBook(book_to_return)
                    library.add_book(book.title, book.author, book.genre)
                except Exception:
                    print("No record of any borrowed book.")
             
                
            elif choice == 3:
                # borrow book
                print("The following books are in the Library: ")
                for book in library.availablebooks:
                    print(f"{book.title} by {book.author}: {book.genre}")
                chooce_book = input("Enter the book title to borrow (Take note of the spelling): ")
                for book in library.availablebooks:
                    if chooce_book == book.title:
                        book_to_borrow = book
                    else:
                        print("Please, write the book's title exactly the way you see it.")
                    break
                try:      
                    borrower = input("Enter patron's name: ")
                    for patron in library.patrons.values():
                        if patron.name == borrower:
                            patron.borrow_book(book_to_borrow)
                except Exception:
                    print("No record of this request book in the library.")

                    
                 
            elif choice == 4:
                # Register Patron
                print("You are about to register a patron, please answer the following correctly: ")
                name = input("Enter your first_name: ")
                age  = int(input("Enter your age: "))
                card_number = input("Enter your card Number: ")
                library.register_patron(name, age, card_number)
            elif choice == 5:
                # Display all available books
                library.displayAvailableBooks()
            elif choice == 6:
                # Display all the registered patrons
                library.display_registered_patrons()
            elif choice ==7:
                # Display book(s) borrowed by a particular patron using the patron's unique card number
                card_number = input("Enter your card Number: ")
                library.display_books_borrowed_by_patron(card_number)
            elif choice == 8:
                sys.exit()


if __name__ == "__main__":

    main()
