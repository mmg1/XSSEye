from .admin import urls as admin_urls
from .admin.api import urls as admin_api_urls
from .api import urls as public_api
from .payload import urls as generator_urls
from .payload.generator import Generator
from .reports import urls as report_urls
from .static import Static
from .users import login
from .utils.blueprint_wrapper import attach
from .utils.http_auth import HTTPBasicAuth


def on_init():
    Static.auth.verify_password(login.verify_password)


def register_blueprint(app):
    app.register_blueprint(attach(admin_urls.routes, Static.auth.login_required), url_prefix='/admin')
    app.register_blueprint(attach(admin_api_urls.routes, Static.auth.login_required), url_prefix='/admin/api')
    app.register_blueprint(public_api.routes, url_prefix='/api')
    app.register_blueprint(generator_urls.routes, url_prefix='/')
    app.register_blueprint(report_urls.routes, url_prefix='/')
