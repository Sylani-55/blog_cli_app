import mysql.connector

# Connecting to MySQL
def connect_db():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",             # Your MySQL username
        password="Sy,lan786", # Your MySQL password
        database="blog_app"       # Database we'll create later
    )
    return connection
# 1. Import mysql.connector
import mysql.connector

# 2. Connection function
def connect_db():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sy,lan786",  # <-- replace with your real MySQL password
        database="blog_app"         # <-- we'll create this database soon
    )
    return connection

# 3. Menu function
def menu():
    while True:
        print("\n--- Blog Post Management ---")
        print("1. Create a new Post")
        print("2. List all Post Titles")
        print("3. View Post by Title")
        print("4. Search Posts by Tag")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            create_post()
        elif choice == '2':
            list_posts()
        elif choice == '3':
            view_post()
        elif choice == '4':
            search_posts()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid input. Please try again.")

def create_post():
    connection = connect_db()
    cursor = connection.cursor()

    title = input("Enter Post Title: ")
    content = input("Enter Post Content: ")
    tags_input = input("Enter tags (comma-separated): ")

    # Insert into posts table
    insert_post_query = "INSERT INTO posts (title, content) VALUES (%s, %s)"
    cursor.execute(insert_post_query, (title, content))
    post_id = cursor.lastrowid

    # Process tags
    tags = [tag.strip() for tag in tags_input.split(",")]

    for tag in tags:
        # Check if tag exists
        cursor.execute("SELECT id FROM tags WHERE name = %s", (tag,))
        tag_data = cursor.fetchone()
        if tag_data:
            tag_id = tag_data[0]
        else:
            # Insert new tag
            cursor.execute("INSERT INTO tags (name) VALUES (%s)", (tag,))
            tag_id = cursor.lastrowid
        
        # Insert into post_tags
        cursor.execute("INSERT INTO post_tags (post_id, tag_id) VALUES (%s, %s)", (post_id, tag_id))

    connection.commit()
    cursor.close()
    connection.close()

    print("Post created successfully!")

def list_posts():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("SELECT title FROM posts")
    posts = cursor.fetchall()

    if posts:
        print("\n--- All Blog Post Titles ---")
        for post in posts:
            print(f"- {post[0]}")
    else:
        print("No posts found.")

    cursor.close()
    connection.close()

def view_post():
    connection = connect_db()
    cursor = connection.cursor()

    title = input("Enter the title of the post you want to view: ")

    query = "SELECT content FROM posts WHERE title = %s"
    cursor.execute(query, (title,))
    result = cursor.fetchone()

    if result:
        print("\n--- Post Content ---")
        print(result[0])
    else:
        print("Post not found.")

    cursor.close()
    connection.close()

def search_posts():
    connection = connect_db()
    cursor = connection.cursor()

    tag = input("Enter the tag to search posts: ")

    query = """
    SELECT posts.title
    FROM posts
    JOIN post_tags ON posts.id = post_tags.post_id
    JOIN tags ON tags.id = post_tags.tag_id
    WHERE tags.name = %s
    """
    cursor.execute(query, (tag,))
    results = cursor.fetchall()

    if results:
        print(f"\n--- Posts tagged with '{tag}' ---")
        for row in results:
            print(f"- {row[0]}")
    else:
        print(f"No posts found with tag '{tag}'.")

    cursor.close()
    connection.close()

if __name__ == "__main__":
    menu()
