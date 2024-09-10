from flask import Flask, request, redirect, url_for
import csv
import os

app = Flask(__name__)

# Ensure the data directory exists
os.makedirs('data', exist_ok=True)

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    # Save to a CSV file
    with open('data/contact_form_submissions.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, email, message])
    
    return redirect(url_for('thank_you'))

@app.route('/thank-you')
def thank_you():
    return "Thank you for your message! We will get back to you soon."

if __name__ == '__main__':
    app.run(debug=True)
