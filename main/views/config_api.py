from . import bp
from flask import current_app

@bp.post("/config/")
def set_config():
    api_admin_key = request.args.get('key',None,type=str)
    if api_admin_key == current_app.config["api_admin_key"]:
        req = request.get_json()
        updateConfig(req)    
    return make_response(current_app.config)
    
@bp.get("/config/")
def get_config():
    api_admin_key = request.args.get('key',None,type=str)
    if api_admin_key == current_app.config["api_admin_key"]:
        return make_response(current_app.config)
    else:
        abort(404)
