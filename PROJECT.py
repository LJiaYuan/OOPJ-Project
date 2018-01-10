from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def Root():
    return render_template('Reward.html')

@app.route('/home')
def home():
    return render_template('HomePage.html')

@app.route('/Reward')
def Reward():
    return render_template('Reward.html')

if __name__ == '__main__':
    app.run()
