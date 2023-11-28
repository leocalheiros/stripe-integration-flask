from flask import Blueprint, redirect, flash, request, url_for, render_template
from src.controllers.create_user_controller import CreatePerson
from src.main.composer.create_user_composer import create_user_composer

user_routes_bp = Blueprint("user_routes", __name__)


@user_routes_bp.route('/create-user', methods=['GET'])
def create_user_page():
    return render_template('create-user.html')


@user_routes_bp.route("/create-user-proccess", methods=['POST'])
def create_user():
    create_user_controller = create_user_composer()
    return create_user_controller.operate()
