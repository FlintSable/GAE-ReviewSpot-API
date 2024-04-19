class Config:
    """Base configuration with default settings suitable for production."""
    DEBUG = False
    TESTING = False
    DATASTORE_DATASET = 'gae-reviewspot-api'
    DATASTORE_EMULATOR_HOST = None  # No emulator for production

class DevelopmentConfig(Config):
    """Development configuration uses the Datastore emulator."""
    DEBUG = True
    DATASTORE_EMULATOR_HOST = 'localhost:8081'
    DATASTORE_DATASET = 'dev-project'

class TestingConfig(Config):
    """Testing configuration, similar to development but potentially with different settings."""
    TESTING = True
    DATASTORE_EMULATOR_HOST = 'localhost:8081'
    DATASTORE_DATASET = 'test-project'