posts=[]
captions=[]


class User():
	def __init__(self,name,email,password):
		self.name=name
		self.email=email
		self.password=password
		self.friends_list=[]
		self.messages_list=[]
	
	def add_friend(self,email):
		self.friends_list.append(email)
		print(self.name + " has added " + email + " as a friend ")
	
	def remove_friend(self,email):
		self.friends_list.remove(email)
		print(self.name +" has removed " + email + " from freinds ")

	def create_post(self,text):
		posts.append(text)
		print(self.name + " has posted " + text)
		

	
	def get_userInfo(self):
		print("Name" + self.name )
		print("Email" + self.email )
		print("Password" + self.password)
		print("freinds" + str(self.friends_list))
		print("Posts" + str(posts))
	
	def send_message(self,email,text):
		self.messages_list.append(email)
class Post():
	def __init__(self,name,caption,author ,comments=[]):
		self.name=name
		self.caption=caption 
		self.comments=[]
		self.author=author

	
	def add_caption(self,caption_text):
		self.caption_text=caption_text
		captions.append(caption_text)
		print(self.name + " has added a caption" + caption_text)
	
	def add_comment(self, comment_text):
		self.comment_text = comment_text
		self.comments.append(comment_text)
		print(self.name + " has added a comment: " + comment_text)
	
	def like_post(self):
		print(self.name +"has liked your post !")
class Comment(Post):
	pass		
user1 = User(" Layan"," layann.hamdan@gmail.com"," layan123")
user2 = User(" celine"," celine.yaghi@gmail.com", " ceine1234")
user1.add_friend("celine.yaghi@gmail.com")
user2.create_post("happy birthday")
user1.get_userInfo()
user2.get_userInfo()
user1.remove_friend("celine.yaghi@gmail.com")
post1 = Post("layan","food is great","comment")
post1.add_caption(" hi")
user1.send_message("celine.yaghi@gmail.com","hi")

