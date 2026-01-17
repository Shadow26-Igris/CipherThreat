from .auth_routes import auth_routes
from .main_routes import main_routes
from .complaint_routes import complaint_routes
from .scan_routes import scan_routes
from .vulnerability_scan_routes import vulnerability_scan_routes

# Export these blueprints for app initialization
__all__ = ['auth_routes', 'main_routes', 'complaint_routes' , 'scan_routes' , 'vulnerability_scan_routes']
