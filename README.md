Blog Post Management with Tagging (Python & MySQL)
Overview

This project is a command-line interface (CLI) application for managing blog posts using Python and MySQL. Users can create, view, list, and search blog posts by tags. The application integrates with a MySQL database to store blog posts and tags in separate tables, with a linking table (post_tags) to associate posts with multiple tags.
Features

    Create a new post: Users can input a title, content, and tags (comma-separated) for the new post.

    List all post titles: Users can view a list of all existing blog post titles.

    View post by title: Users can view the content of a specific post by providing the post's title.

    Search posts by tag: Users can search for posts based on a given tag, displaying all posts associated with that tag.

Technologies Used

    Python: Programming language used to build the CLI app.

    MySQL: Relational database used to store blog posts, tags, and their relationships.

    mysql-connector-python: Python library used for connecting to and interacting with MySQL databases.

Project Setup
Prerequisites

Before running this project, ensure you have the following installed on your system:

    Python 3.x: Install Python from https://www.python.org/downloads/.

    MySQL: Install MySQL from https://dev.mysql.com/downloads/.

    MySQL Connector for Python: Install it using pip:

    pip install mysql-connector-python

    MySQL Workbench (Optional): For managing your database more easily, you can use MySQL Workbench, which is a graphical user interface for MySQL.

Setting Up MySQL Database

    Create the database: Log in to MySQL and create a new database for this project:

CREATE DATABASE blog_app;

Create the required tables:

Run the following SQL commands to create the necessary tables in the blog_app database:

    USE blog_app;

    -- Table to store posts
    CREATE TABLE posts (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        content TEXT NOT NULL
    );

    -- Table to store tags
    CREATE TABLE tags (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) UNIQUE NOT NULL
    );

    -- Linking table for many-to-many relationship between posts and tags
    CREATE TABLE post_tags (
        post_id INT,
        tag_id INT,
        FOREIGN KEY (post_id) REFERENCES posts(id),
        FOREIGN KEY (tag_id) REFERENCES tags(id),
        PRIMARY KEY (post_id, tag_id)
    );

Setting Up the Python Application

    Clone the repository:

    Clone the project to your local machine:

git clone https://github.com/Sylani-55/blog_cli_app.git
cd blog_cli_app

Configure MySQL connection:

Edit the connect_db() function in app.py to include your MySQL database credentials:

def connect_db():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",             # Your MySQL username
        password="your_password", # Your MySQL password
        database="blog_app"       # Database you created
    )
    return connection

Run the application:

Once everything is set up, run the Python application:

    python app.py

    You should now see the menu prompt in your terminal.

Application Usage

Once you run the application, you will see the following menu:

--- Blog Post Management ---
1. Create a new Post
2. List all Post Titles
3. View Post by Title
4. Search Posts by Tag
5. Exit

You can interact with the application by choosing one of the following options:

    Create a new post: Add a new blog post with a title, content, and tags.

    List all post titles: View all titles of the blog posts in the database.

    View post by title: View the content of a specific post by entering its title.

    Search posts by tag: Search for blog posts that are tagged with a specific tag.

    Exit: Exit the application.

File Structure

blog_cli_app/
├── app.py                # Python CLI application code
├── .gitignore            # Git ignore file to exclude unnecessary files
└── README.md             # This readme file
