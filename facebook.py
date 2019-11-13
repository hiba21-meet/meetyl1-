class User():
	def __init__(self,name,email,password):
		self.name=name
		self.email=email
		self.password=password
		self.friends_list=[]
		self.posts=[]
	def add_friend(self,email):
		self.friends_list.append(email)
		print(self.name + " has added " + email + " as a friend ")
	def remove_friend(self,email):
		self.friends_list.remove(email)
		print(self.name +" has removed " + email + " from freinds ")
	def create_post(self,text):
		self.posts.append(text)
		print(self.name + " has posted " + text)
	def get_userInfo(self):
		print("Name" + self.name )
		print("Email" + self.email )
		print("Password" + self.password)
		print("freinds" + str(self.friends_list))
		print("Posts" + str(self.posts))
user1 = User(" Layan"," layann.hamdan@gmail.com"," layan123")
user2 = User(" celine"," celine.yaghi@gmail.com", " ceine1234")
user1.add_friend("celine.yaghi@gmail.com")
user2.create_post("happy birthday")
user1.get_userInfo()
user2.get_userInfo()
user1.remove_friend("celine.yaghi@gmail.com")
class Post():




