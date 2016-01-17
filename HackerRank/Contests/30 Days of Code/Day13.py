'''
Day 13: Abstract Classes!

In the editor we have provided the abstract Book class and a Solution class. In the Solution class we created instance of a class called MyBook. Your task is to write just the MyBook class. The class MyBook mustn't be public.

Note: Since this is a very specific Object-Oriented topic, we have only enabled a few languages for which abstract classes make sense. If you don't find your favorite language, try to experiment with the provided languages or come back for the upcoming challenges.

Input Format

Input from STDIN is already handled in the code given in the editor. MyBook's constructor must have the following parameters: String title, String author, and int price.

Output Format

The void display() method should print and label the respective title, author, and price of the book's instance (with each value on its own line) like so:

Title: $title
Author: $author
Price: $price
Note: The $ is prepended to variable names to indicate they are placeholders for variables.

Sample Input

The Alchemist
Paulo Coelho
248
Sample Output

Title: The Alchemist
Author: Paulo Coelho
Price: 248
'''

from abc import ABCMeta, abstractmethod
class Book:
    __metaclass__ = ABCMeta
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

#Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        self.price = price
        super(MyBook, self).__init__(title, author)
    def display(self):
        print "Title:", self.title
        print "Author:", self.author
        print "Price:", self.price
	
title=raw_input()
author=raw_input()
price=int(raw_input())
new_novel=MyBook(title,author,price)
new_novel.display()