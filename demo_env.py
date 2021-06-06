SECRET_KEY="Your key"
DATABASE_NAME="your db name"
DATABASE_USER="your db user"
DATABASE_PASS="your db pass"
DATABASE_HOST="your db host"
DATABASE_PORT="your db port"
DEBUG=True
ALLOWED_HOST=['*']
SESSION_COOKIE_SECURE=False
SECURE_SSL_REDIRECT=False
CSRF_COOKIE_SECURE=False
SECURE_BROWSER_XSS_FILTER=False

#smtp credentials if you don't want to use just remove these fields from django setting

EMAIL_HOST = 'your smtp host address'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'your username'
EMAIL_HOST_PASSWORD = 'your password'