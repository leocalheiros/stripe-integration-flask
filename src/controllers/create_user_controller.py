from src.infra.db.repositories.users_repository import UsersRepositoryInterface
from flask import request, flash, redirect, url_for
import hashlib


class CreatePerson:
    def __init__(self, repo: UsersRepositoryInterface):
        self.__repo = repo

    def operate(self) -> any:
        email = request.form.get("email")
        password = request.form.get("password")
        if not self.__validate(email, password):
            flash("Existent user/invalid input", "error")
            return redirect(url_for('user_routes.create_user_page'))
        try:
            hashed_password = self.__hash_password(password)
            self.__repo.create_user(email=email, password=hashed_password)
            flash('Person created sucessfully', 'success')
            return redirect(url_for('stripe_routes.index'))
        except Exception as e:
            flash(str(e), 'error')
            return redirect(url_for('user_routes.create_user_page'))

    def __validate(self, email: str, password: str):
        if not email or not password:
            return False
        existing_user = self.__repo.get_user_by_email(email)
        if existing_user:
            return False
        return True

    def __hash_password(self, password: str) -> str:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password
