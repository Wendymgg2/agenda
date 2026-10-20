from app import crear_app
from app.routes import registrar_rutas
app, get_db = crear_app()
registrar_rutas(app, get_db)
if __name__ == '__main__':
    app.run(debug=True)