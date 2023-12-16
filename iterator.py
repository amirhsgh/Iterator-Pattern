# classic method

# from dataclasses import dataclass

# @dataclass
# class Post:
#     text:str
#     author:str

# posts = [
#     Post(text="Post about design patterns", author="Uncle Bob"),
#     Post(text="Post about advanced design patters", author="Uncle Bob"),
#     Post(text="Post about software architecture", author="Uncle Bob"),
#     Post(text="Post about machine learning", author="Uncle Bob"),
#     Post(text="Post about operating systems", author="John Doe"),
#     Post(text="Post about computer networks", author="John Doe"),
# ]

# keywords = "design patterns"
# for post in posts:
#     if post.text.find(keywords) > -1:
#         print(post)

# design pattern method

from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Post:
    text:str
    author:str

class Iterator(ABC):
    
    @abstractmethod
    def get_next(self):
        pass

    @abstractmethod
    def has_next(self):
        pass


class Postiterator(Iterator):
    def __init__(self, posts):
        self.__posts = posts
        self.__index = 0


    def get_next(self):
        if self.has_next():
            result = self.__posts[self.__index]
            self.__index += 1
            return result
        return None

    def has_next(self):
        return self.__index < len(self.__posts)
    

class IterableCollection(ABC):

    @abstractmethod
    def create_iterator(self, items) -> Iterator:
        pass

class PostCollection(IterableCollection):

    def __init__(self):
        self.__posts = [
            Post(text="Post about design patters", author="Uncle Bob"),
            Post(text="Post about advanced design patterns", author="Uncle Bob"),
            Post(text="Post about software architecture", author="Uncle Bob"),
            Post(text="Post about machine learning", author="Uncle Bob"),
            Post(text="Post about operating systems", author="John Doe"),
            Post(text="Post about computer networks", author="John Doe"),
        ]


    def create_iterator(self, items) -> Iterator:
        return Postiterator(items)
    
    def search_by_text(self, keyword):
        return self.create_iterator(list(filter(
            lambda post:post.text.find(keyword) > -1,
            self.__posts
        )))

    def search_by_author(self, keyword):
        return  self.create_iterator(list(filter(
            lambda post:post.author.find(keyword) > -1,
            self.__posts
        )))
    


post_coll = PostCollection()
posts = post_coll.search_by_text("design patterns")


while posts.has_next():
    print(posts.get_next())


print("===============================")
post_collection = PostCollection()
posts = post_collection.search_by_author("Uncle Bob")

while posts.has_next():
    print(posts.get_next())