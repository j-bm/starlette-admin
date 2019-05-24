from starlette.applications import Starlette
from starlette.staticfiles import StaticFiles
from starlette_admin.site import AdminSite
from starlette_core.database import Database
from starlette_core.middleware import DatabaseMiddleware

from .admin import DemoAdmin, DemoModelAdmin


db = Database('sqlite:///')
db.create_all()


# create admin site
adminsite = AdminSite(debug=True, name="admin")
# register admins
adminsite.register(DemoAdmin)
adminsite.register(DemoModelAdmin)

# create app
app = Starlette(debug=True)

app.mount(
    path="/static",
    app=StaticFiles(directory="static", packages=["starlette_admin"]),
    name="static"
)

app.add_middleware(DatabaseMiddleware)

# mount admin site
app.mount(path="/", app=adminsite, name=adminsite.name)
