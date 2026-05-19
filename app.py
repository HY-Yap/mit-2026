from flask import Flask, render_template, request
from helperfuncs import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/fitnessplan", methods = ["GET", "POST"])
def fitness():
    if request.method == "GET":
        return render_template("form.html")
    elif request.method == "POST":
        data = request.form.to_dict()
        print(data)

        #Process the data (This part can probably be turned into a helper function)
        start_time = time_to_seconds(int(data["start_mins"]), int(data["start_secs"]))
        target_time = time_to_seconds(int(data["target_mins"]), int(data["target_secs"]))

        if data["sequence"] == "arithmetic": #find out which function to use
            result = decr_arith_seq(start_time, target_time, int(data["improvement"]))
        elif data["sequence"] == "geometric":
            result = decr_geo_seq(start_time, target_time, float(data["improvement"]))
        else:
            result = "Error"

        result = list(map(seconds_to_time, result))





        
        #render the final result
        return f"i like eating haagendazs <br>{result}" #placeholder
    
if __name__ == "__main__":
    app.run(debug=True)
