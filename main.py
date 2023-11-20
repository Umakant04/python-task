from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

# Fake user data for demo purposes (replace this with a proper user authentication system)
fake_users = {
    "username": "password"
}

@app.get("/", response_class=HTMLResponse)
async def login_page(request: Request):
    return """
    <html>
    <body>
        <h1>Login</h1>
        <form action="/login" method="post">
            <label for="username">Username:</label><br>
            <input type="text" id="username" name="username"><br>
            <label for="password">Password:</label><br>
            <input type="password" id="password" name="password"><br><br>
            <input type="submit" value="Submit">
        </form>
    </body>
    </html>
    """

@app.post("/login", response_class=HTMLResponse)
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
    if username in fake_users and fake_users[username] == password:
        return """
        <html>
        <body>
            <h2>Login Successful!</h2>
            <form action="/add_user" method="get">
                <input type="submit" value="Add User">
            </form>
        </body>
        </html>
        """
    else:
        return "Invalid credentials"

@app.get("/add_user", response_class=HTMLResponse)
async def add_user_page():
    return """
    <html>
    <body>
        <h1>Add User</h1>
        <form action="/add_user" method="post">
            <label for="new_username">New Username:</label><br>
            <input type="text" id="new_username" name="new_username"><br>
            <label for="new_password">New Password:</label><br>
            <input type="password" id="new_password" name="new_password"><br><br>
            <input type="submit" value="Add">
        </form>
    </body>
    </html>
    """

@app.post("/add_user", response_class=HTMLResponse)
async def add_user(new_username: str = Form(...), new_password: str = Form(...)):
    # Handle adding user logic here (e.g., adding to a database)
    # For simplicity, let's just update fake_users
    fake_users[new_username] = new_password
    return f"User {new_username} added successfully!"