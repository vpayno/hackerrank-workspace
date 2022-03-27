#!/usr/bin/env python3

from abc import ABCMeta, abstractmethod


class Book(object, metaclass=ABCMeta):

    def __init__(self, title, author):
        self.title = title
        self.author = author

    @staticmethod
    @abstractmethod
    def display():
        pass


class MyBook(Book):

    def __init__(self, title: str, author: str, price: int):
        super().__init__(title, author)
        self.price: int = price

    def display(self):
        print(f"Title: {title}")
        print(f"Author: {author}")
        print(f"Price: {price}")


title = input()
author = input()
price = int(input())
new_novel = MyBook(title, author, price)
new_novel.display()
