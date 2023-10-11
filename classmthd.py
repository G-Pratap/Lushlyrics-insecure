# class Developer:
#     LIMIT = 3

#     def __init__(self, name, age):
#         self.name = name
#         self. age = age
#         self.skills = []

#     def add_skills(self, skills):
#         if len(self.skills) < Developer.LIMIT:
#             self.skills.append(skills)
#             print("Skills added successfully")

#         else:
#             print(f"Skills count cannot exceed {Developer.LIMIT}")

#     @classmethod
#     def set_limits(cls, limit):
#         cls.LIMIT = limit

# class Player:
#     Max_Hearts = 3
#     def __init__(self, name):
#         self.name = name
#         self.hearts = Player.Max_Hearts

#     def __str__(self):
#         print(f"The player name : {self.name} and has {self.hearts} hearts")

#     def lose(self):
#         if self.hearts > 0:
#             self.hearts -= 1
#             print(f"You lose but you have {self.hearts} hearts left")
#         else:
#             print("Game Over!")

class ShoppintList:
    def __init__(self, items):
        self.items = items 

    @classmethod
    def from_string(cls, text):
        items = text.split(',')
        return cls(items)




