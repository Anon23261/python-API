from app import create_app
from app.routes.auth import auth_bp

app = create_app()

# Register the auth blueprint
app.register_blueprint(auth_bp, url_prefix='/auth')

if __name__ == '__main__':
    app.run(debug=True)