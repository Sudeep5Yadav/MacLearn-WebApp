from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/download")
def download():
    return render_template('download.html')

@app.route("/download/MacLearn")
def MacLearn():
    return render_template('downloadMacLearn.html')

@app.route("/download/MacDecrypt")
def MacDecrypt():
    return render_template('downloadMacDecrypt.html')

@app.route("/about")
def About():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)