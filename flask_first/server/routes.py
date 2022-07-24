from flask import render_template, request, redirect, url_for, session

from . import SERVER_BLUEPRINT
from .forms import UserForm
from flask_first.db.models import DB, Users


# CRUD -> INSERT, SELECT, UPDATE, DELETE

# domyslnie Flask korzysta z method GET, nie musisz dodawac  methods=["GET"]
@SERVER_BLUEPRINT.route("/welcome/<string:user_name>")
def welcome_user(user_name: str):
    return render_template("welcome_user.html", user_name=user_name)


# TODO Bye route!
@SERVER_BLUEPRINT.route("/bye_user/<string:user_name>")
def bye_user(user_name: str):
    session.permanent = True
    return render_template("bye_user.html", user_name=user_name)


@SERVER_BLUEPRINT.route("/create_new_user/", methods=["GET", "POST"])
def create_user():
    user_form = UserForm()
    session.permanent = True
    if request.method == "POST":
        DB.session.add(Users(name=user_form.name.data, surname=user_form.surname.data, sex=user_form.sex.data,
                             age=user_form.age.data, position=user_form.position.data))
        DB.session.commit()
        return redirect(url_for(".show_new_user", new_user_name=user_form.name.data))

    return render_template("user_form.html", form=user_form)


# pokazuje nowego uzytkownika w petli for
@SERVER_BLUEPRINT.route("/show_new_user/")
def show_new_user():
    session.permanent = True
    print(request.args["new_user_name"])
    new_user = Users.query.filter_by(name=request.args["new_user_name"]).first()
    return render_template("show_created_user.html", new_user=new_user)


@SERVER_BLUEPRINT.route("/all_users/")  # pokazuje wszystkich dodanych uzytkownikow
def show_all_users():
    session.permanent = True
    return render_template("all_users.html", all_users=Users.query.all())


# UPDATing user
@SERVER_BLUEPRINT.route("/update/<int:id_>", methods=["GET", "POST"])
def update(id_: int):
    session.permanent = True
    user_form = UserForm()
    user = Users.query.filter_by(id_=id_).first()
    print(user)
    if request.method == 'POST':
        if user:
            DB.session.delete(user)
            DB.session.commit()

            DB.session.add(Users(id_=id_, name=user_form.name.data, surname=user_form.surname.data,
                                 age=user_form.age.data, sex=user_form.sex.data, position=user_form.position.data))

            DB.session.commit()
            return redirect("/all_users")
        return f"Nie mozesz zaktualizowac tego uzytkownika bo nie ma ID o numerze: {id_}"

    return render_template('update.html', user=user)


# Delete user
@SERVER_BLUEPRINT.route('/delete/<int:id_>', methods=['GET', 'POST'])
def delete(id_: int):
    session.permanent = True
    user_to_delete = Users.query.filter_by(id_=id_).first()
    if request.method == 'POST':
        if user_to_delete:
            DB.session.delete(user_to_delete)
            print(user_to_delete)
            DB.session.commit()
            return redirect('/all_users')  # przekierowuje nas na strone ze wszystkimi uzytkownikami
        return f"Nie ma uzytkownika o ID {id_}"

    return render_template("delete.html", id=id_)
