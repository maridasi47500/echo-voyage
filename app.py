from flask import Flask, render_template, request, session
import os
from yourappdb import query_db, get_db
from flask import g

app = Flask(__name__)
app.secret_key="any string"
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
init_db()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def hello_world():
    user = query_db('select * from contacts')
    the_username = "anonyme"
    one_user = query_db('select * from contacts where first_name = ?',
                [the_username], one=True)
    return render_template("hey.html", users=user, one_user=one_user, the_title="my title")
@app.route("/add_one_country", methods=["GET","POST"])
def add_one_country():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into country (name) values (:name)",hey)
        user = query_db('select * from country')

        return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")


    user = query_db('select * from country')
    one_user = query_db("select * from country limit 1", one=True)
    return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")

@app.route("/add_one_user", methods=["GET","POST"])
def add_one_user():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescountry= query_db("select * from country")

        one_user = query_db("insert into user (username,email,password,phone,country_id) values (:username,:email,:password,:phone,:country_id)",hey)
        user = query_db('select * from user')

        last_user = query_db("select * from user where email = ? and password = ?",[hey["email"], hey["password"]], one=True)
        session["current_user_id"]=last_user["id"]
        for x in ['username','email','password','phone','country_id']:
            session[x]=hey[x]


        return render_template("userform.html", users=user, one_user=one_user, the_title="add new user", touslescountry=touslescountry)


    touslescountry= query_db("select * from country")

    user = query_db('select * from user')
    one_user = query_db("select * from user limit 1", one=True)
    return render_template("userform.html", users=user, one_user=one_user, the_title="add new user", touslescountry=touslescountry)


@app.route("/user_sign_out", methods=["GET","POST"])
def user_sign_out():
    if request.method == 'POST':
        session["current_user_id"]=""
        for x in ['username','email','password','phone','country_id']:
            session[x]=""
        return redirect("/")


@app.route("/user_log_in", methods=["GET","POST"])
def user_login():
    if request.method == 'POST':
        hey=request.form
        last_user = query_db("select * from user where email = ? and password = ?",[hey["email"], hey["password"]], one=True)
        try:
            session["current_user_id"]=last_user["id"]
            for x in ['username','email','password','phone','country_id']:
                session[x]=hey[x]
        except:
            return render_template("userlogin.html")
    return render_template("userlogin.html")
@app.route("/add_one_city", methods=["GET","POST"])
def add_one_city():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescountry= query_db("select * from country")

        one_user = query_db("insert into city (name,country_id) values (:name,:country_id)",hey)
        user = query_db('select * from city')

        return render_template("cityform.html", citys=user, one_user=one_user, the_title="add new city", touslescountry=touslescountry)


    touslescountry= query_db("select * from country")

    user = query_db('select * from city')
    one_user = query_db("select * from city limit 1", one=True)
    return render_template("cityform.html", citys=user, one_user=one_user, the_title="add new city", touslescountry=touslescountry)

@app.route("/add_one_carnetdevoyage", methods=["GET","POST"])
def add_one_carnetdevoyage():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesuser= query_db("select * from user")

        one_user = query_db("insert into carnetdevoyage (title,description,user_id) values (:title,:description,:user_id)",hey)
        user = query_db('select * from carnetdevoyage')

        return render_template("carnetdevoyageform.html", carnetdevoyages=user, one_user=one_user, the_title="add new carnetdevoyage", touslesuser=touslesuser)


    touslesuser= query_db("select * from user")

    user = query_db('select * from carnetdevoyage')
    one_user = query_db("select * from carnetdevoyage limit 1", one=True)
    return render_template("carnetdevoyageform.html", carnetdevoyages=user, one_user=one_user, the_title="add new carnetdevoyage", touslesuser=touslesuser)

