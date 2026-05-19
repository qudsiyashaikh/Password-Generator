import random
import string
from flask import Flask, render_template_string, request

app = Flask(__name__)

# --- HTML & CSS TEMPLATE ---
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Random Password Generator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f4f9;
            text-align: center;
            margin-top: 50px;
        }
        .container {
            display: inline-block;
            padding: 30px;
            background: white;
            border-radius: 10px;
            box-shadow: 0px 0px 15px rgba(0,0,0,0.1);
            width: 400px;
            text-align: left;
        }
        h2 { text-align: center; color: #333; }
        label { font-weight: bold; display: block; margin-top: 15px; }
        input[type="number"] {
            width: 100%;
            padding: 10px;
            margin-top: 5px;
            border: 1px solid #ccc;
            border-radius: 5px;
            box-sizing: border-box;
        }
        .checkbox-group {
            margin-top: 15px;
            display: flex;
            align-items: center;
        }
        .checkbox-group input { margin-right: 10px; transform: scale(1.2); }
        button {
            width: 100%;
            background-color: #28a745;
            color: white;
            border: none;
            padding: 12px;
            font-size: 16px;
            font-weight: bold;
            border-radius: 5px;
            cursor: pointer;
            margin-top: 20px;
        }
        button:hover { background-color: #218838; }
        .result-box {
            margin-top: 25px;
            background: #e9ecef;
            padding: 15px;
            border-radius: 5px;
            text-align: center;
            word-break: break-all;
        }
        .password {
            font-size: 20px;
            font-family: 'Courier New', monospace;
            font-weight: bold;
            color: #d9534f;
        }
    </style>
</head>
<body>

<div class="container">
    <h2>Password Generator</h2>
    
    <form method="POST">
        <!-- Length Choose Feature -->
        <label for="length">Password Length (8-32):</label>
        <input type="number" id="length" name="length" min="8" max="32" value="{{ length if length else 12 }}" required>
        
        <!-- Symbols Feature -->
        <div class="checkbox-group">
            <input type="checkbox" id="include_symbols" name="include_symbols" {% if include_symbols %}checked{% endif %}>
            <label for="include_symbols">Include Symbols (@, #, $, etc.)</label>
        </div>
        
        <button type="submit">Generate Password</button>
    </form>

    <!-- Result Display -->
    {% if password %}
        <div class="result-box">
            <strong>Your Random Password:</strong>
            <div class="password">{{ password }}</div>
        </div>
    {% endif %}
</div>

</body>
</html>
"""

# --- BACKEND LOGIC FUNCTIONS ---
def generate_password(length, include_symbols):
    # Strings Concept: Alphabets aur Numbers ko lena
    characters = string.ascii_letters + string.digits
    
    # Condition: Agar user ko symbols chahiye toh unhe add karna
    if include_symbols:
        characters += string.punctuation  # contains characters like !@#$%^&*()
        
    password = ""
    
    # Loops Concept: Jitni length chahiye utni baar loop chalana
    for i in range(length):
        # Random Module Concept: Characters me se ek random akshar chunna
        random_char = random.choice(characters)
        password += random_char
        
    return password


# --- FLASK ROUTE ---
@app.route('/', methods=['GET', 'POST'])
def home():
    password = ""
    length = 12
    include_symbols = False

    if request.method == 'POST':
        # Form se data uthana
        length = int(request.form.get('length', 12))
        include_symbols = 'include_symbols' in request.form  # True agar checked hai, else False
        
        # Function call karke password generate karna
        password = generate_password(length, include_symbols)

    return render_template_string(HTML, password=password, length=length, include_symbols=include_symbols)


if __name__ == '__main__':
    app.run(debug=True)