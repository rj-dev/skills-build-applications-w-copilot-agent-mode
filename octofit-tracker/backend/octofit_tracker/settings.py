# Add 'tracker' to the INSTALLED_APPS list
INSTALLED_APPS = [
    # ...existing apps...
    'tracker',
]

# Configure the database engine to use djongo
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'octofit_db',
        'HOST': 'localhost',
        'PORT': 27017,
    }
}

# Enable CORS
INSTALLED_APPS += [
    'corsheaders',
]

# Add 'octofit_tracker' to the INSTALLED_APPS list
INSTALLED_APPS += [
    'octofit_tracker',
]

# Define MIDDLEWARE if not already defined
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Ensure CORS middleware is added
MIDDLEWARE.insert(0, 'corsheaders.middleware.CorsMiddleware')

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS',
]
CORS_ALLOW_HEADERS = [
    '*',
]

# Allow all hosts
ALLOWED_HOSTS = ['*']

# Add a valid SECRET_KEY
SECRET_KEY = 'your-secret-key-here'