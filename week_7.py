"""
TASK 1

Write a class to represent a Cash Register.
You class should keep the state of price total and purchased items

Below is a starter code:
------------------------
1. you can add new variables and function if you want to
2. you will NEED to add accepted method parameters where required.
For example, method add_item probably accepts some kind of an item?..
3. You will need to write some examples of how your code works.
"""

class CashRegister:

    def __init__(self, discount=0):

        self.total_items = dict()
        self.total_price = 0
        self.discount = discount

    def add_discount(self, new_discount):  # updating the discount
        self.discount = new_discount

    def add_item(self, item, price):
        self.total_items[item] = price
        pass

    def remove_item(self, item):
        self.total_items.pop(item)
        pass

    def apply_discount(self):
        discounted_price = self.total_price - (self.total_price/self.discount)
        except ZeroDevisionError:
            print("There is no discount available")
        else:
            self.total_price = discounted_price
        pass

    def get_total(self):
        self.total_price = sum(self.total_items.values())
        self.apply_discount()

        pass

    def show_items(self):
        msg = """
                ====================
                Items purchased
                ---------------
                {}

                Total: {}

                Thank you!
                ====================
                """
        width = 20
        records = []

        for k, v in self.total_items.items():
            txt = len(k)
            digits = len(str(v))
            characters = width - txt - digits
            r = "{}{}{}".format(k, '.' * characters, v)
            records.append(r)

        all_records = '        \n'.join(records)
        final_msg = msg.format(all_records, self.total_price)
        print(final_msg)
        pass

    def reset_register(self):
        self.total_price = 0
        self.total_items.clear()
        self.discount = 0
        pass

"""
TASK 2

Write a base class to represent a student. Below is a starter code. 
Feel free to add any more new features to your class. 
As a minimum a student has a name and age and a unique ID.

Create a new subclass from student to represent a concrete student doing a specialization, for example:
Software Student and Data Science student. 
"""

class Student:

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = dict()

        def add_subjects(self, list_of_subjects):
            for subject in list_of_subjects:
                self.subjects[subject] = None

class CFGStudent(Student):
    def __init__(self, stream, *args, **kwargs):
        super().__init__(*args, **kwargs):
        self.specialisation = stream

    def add_subject(self, subject):
        self.subjects[subject] = None

    def view_all_subjects(self):
        return list(self.subjects.keys())

    def update_grade(self, subject, grade):
        self.subjects[subject] = grade

    def get_overall_mark(self):
        current = dict({(k, v) for k, v in self.subjects.items() if v is not None})
        return sum(current.values()) / len(current.values())