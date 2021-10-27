<h1> Future Scandals </h1>

Megan Archibald
Jesse Wilson-Seeley
Nathan Hanlon

Scrum Master: Nathan Hanlon


For our project we are creating an app which allows users to create, share, and follow various blogs. Blogs will be searchable through tags, title, or author. Furthermore, there will be an explore page that will show popular blogs. Users will be able to like blogs using a little heart button. It will be an outline of a red heart and turn solid red when you click it. When creating a blog, users will ideally be able to use the markdown language to insert html tags to customize their post[3].

We are going to use the stream framework package[1] to organize various feeds of blog posts. This will include users they are following, new posts, and a popular posts feed using a revolutionary algorithm for calculating popularity by dividing the number of likes by the time since it was posted. We will then use the taggit package[2] to allow users to add tags to their post so other users can find blogs they are interested in.

The different views for our app will include a homepage, account login page, profile page, search page, account name/blog title page, and search result page. These views will allow the user to easily access blog posts and follow users with blog content that they like. 

These will all be organized in the following apps: accounts, blogs, views. Accounts will contain the views for each user’s profile and such. Blogs will contain the detail view of each blog as well as the edit and create page. Views will contain the homepage, containing the following and popular stream.



[1] https://djangopackages.org/packages/p/stream-framework/
[2] https://django-taggit.readthedocs.io/en/latest/forms.html
[3] https://learndjango.com/tutorials/django-markdown-tutorial 
