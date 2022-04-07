# from flask import url_for
# import msal
from importlib_metadata import functools
from msal import ConfidentialClientApplication, SerializableTokenCache
import app_config

class CellPhoneMSALApp:

    def _build_msal_app(self):
        return ConfidentialClientApplication(
            app_config.CLIENT_ID,
            authority=app_config.AUTHORITY,
            client_credential=app_config.CLIENT_SECRET
        )

    def _load_cache(self):
        cache = SerializableTokenCache()
        if self.session.get("token_cache"):
            cache.deserialize(self.session["token_cache"])
        return cache

    def _save_cache(self, cache):
        if cache.has_state_changed:
            self.session["token_cache"] = cache.serialize()

    def get_msal_token(self):
        app = self._build_msal_app()
        if app:
            result = app.acquire_token_for_client(scopes=app_config.SCOPES)
            if result.get("access_token"):
                return result["access_token"]


#custom decorator
def auth_required(func):
    @functools.wraps(func)
    def is_authenticated(*args, **kwargs):
        try:
            # session = kwargs['session']
            msalapp = CellPhoneMSALApp()
            token = msalapp.get_msal_token()
            if token:
                return func(*args, **kwargs)
            else:
                return {"messagem": "Acesso negado"}, 401

        except RuntimeError as e:
            return {"message": "Error {}".format(e)}
    return is_authenticated
