from flask import Blueprint, render_template , redirect , url_for

bp = Blueprint('auth', __name__ , url_prefix='/auth' , template_folder='templates')

@bp.route('/')
@bp.route('/login')
def login():
    return render_template('/auth/login.html')

@bp.route('/register')
def register():
    return render_template('/auth/register.html')

@bp.route('/forgot')
def forgot_password():
    return render_template('/auth/forgot.html')

@bp.route('/reset')
def reset_password():
    return render_template('/auth/reset.html')

@bp.route('/lock')
def lock():
    return render_template('/auth/lock.html')

@bp.route('/logout')
def logout():
    return render_template('/auth/logout.html')

@bp.route('/<path:path>')
def catch_all(path):
    return redirect(url_for('auth.login'))