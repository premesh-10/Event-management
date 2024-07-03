from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# Set up MongoDB client
client = MongoClient("mongodb://localhost:27017/")
db = client.event_management
events_collection = db.events

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_event', methods=['GET', 'POST'])
def add_event():
    if request.method == 'POST':
        event = {
            'name': request.form['name'],
            'date': request.form['date'],
            'location': request.form['location'],
            'description': request.form['description']
        }
        events_collection.insert_one(event)
        return redirect(url_for('view_events'))
    return render_template('add_event.html')

@app.route('/view_events')
def view_events():
    events = events_collection.find()
    return render_template('view_events.html', events=events)

if __name__ == '__main__':
    app.run(debug=True)