@app.route("/add_one_destination", methods=["GET","POST"])
def add_one_destination():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescarnetdevoyage= query_db("select * from carnetdevoyage")

        touslescity= query_db("select * from city")

        one_user = query_db("insert into destination (carnetdevoyage_id,city_id) values (:carnetdevoyage_id,:city_id)",hey)
        user = query_db('select * from destination')

        return render_template("destinationform.html", destinations=user, one_user=one_user, the_title="add new destination", touslescarnetdevoyage=touslescarnetdevoyage, touslescity=touslescity)


    touslescarnetdevoyage= query_db("select * from carnetdevoyage")

    touslescity= query_db("select * from city")

    user = query_db('select * from destination')
    one_user = query_db("select * from destination limit 1", one=True)
    return render_template("destinationform.html", destinations=user, one_user=one_user, the_title="add new destination", touslescarnetdevoyage=touslescarnetdevoyage, touslescity=touslescity)

@app.route("/add_one_son", methods=["GET","POST"])
def add_one_son():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)

        uploaded_file = request.files['zik']
        if uploaded_file.filename != '':
            uploaded_file.save(os.path.join('static/photos', uploaded_file.filename))

        hey["zik"]=uploaded_file.filename


        touslesdestination= query_db("select * from destination")

        touslesuser= query_db("select * from user")

        one_user = query_db("insert into son (zik,destination_id,description,user_id) values (:zik,:destination_id,:description,:user_id)",hey)
        user = query_db('select * from son')

        return render_template("sonform.html", sons=user, one_user=one_user, the_title="add new son", touslesdestination=touslesdestination, touslesuser=touslesuser)


    touslesdestination= query_db("select * from destination")

    touslesuser= query_db("select * from user")

    user = query_db('select * from son')
    one_user = query_db("select * from son limit 1", one=True)
    return render_template("sonform.html", sons=user, one_user=one_user, the_title="add new son", touslesdestination=touslesdestination, touslesuser=touslesuser)

@app.route("/add_one_photo", methods=["GET","POST"])
def add_one_photo():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)

        uploaded_file = request.files['pic']
        if uploaded_file.filename != '':
            uploaded_file.save(os.path.join('static/photos', uploaded_file.filename))

        hey["pic"]=uploaded_file.filename


        touslesuser= query_db("select * from user")

        touslesdestination= query_db("select * from destination")

        one_user = query_db("insert into photo (user_id,pic,destination_id) values (:user_id,:pic,:destination_id)",hey)
        user = query_db('select * from photo')

        return render_template("photoform.html", photos=user, one_user=one_user, the_title="add new photo", touslesuser=touslesuser, touslesdestination=touslesdestination)


    touslesuser= query_db("select * from user")

    touslesdestination= query_db("select * from destination")

    user = query_db('select * from photo')
    one_user = query_db("select * from photo limit 1", one=True)
    return render_template("photoform.html", photos=user, one_user=one_user, the_title="add new photo", touslesuser=touslesuser, touslesdestination=touslesdestination)

@app.route("/add_one_street", methods=["GET","POST"])
def add_one_street():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescity= query_db("select * from city")

        one_user = query_db("insert into street (name,city_id) values (:name,:city_id)",hey)
        user = query_db('select * from street')

        return render_template("streetform.html", streets=user, one_user=one_user, the_title="add new street", touslescity=touslescity)


    touslescity= query_db("select * from city")

    user = query_db('select * from street')
    one_user = query_db("select * from street limit 1", one=True)
    return render_template("streetform.html", streets=user, one_user=one_user, the_title="add new street", touslescity=touslescity)

@app.route("/add_one_track", methods=["GET","POST"])
def add_one_track():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesstreet= query_db("select * from street")

        one_user = query_db("insert into track (composer_artist,title,street_id) values (:composer_artist,:title,:street_id)",hey)
        user = query_db('select * from track')

        return render_template("trackform.html", tracks=user, one_user=one_user, the_title="add new track", touslesstreet=touslesstreet)


    touslesstreet= query_db("select * from street")

    user = query_db('select * from track')
    one_user = query_db("select * from track limit 1", one=True)
    return render_template("trackform.html", tracks=user, one_user=one_user, the_title="add new track", touslesstreet=touslesstreet)

@app.route("/add_one_magasin", methods=["GET","POST"])
def add_one_magasin():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesstreet= query_db("select * from street")

        one_user = query_db("insert into magasin (street_id,name) values (:street_id,:name)",hey)
        user = query_db('select * from magasin')

        return render_template("magasinform.html", magasins=user, one_user=one_user, the_title="add new magasin", touslesstreet=touslesstreet)


    touslesstreet= query_db("select * from street")

    user = query_db('select * from magasin')
    one_user = query_db("select * from magasin limit 1", one=True)
    return render_template("magasinform.html", magasins=user, one_user=one_user, the_title="add new magasin", touslesstreet=touslesstreet)

