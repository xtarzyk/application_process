from flask import Flask, render_template, request, url_for, redirect

import data_manager

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/mentors')
def mentors_list():
    mentor_name = request.args.get('mentor-last-name')
    city = request.args.get('city-input')
    cities = data_manager.get_cities()

    if mentor_name:
        mentor_details = data_manager.get_mentors_by_last_name(mentor_name)
    elif city:
        mentor_details = data_manager.get_mentors_by_city(city)
    else:
        mentor_details = data_manager.get_mentors()

    # We get back a list of dictionaries from the data_manager (for details check 'data_manager.py')

    return render_template('mentors.html', mentors=mentor_details, cities=cities)

@app.route('/applicants-phone')
def applicants_phone():
    applicant_name = request.args.get('applicant-name')
    applicant_details = data_manager.get_applicant_data_by_name(applicant_name)
    return render_template('phone.html', applicants=applicant_details, name=applicant_name)

@app.route('/applicants-email')
def applicants_email():
    applicant_email_ending = request.args.get('applicant-email-ending')
    applicant_details = data_manager.get_applicant_data_by_email_ending(applicant_email_ending)
    return render_template('email.html', endings=applicant_details, email_ending=applicant_email_ending)


if __name__ == '__main__':
    app.run(debug=True)
