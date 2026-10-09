from django.contrib.admin.apps import AdminConfig
from django.contrib.auth.apps import AuthConfig
from django.contrib.contenttypes.apps import ContentTypesConfig

OID = "django_mongodb_backend.fields.ObjectIdAutoField"

class MongoAdminConfig(AdminConfig):
    default_auto_field = OID

class MongoAuthConfig(AuthConfig):
    default_auto_field = OID

class MongoContentTypesConfig(ContentTypesConfig):
    default_auto_field = OID