
# Smart-Health

A management system for smart-Health Care.


## The system includes:

 - Registration of patients, doctors.
 - Making appointments.
 - Storing patient records.
 - Prescribing patients.

### Doctor dashboard
 
 - To access doctor dashboard, requires the user to authenticate themselves through login as doctor.
 - Can view their appointments and patient details. 
 - Can prescribe patients.

### Patient dashboard

 - Can book appointments. (Login required)
 - Can view all the registered doctors details.


## Running the application

- Install Python. (Don't Forget to Tick 'Add to Path while installing Python)
- Download this project zip folder and extract it.
- Move to project folder in Terminal. Then run following Commands:          
    - pip install -r requirements.txt
- Open the MySql database admin panel into your browser and create a new database named "healthcareSystem".
- Again go to the terminal and run the following Commands:
    - python manage.py makemigrations
    - python manage.py migrate
    - python manage.py runserver
- Now enter the (http://127.0.0.1:8000/) URL in your browser.
