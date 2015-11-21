from src.menu import Menu
from src.models.blog import Blog
from src.models.post import Post
from src.database import Database

__author__ = 'ibininja'

Database.initialize()

#post = Post(blog_id="125",
#            title="Healthy Banana",
#           content="This is the content of Healthy Banana name published articles....",
#            author="Mohamed")
#post.save_to_mongo()

#posts = Post.from_blog('125')
#for post in posts:
#    print(post)

#posts = Post.from_mongo('3782101c9d3d4e5eae511d8f3180f8d5')
#print(posts)

#This below is to test Blog
# blog = Blog(author="Ibrahim",
#             title="Sample Title",
#             description="Sample Description")
# blog.new_post()
# blog.save_to_mongo()
# from_database= Blog.from_mongo(blog.id)
# print(blog.get_posts())

#This below is the normal fully fledged running blog:
menu = Menu()
menu.run_menu()