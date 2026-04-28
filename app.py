from flask import Flask, render_template_string, request

app = Flask(__name__)


HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>My DevOps App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background-color: #f0f0f0;
        }
        .container {
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
        }
        input {
            padding: 10px;
            margin: 10px;
            width: 200px;
        }
        button {
            padding: 10px 20px;
            background-color: #007bff;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3;
        }
        .message {
            margin-top: 20px;
            padding: 10px;
            background-color: #d4edda;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to My DevOps Project! 🚀</h1>
        <form method="POST">
            <label>Enter your name:</label>
            <input type="text" name="name" placeholder="Your name">
            <button type="submit">Submit</button>
        </form>
        {% if message %}
        <div class="message">
            Hello {{ message }}! Your DevOps pipeline is working! ✅
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    message = None
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            message = name
    return render_template_string(HTML_TEMPLATE, message=message)

@app.route('/health')
def health():
    return {"status": "healthy", "message": "App is running!"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)