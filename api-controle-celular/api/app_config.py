# Configurações do SQLAlchemy
SQLALCHEMY_DATABASE_URI = "sqlite:///cellphone.db"
SQLALCHEMY_TRACK_MODIFICATIONS = False
PROPAGATE_EXCEPTIONS = True

# Autenticação do APP no Azure AD B2C
CLIENT_ID = "42f4eb4b-f48d-4bdf-af99-c3994605a805"
# CLIENT_SECRET = "aded315b-e3a5-4cb0-9370-4b4a78d77a7c"
# CLIENT_SECRET = "3D77Q~FD1v~Ryk-IHBOwINMychrgdtZNkblA~"
CLIENT_SECRET = "qualquercoisa"

AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app

# Used for forming an absolute URL to your redirect URI.
# The absolute URL must match the redirect URI you set
# in the app's registration in the Azure portal.
REDIRECT_PATH = "/getAToken"

# You can find more Microsoft Graph API endpoints from Graph Explorer
# https://developer.microsoft.com/en-us/graph/graph-explorer
ENDPOINT = 'https://graph.microsoft.com/v1.0/users'  # This resource requires no admin consent

# You can find the proper permission names from this document
# https://docs.microsoft.com/en-us/graph/permissions-reference
# SCOPES = ["User.ReadBasic.All"]
SCOPES = ["https://graph.microsoft.com/.default"]

SESSION_TYPE = "filesystem"  # Specifies the token cache should be stored in server-side session

# Configurations for upload bulk CSV files
UPLOAD_FOLDER = 'static/files'

# Configurarions for upload Termo de Responsabilidades
UPLOAD_DOCS = 'static/documents'
IMG_LOCATION = 'static/images'