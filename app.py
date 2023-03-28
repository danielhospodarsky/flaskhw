from flask import Flask, request, render_template, redirect, url_for,

app = Flask(__name__)

friends_dict = [
    {"name": "Test", "flavor": "swirl", "read": "yes", "activities": "reading"}
]


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template(
        "index.html", pageTitle="Web form template", friends=friends_dict
    )


@app.route("/add", methods=["POST"])
def add():
    print("inside add function")
    if request.method == "POST":

        form = request.form

        fname = form["fname"]
        flavor = form["flavor"]
        read = form["read"]
        activities = form.getlist("activities")  # this is a Python list

        print(fname)
        print(flavor)
        print(read)
        print(activities)

        activities_string = ", ".join(activities)  # make the Python list into a string

        friend_dict = {
            "name": fname,
            "flavor": flavor,
            "read": read,
            "activities": activities_string,
        }

        print(friend_dict)
        friends_dict.append(
            friend_dict
        )  # append this dictionary entry to the larger friends dictionary
        print(friends_dict)
        return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))

@app.route("/about")
def about():
    return render_template('about.html')
    

# Route for homepage 
"""
import csv

@app.route("/")
def index():
    return render_template("index.html")

# Route for adding data
@app.route("/add", methods=["POST"])
def add_data():
    # Collect data from form
    name = request.form.get("name")
    email = request.form.get("email")
    age = request.form.get("age")
    
    # Open CSV file and write data
    with open("data.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([name, email, age])
    
    return "Data received and processed successfully."

# Route for about page
@app.route("/about")
def about():
    return render_template("about.html")
"""
