from flask import Flask, render_template, redirect, request, flash, session
import model, json
app = Flask(__name__)
app.secret_key = '\xf5!\x07!qj\xa4\x08\xc6\xf8\n\x8a\x95m\xe2\x04g\xbb\x98|U\xa2f\x03'


@app.route("/")
def index():
    user_list = model.session.query(model.User).limit(5).all()
    return render_template("user_list.html", user_list=user_list)

@app.route("/createuser", methods=["GET"])
def show_createuser():
    return render_template("create_user.html")

@app.route("/createuser", methods=["POST"])
def createuser():
    user = model.User(email=request.form['email'], 
        password=request.form['password'], age=request.form['age'], 
        zipcode=request.form['zipcode'])
    print request.form['email']
    r = model.session.query(model.User).filter_by(email = request.form['email']).all()
    print type(r)
    print r[0].email
    if len(r) > 0:
        print "Hello"
        return redirect("/login")
    model.session.add(user)
    model.session.commit()
    print "User has been added"
    return "User has been added"


@app.route("/login", methods=["GET"])
def show_login():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def process_login():
    #user = model.User()
    email = request.form['email']
    r = model.session.query(model.User).filter_by(email = email).all()
    
    if len(r)==0:
        #user does not exist in database
        return redirect("/createuser")
    else:
        user = r[0]
        if user.password != request.form['password']:
            #passwords do not match/ Want to Flash method.
            print("Your password does not match")
            #message = 'Passwords do not match, please try again'
            #flash(message)
            return redirect("/login")        
        else:
            #passwords match store in session
            session['userid'] = user.id
            print session['userid']
            return redirect("/")

@app.route("/viewusers")
def viewusers():

    v = model.session.query(model.User).all()
    return render_template("user_list.html", user_list=v)



#@app.route("/melon/<int:id>")
@app.route("/userreviews/<int:id>")
def viewreviews():

    #for request.args['user.id']
    #v = model.session.query(model.User).all()
    return render_template("userreviews.html")#, user_list=v)

@app.route("/sessionclear")
def clear_session():
    session.clear()
    return "Clearing"
            

    


    """TODO: Receive the user's login credentials located in the 'request.form'
    dictionary, look up the user, and store them in the session."""


if __name__ == "__main__":
    app.run(debug = True)