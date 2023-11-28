from src.infra.db.repositories.users_repository import UsersRepositoryInterface
from flask import request, flash, redirect, url_for, session
import hashlib


class LoginController:
    def __init__(self, repo: UsersRepositoryInterface):
        self.__repo = repo

    def operate(self) -> any:
        email = request.form.get("email")
        password = request.form.get("password")
        user_data = self.__repo.get_user_by_email(email)

        if user_data and self.__validate(password, user_data['password']):
            session['user_id'] = user_data['id']
            flash('Login successful', 'success')
            return redirect(url_for('stripe_routes.index'))
        else:
            flash('Invalid email or password', 'error')
            return redirect(url_for('user_routes.login_page'))

    def __validate(self, input_password: str, stored_password: str) -> bool:
        hashed_input_password = hashlib.sha256(input_password.encode()).hexdigest()
        return hashed_input_password == stored_password
