from decorate import line
from pathlib import Path
# 1) Створіть клас Book, який має такі властивості:

# - назва книги
# - автор книги
# - кількість сторінок

# Додайте методи:

# - аксесори
# - метод, який виводить інформацію про книгу
# - метод, який повертає True, якщо кількість сторінок більше 300, інакше False.


class Book:
    '''
    The Book class represents a book with a title, author, and number of pages.
    Methods:
        - get_info(): returns information about the book as a string.
        - is_long_book(): returns True if the number of pages is greater than 300, False otherwise.
    '''
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    def get_info(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"

    def is_long_book(self):
        return self.pages > 300
    

if __name__ == "__main__":
    line("Book class, task 1")

    book1 = Book("Methodius Buslaev. The Dryad's Necklace", "Dmitry Yemets", 384)
    book2 = Book("Azazel", "Boris Akunin", 250)

    print(book1.get_info()) # Title: Methodius Buslaev. The Dryad's Necklace, Author: Dmitry Yemets, Pages: 384
    print(book2.get_info()) # Title: Azazel, Author: Boris Akunin, Pages: 250

    print(f"is {book1.title} have more than 300 pages?: {book1.is_long_book()}") # True
    print(f"is {book2.title} have more than 300 pages?: {book2.is_long_book()}") # False



# 2) Створіть клас Counter, який є лічильником:

# - count (початкове значення дорівнює 0).

# Методи:
# increment(): збільшує значення на 1,
# decrement(): зменшує значення на 1,
# reset(): скидає значення лічильника на 0,
# get_value(): повертає поточне значення лічильника.


class Counter:
    '''
    The Counter class represents a simple counter with methods to increment, decrement, reset, and get the current value.
    Methods:
        - increment(): increases the count by 1.
        - decrement(): decreases the count by 1.
        - reset(): resets the count to 0.
        - get_value(): returns the current value of the count.
    '''
    def __init__(self, start: int = 0):
        self.__count = start

    def increment(self):
        self.__count += 1

    def decrement(self):
        self.__count -= 1

    def reset(self):
        self.__count = 0

    def get_value(self):
        return self.__count


if __name__ == "__main__":
    line("Counter class, task 2")

    counter = Counter()
    print(counter.get_value()) # 0
    counter.increment()
    counter.increment()
    print(f"After increment twice: {counter.get_value()}") # 2
    counter.decrement()
    print(f"After decrement: {counter.get_value()}") # 1
    counter.reset()
    print(f"After reset: {counter.get_value()}") # 0

    try:
        print("its private so we cant access it directly: ")
        print(counter.__count) #! AttributeError: 'Counter' object has no attribute '__count'
    except AttributeError as e:
        print(e)

# 3) Створіть клас Calculator, який виконує прості арифметичні операції: додавання, віднімання, множення та ділення.
# Використовуйте статичні методи.

# Методи:
# add(a, b): повертає суму двох чисел,
# subtract(a, b): повертає різницю двох чисел,
# multiply(a, b): повертає добуток двох чисел,
# divide(a, b): повертає результат ділення, якщо дільник не дорівнює нулю; інакше виводить повідомлення "Ділення на нуль!".

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b 
    @staticmethod
    def subtract(a, b):
        return a - b
    @staticmethod
    def multiply(a, b):
        return a * b
    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("You cant divide by zero!")
        return a / b
    

if __name__ == "__main__":
    line("Calculator class, task 3")

    print(Calculator.add(5, 3)) # 8
    print(Calculator.subtract(5, 3)) # 2
    print(Calculator.multiply(5, 3)) # 15
    try:
        print(Calculator.divide(5, 0)) #! ValueError: You cant divide by zero!
    except ValueError as e:
        print(e)

# 4) Створіть клас Rectangle, який має два властивості: ширина та висота.

# Методи:
# area(): повертає площу прямокутника,
# perimeter(): повертає периметр прямокутника,
# is_square(): повертає True, якщо це квадрат (ширина дорівнює висоті), інакше False.

class Rectangle:
    '''
    The Rectangle class represents a rectangle with width and height.
    Methods:
    - area(): returns the area of the rectangle.
    - perimeter(): returns the perimeter of the rectangle.
    - is_square(): returns True if the rectangle is a square (width equals height), False otherwise.

    '''
    def __init__ (self, width: float, height: float):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
    def is_square(self):
        return self.width == self.height
    
    
if __name__ == "__main__":
    line("Rectangle class, task 4")
    rectangle = Rectangle(4, 5)
    square = Rectangle(3, 3)
    print(f"Area of rectangle: {rectangle.area()}") # 20
    print(f"Perimeter of rectangle: {rectangle.perimeter()}") #18
    print(f"Is this rectangle a square?: {rectangle.is_square()}") # False
    line()
    print(f"Area of square: {square.area()}") # 9
    print(f"Perimeter of square: {square.perimeter()}") # 12
    print(f"Is this rectangle a square?: {square.is_square()}") # True


# 5) Створіть клас BankAccount, який має властивості:

# - власник рахунку
# - баланс

# Методи:
# deposit(amount): збільшує баланс на amount,
# withdraw(amount): зменшує баланс на amount, якщо достатньо коштів, інакше виводить повідомлення: "Недостатньо коштів на рахунку!",
# display_balance(): виводить поточний баланс.

class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.__owner = owner
        self.__balance = balance

    def show_owner(self):
        return self.__owner
    
    def change_owner(self, new_owner: str, old_owner: str = ""):

        if old_owner == "":
            check = input(f"Weeel~ we not secure, so maybe you can ateast enter correctly your name? :");
            if check == old_owner:
                self.__owner = new_owner
        if old_owner == self.__owner:
            self.__owner = new_owner
        else:
            print("Nah man, you atleast need to know your name, u know?")


    def deposit(self, amount: float):
        self.__balance += amount

    def withdraw(self, amount: float):
        if amount > self.__balance:
            raise ValueError("Not enough funds in the account!")
        self.__balance -= amount

    def display_balance(self):
        print(f"Current balance for {self.__owner}: {self.__balance}")

if __name__ == "__main__":
    line("BankAccount class, task 5")
    account = BankAccount("Silver arrow", 1000.0)
    account.display_balance() # Current balance for Silver arrow: 1000.0
    account.deposit(500.0)
    account.display_balance() # Current balance for Silver arrow: 1500.0
    try:
        account.withdraw(2000.0) #! ValueError: Not enough funds in the account!
    except ValueError as e:
        print(e)
    account.withdraw(300.0)
    account.display_balance() # Current balance for Silver arrow: 1200.0

    #well i did it, sooo
    account.change_owner("Green arrow", "Silver arrow")
    account.display_balance() # Current balance for Green arrow: 1200.0


# 6) Створіть класи Book і Library, які будуть взаємодіяти між собою.
# Клас Book:
# назва  
# автор
# кількість сторінок
# ідентифікатор книги
# Методи:
# виводити інформацію про книгу

# Клас Library:
# список книг у бібліотеці
# Методи:
# додати книгу до бібліотеки
# видалити книгу за ідентифікатором
# шукати книгу за назвою та повертати її інформацію

class BookFromLibrary(Book):
    '''The BookFromLibrary class represents a book in the library with an additional ISBN identifier.
    The class inherits from the Book class, so it also has access to the title, author, and pages properties.
    Methods:
    - get_info(): returns information about the book including its ISBN, title, author, and
      number of pages.
    '''
    def __init__(self, title: str, author: str, pages: int, ISBN: int):
        super().__init__(title, author, pages)
        self.__ISBN = ISBN

    def get_info(self):
        return f"ISBN: {self.__ISBN}, Title: {self.title}, Author: {self.author}, Pages: {self.pages}"

class Library:
    def __init__(self):
        self.__books = []

    def add_book(self, book: BookFromLibrary):
        self.__books.append(book)

    def remove_book(self, book_ISBN: int):
        self.__books = [book for book in self.__books if book._BookFromLibrary__ISBN != book_ISBN]

    def find_book_by_title(self, title: str):
        for book in self.__books:
            if book.title == title:
                return book.get_info()
        return "Book not found"


if __name__ == "__main__":
    line("Book and Library classes, task 6")
    library = Library()
    book1 = BookFromLibrary("Methodius Buslaev. The Dryad's Necklace", "Dmitry Yemets", 384, 9785699335466)
    book2 = BookFromLibrary("Azazel", "Boris Akunin", 250,  9789662054675)

    library.add_book(book1)
    library.add_book(book2)

    print(library.find_book_by_title("Methodius Buslaev. The Dryad's Necklace")) # ISBN: 9785699335466, Title: Methodius Buslaev. The Dryad's Necklace, Author: Dmitry Yemets, Pages: 384
    print(library.find_book_by_title("Azazel")) # ISBN: 9789662054675, Title: Azazel, Author: Boris Akunin, Pages: 250

    library.remove_book(9785699335466)
    print(f"After delete: {library.find_book_by_title("Methodius Buslaev. The Dryad's Necklace")}") # Book not found
    
# 7) Створіть класи страва, замовлення та ресторан.
# Зробіть меню через яке можна робити замовлення, та оновлювати меню.
# Клас Dish:
# назва
# ціна
# категорія

# Методи:
# повертати опис страви

# Клас Order:
# список страв

# Методи:
# додати страву в замовлення
# видалити страву з замовлення
# повернути загальну суму замовлення

# Клас Restaurant:
# список доступних страв

# Методи:
# додати страву в меню
# вивести список доступних страв

class Dish:
    def __init__(self, name: str, price: float, category: str):
        self.name = name
        self.price = price
        self.category = category

    def get_dish(self):
        return self.__str__()

    def __str__(self):
        return f"Name: {self.name}, Price: {self.price}, Category: {self.category}"
    
class Order:
    def __init__(self):
        self.dishes = []

    def add_dish(self, dish: Dish):
        self.dishes.append(dish)

    def remove_dish(self, dish_name: str):
        self.dishes = [dish for dish in self.dishes if dish.name != dish_name]

    def get_total_order_sum(self):
        return sum(dish.price for dish in self.dishes)
    
class Restaurant:
    def __init__(self):
        self.menu = []

    def add_dish_to_menu(self, dish: Dish):
        self.menu.append(dish)

    def display_menu(self):
        for dish in self.menu:
            print(dish.get_dish())

if __name__ == "__main__":
    line("Dish, Order and Restaurant classes, task 7")
    restaurant = Restaurant()
    dish1 = Dish("Spaghetti Carbonara", 12.99, "Main Course")
    dish2 = Dish("Caesar Salad", 8.99, "Appetizer")
    dish3 = Dish("Tiramisu", 6.99, "Dessert")

    restaurant.add_dish_to_menu(dish1)
    restaurant.add_dish_to_menu(dish2)
    restaurant.add_dish_to_menu(dish3)

    print("Menu:")
    restaurant.display_menu()

    order = Order()
    order.add_dish(dish1)
    order.add_dish(dish3)

    print(f"Total order cost: ${order.get_total_order_sum():.2f}") # Total order cost: $19.98


# 8) Облік студентів з файлами

# Створіть клас StudentDatabase, який зберігає студентів у файлі.
# Клас Student:
# ім'я
# вік
# оцінки

# Методи:
# повернути середню оцінку

# Клас StudentDatabase:
# додати студента у файл
# зчитати студентів з файлу
# знайти студента у файлі

class Student:
    def __init__(self, name: str, age: int, grades: list):
        self.name = name
        self.age = age
        self.grades = grades

    def get_average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0.0
    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Grades: {self.grades}, Average Grade: {self.get_average_grade():.2f}"
    

class StudentDatabase:

    def __init__(self, filename: str, subfolder: str = None, overwrite: bool = False):
        self.filename = filename
        base_dir = Path(__file__).parent
        
        if subfolder:
            target_dir = base_dir / subfolder
            target_dir.mkdir(parents=True, exist_ok=True)
            self.filepath = target_dir / filename
        else:
            self.filepath = base_dir / filename

        if overwrite and self.filepath.exists():
            self.filepath.unlink()
            print(f"Файл {self.filepath.name} был очищен.")

    def add_student(self, student: Student):
        with open(self.filepath, 'a', encoding='utf-8') as file:
            file.write(f"{student.name},{student.age},{','.join(map(str, student.grades))}\n")

    def read_students(self):
        students = []
        if not self.filepath.exists():
            return students
                
        with open(self.filepath, 'r', encoding='utf-8') as file:
            for line in file:
                name, age, *grades = line.strip().split(',')
                students.append(Student(name, int(age), list(map(float, grades))))
        return students

    def get_student(self, name: str):
        students = self.read_students()
        for student in students:
            if student.name == name:
                return student
        return None


def ifRes(res = None, errorText: str = "Student not found.", text: str = "Result:"):
    if not res:
        print(errorText)
        return
    print(f"{text} {res}")



if __name__ == "__main__":
    line("Student and StudentDatabase classes, task 8")

    filename = "students.txt"
    test_filepath = Path(__file__).parent / filename
    need_overwrite = False
    

    if test_filepath.exists():
        choice = input(f"File {filename} already exists. Do you want to rewrite it? (y/n): ").lower()
        if choice == 'y':
            need_overwrite = True
        else:
            print("Using existing file.")

    database = StudentDatabase(filename, overwrite=need_overwrite, subfolder="data")
    student1 = Student("Sata", 17, [11, 8, 9, 11, 12])
    student2 = Student("Bob", 29, [12, 10, 3])

    database.add_student(student1)
    database.add_student(student2)

    print("All students in the database:")
    for student in database.read_students():
        print(student)

    name = "Sata"
    res = database.get_student(name)
    ifRes(res, errorText=f"Student {name} not found.", text=f"Found student {name}:")

    name = "Alex"
    res = database.get_student(name)
    ifRes(res, errorText=f"Student {name} not found.", text=f"Found student {name}:")
        
