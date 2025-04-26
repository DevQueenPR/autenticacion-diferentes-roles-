from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_principal import Principal, Permission, RoleNeed, Identity, identity_loaded, identity_changed, AnonymousIdentity
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'clave_secreta'

#  Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Flask-Principal
principals = Principal(app)

# Permisos
admin_permission = Permission(RoleNeed('admin'))
user_permission = Permission(RoleNeed('user'))

#usuarios y admins
users = {
    "admin": {"id": 1, "username": "admin", "password": generate_password_hash("adminpass"), "role": "admin"},
    "juan": {"id": 2, "username": "juan", "password": generate_password_hash("juan123"), "role": "user"},
    "maria": {"id": 3, "username": "maria", "password": generate_password_hash("maria123"), "role": "user"}
}

# Modelo de usuario
class User(UserMixin):
    def __init__(self, id, username, role):
        self.id = id
        self.username = username
        self.role = role

@login_manager.user_loader
def load_user(user_id):
    for user_info in users.values():
        if str(user_info["id"]) == user_id:
            return User(user_info["id"], user_info["username"], user_info["role"])
    return None

# rol actual
@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    if hasattr(current_user, 'role'):
        identity.provides.add(RoleNeed(current_user.role))


# Rutas
# Home (index)
@app.route('/')
def home():
    return render_template('home.html')

# Ruta Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_info = users.get(username)

        if user_info and check_password_hash(user_info['password'], password):
            user = User(user_info["id"], username, user_info["role"])
            login_user(user)
            identity_changed.send(app, identity=Identity(user.id))
            flash('Inicio de sesión exitoso.', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Credenciales inválidas. Intenta nuevamente.', 'danger')
            return redirect(url_for('login'))
    
    return render_template('login.html')

# Ruta Dashboard 
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', username=current_user.username, role=current_user.role, users=users)

# Logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    identity_changed.send(app, identity=AnonymousIdentity())
    flash('Sesión cerrada.', 'info')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
