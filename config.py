import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'jashan-secret-key'

    # Azure Blob Storage
    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'cmsstoragejashan'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'fAAGRVqdsUeu1u10BXc+Eygt0vCjM87i1lIs3h6KaEDXcapz7aGD/mppAXpe9gs+0EokPBb+k1NT+AStPk0DBg=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    # Azure SQL Database
    SQL_SERVER = os.environ.get('SQL_SERVER') or 'cmsdatabase.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'cmsdatabase'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'azureuser'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Secure!123'

    SQLALCHEMY_DATABASE_URI = (
        'mssql+pyodbc://' + SQL_USER_NAME + ':' + SQL_PASSWORD +
        '@' + SQL_SERVER + ':1433/' + SQL_DATABASE +
        '?driver=ODBC+Driver+17+for+SQL+Server'
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Microsoft Login (MSAL)
    CLIENT_ID = "f610c541-0f30-4182-8e5f-ddf47b5e2c48"
    CLIENT_SECRET = "unV8Q~uba9ceFRtrQjLvv8XRIyjGvxKSIq_t9cze"

    AUTHORITY = "https://login.microsoftonline.com/common"

    REDIRECT_PATH = "/getAToken"

    SCOPE = ["User.Read"]

    SESSION_TYPE = "filesystem"
