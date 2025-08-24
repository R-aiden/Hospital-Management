from flask import Flask
import subprocess

#print("into flask")

app = Flask(__name__)

#@app.route("/")
def home():
    #print("home")
    return '<h2> Click below to open GUI:</h2><font size = "10"><a href = "/open_main_menu">Open Window</a></font>'

#Route to launch main menu
@app.route("/open_main_menu")

def open_main_menu():
    #print("Calling window")
    subprocess.Popen(["python",r"C:\Users\chava\Desktop\Hospital Management\Main menu.py"])
    return "Main menu launched -- you can close this tab."

if __name__ == "__main__":
    app.run(port = 5000)