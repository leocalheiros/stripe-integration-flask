from flask import Blueprint, render_template, session, flash, redirect, url_for
from src.main.composer.create_user_composer import create_user_composer
from src.main.composer.login_composer import login_composer

user_routes_bp = Blueprint("user_routes", __name__)


@user_routes_bp.route('/create-user', methods=['GET'])
def create_user_page():
    return render_template('create-user.html')


@user_routes_bp.route("/create-user-proccess", methods=['POST'])
def create_user():
    create_user_controller = create_user_composer()
    return create_user_controller.operate()


@user_routes_bp.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')


@user_routes_bp.route('/login-process', methods=['POST'])
def login():
    login_controller = login_composer()
    return login_controller.operate()


@user_routes_bp.route('/logout', methods=['GET'])
def logout():
    if 'user_id' in session:
        session.clear()
        flash('Successfull logout', 'success')
        return redirect(url_for('stripe_routes.index'))
    flash('You are not logged in', 'error')
    return redirect(url_for('user_routes.login_page'))