@app.route("/add_one_article", methods=["GET","POST"])
def add_one_article():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)

        uploaded_file = request.files['pic']
        if uploaded_file.filename != '':
            uploaded_file.save(os.path.join('static/photos', uploaded_file.filename))

        hey["pic"]=uploaded_file.filename


        touslesmagasin= query_db("select * from magasin")

        touslescountry= query_db("select * from country")

        one_user = query_db("insert into article (magasin_id,name,country_id,pic) values (:magasin_id,:name,:country_id,:pic)",hey)
        user = query_db('select * from article')

        return render_template("articleform.html", articles=user, one_user=one_user, the_title="add new article", touslesmagasin=touslesmagasin, touslescountry=touslescountry)


    touslesmagasin= query_db("select * from magasin")

    touslescountry= query_db("select * from country")

    user = query_db('select * from article')
    one_user = query_db("select * from article limit 1", one=True)
    return render_template("articleform.html", articles=user, one_user=one_user, the_title="add new article", touslesmagasin=touslesmagasin, touslescountry=touslescountry)

@app.route("/add_one_ruby_gps", methods=["GET","POST"])
def add_one_ruby_gps():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesstreet= query_db("select * from street")

        one_user = query_db("insert into ruby_gps (lat,lon,street_id,mood,heure,souvenir) values (:lat,:lon,:street_id,:mood,:heure,:souvenir)",hey)
        user = query_db('select * from ruby_gps')

        return render_template("ruby_gpsform.html", ruby_gpss=user, one_user=one_user, the_title="add new ruby_gps", touslesstreet=touslesstreet)


    touslesstreet= query_db("select * from street")

    user = query_db('select * from ruby_gps')
    one_user = query_db("select * from ruby_gps limit 1", one=True)
    return render_template("ruby_gpsform.html", ruby_gpss=user, one_user=one_user, the_title="add new ruby_gps", touslesstreet=touslesstreet)

@app.route("/add_one_creation", methods=["GET","POST"])
def add_one_creation():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)

        uploaded_file = request.files['pic']
        if uploaded_file.filename != '':
            uploaded_file.save(os.path.join('static/photos', uploaded_file.filename))

        hey["pic"]=uploaded_file.filename


        touslesdestination= query_db("select * from destination")

        touslesuser= query_db("select * from user")

        one_user = query_db("insert into creation (destination_id,user_id,title,pic,description) values (:destination_id,:user_id,:title,:pic,:description)",hey)
        user = query_db('select * from creation')

        return render_template("creationform.html", creations=user, one_user=one_user, the_title="add new creation", touslesdestination=touslesdestination, touslesuser=touslesuser)


    touslesdestination= query_db("select * from destination")

    touslesuser= query_db("select * from user")

    user = query_db('select * from creation')
    one_user = query_db("select * from creation limit 1", one=True)
    return render_template("creationform.html", creations=user, one_user=one_user, the_title="add new creation", touslesdestination=touslesdestination, touslesuser=touslesuser)

@app.route("/add_one_limite_map", methods=["GET","POST"])
def add_one_limite_map():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescity= query_db("select * from city")

        touslesuser= query_db("select * from user")

        one_user = query_db("insert into limite_map (lat1,lat2,lon1,lon2,city_id,user_id) values (:lat1,:lat2,:lon1,:lon2,:city_id,:user_id)",hey)
        user = query_db('select * from limite_map')

        return render_template("limite_mapform.html", limite_maps=user, one_user=one_user, the_title="add new limite_map", touslescity=touslescity, touslesuser=touslesuser)


    touslescity= query_db("select * from city")

    touslesuser= query_db("select * from user")

    user = query_db('select * from limite_map')
    one_user = query_db("select * from limite_map limit 1", one=True)
    return render_template("limite_mapform.html", limite_maps=user, one_user=one_user, the_title="add new limite_map", touslescity=touslescity, touslesuser=touslesuser)

