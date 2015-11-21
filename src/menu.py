from src.database import Database
from src.models.blog import Blog

__author__ = 'ibininja'


class Menu(object):
    def __init__(self):
        ###########################
        # Pseudo Code
        ###########################
        # Ask user for author name
        # Check if they an account
        # IF not create one.
        ###########################

        self.user = input("Enter your author name: ")
        self.user_blog = None

        # The underscore in variable names mean nothing to python; however the developers use it for private attributes/methods naming.
        # so not to call them from other classes,
        if self._user_has_account():
            print("Welcome Back {}".format(self.user))
        else:
            self._prompt_user_for_account()

    def _user_has_account(self):
        blog = Database.find_one('blogs', {'author': self.user})
        if blog is not None:
            #self.user_blog = blog #This would work however returning the object is better for this case
            self.user_blog = Blog.from_mongo(blog['id'])
            return True
        else:
            return False

    def _prompt_user_for_account(self):
        title = input("Enter blog name: ")
        description = input("Enter blog description")
        blog = Blog(author=self.user,
                    title=title,
                    description=description)
        blog.save_to_mongo()
        self.user_blog = blog

    def run_menu(self):
        ###########################
        # Pseudo Code
        ###########################
        # user read or write blog
        # if read:
        # lisst blogs in DB
        # allow user to pick one
        # display posts
        # if write:
        # Check if user has Blog
        # if yes, prompt to write new post
        # Else, prompt to create new blog
        ###########################
        read_or_write = input("Do you want to read (R) or write (W) blogs?")
        if read_or_write == 'R':
            self._list_blogs()
            self._view_blog()
        elif read_or_write == 'W':
            self.user_blog.new_post()
        else:
            print("Thank you for blogging!")

    def _list_blogs(self):
        blogs = Database.find(collection='blogs', query={})

        for blog in blogs:
            print("ID:{}, Title:{}, Author:{}".format(blog['id'], blog['title'], blog['author']))

    def _view_blog(self):
        blog_to_see = input("Enter the ID of the blog you'd like to read: ")
        blog= Blog.from_mongo(blog_to_see)
        posts = blog.get_posts()
        for post in posts:
            print("Date: {}, title:{}\n\n{}".format(post['created_date'], post['title'], post['content']))

