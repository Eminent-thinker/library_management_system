# library_management_system
Library management system using object oriented programming 
This is a Python program that implements a basic library management system.
The program includes three main classes: `Book`, `Patron` and `Library`. These classes are used to simulate the interactions between patrons, books, and the library itself. Here is a brief overview of how the program works:
The `Book` class represents individual books with attributes like title, author, genre, and whether the book has been borrowed. The class provides methods to check if a book is available, borrow a book, and return a book.
The `Patron` class represents patrons with attributes like name, age, and a card number. Patrons can borrow and return books using methods defined in this class.
The `Library` class manages the collection of available books and registered patrons. It provides methods to add books to the library, check book availability, register new patrons, and display available books and registered patrons. Patrons can also borrow books from the library through this class.
There's also a `ReferenceBook` class that inherits from the `Book` class and includes an additional attribute reference_id for reference books.
The `main()` function serves as the entry point for the program. It creates instances of the `Library` class and simulates the interaction between patrons and the library through a menu-driven interface.

User can interact with the library by choosing options from the menu. They can add books, return books, borrow books, register patrons, display available books, display registered patrons, and more.

Overall, this program provides a basic framework for library management system. However, there are several areas that could be improved or expanded depending on the specific requirements of a real-world library system. For instance, error handling, data validation, and more advanced features like due dates, reservation systems, and user authentication could be added to enhance the functionality and robustness of the program.

You are highly welcome to make a pull request if there's anything you can add to the codes.
