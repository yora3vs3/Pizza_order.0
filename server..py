from flask import Flask, render_template, send_from_directory

app = Flask(_name_)

# Serve HTML files
@app.route('/')
def index():
    return render_template('order.html')

# Serve static files (CSS, JavaScript, images, etc.)
@app.route('/')
def static_files(path):
    return send_from_directory('static', path)

if _name_ == '_main_':
    app.run(debug=True)