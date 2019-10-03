class User:
	active_users = 0
	
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		User.active_users +=1
	
	def full_name(self):
		return f"{self.first} {self.last}"
	
	def initials(self):
		return f"{self.first[0]} {self.last[0]}"
	
	def likes(self, thing):
		return f"{self.first} likes {thing}"
	
	def is_senior(self):
		return self.age >= 65
	
	def birthday(self):
		self.age += 1
		return f"Happy {self.age}th birthday, {self.first}"
	
	def logout(self):
		User.active_users -=1


user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)

print(user1.likes("Ice Cream"))
print(user2.likes("Chips"))


# user1 = User("Joe", "Gatto", 34)
# print(user1.full_name())
# print(user1.initials())
