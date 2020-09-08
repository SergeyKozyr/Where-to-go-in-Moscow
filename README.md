# Map of Moscow's interesting places

Interactive map of the most interesting places in Moscow, such as: 

- Guided tours 
- Museums 
- Scenic viewpoints 
- and other different sights.

Each place has a set of photos, a description and contact information.

---

<img src="screenshots/readme.gif">

---
- The data is taken from [Kudago](https://kudago.com/msk/)

- [Website](http://kozyrsergey.pythonanywhere.com/)

- [Admin page](http://kozyrsergey.pythonanywhere.com/admin)

- Admin credentials:
    - username: admin
    - password: password234


## How to run locally
1. Clone the repo

1. Install dependencies 

        pip install -r requirements.txt

1. Create .env with the variables `SECRET_KEY="Secret key"` and `DEBUG=False`. About [SECRET_KEY](https://docs.djangoproject.com/en/3.1/ref/settings/#secret-key) and [DEBUG](https://docs.djangoproject.com/en/3.1/ref/settings/#debug)

1. Add places on map 

        python manage.py load_place raw json file url

    [List of places](https://github.com/devmanorg/where-to-go-places/tree/master/places)

1. Run development server

        python manage.py runserver

1. Go to <http://localhost:8000/> or <http://127.0.0.1:8000/>

1. Admin page is located at  <http://localhost:8000/admin>, credentials are stated above

## Project Goals
The code is written for educational purposes on online-course for web-developers [dvmn.org](dvmn.org)