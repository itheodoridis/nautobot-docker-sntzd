import os
import sys

from nautobot.core.settings import *  # noqa F401,F403
from nautobot.core.settings_funcs import is_truthy, parse_redis_connection

#########################
#                       #
#   Required settings   #
#                       #
#########################

# This is a list of valid fully-qualified domain names (FQDNs) for the Nautobot server. Nautobot will not permit write
# access to the server via any other hostnames. The first FQDN in the list will be treated as the preferred name.
#
# Example: ALLOWED_HOSTS = ['nautobot.example.com', 'nautobot.internal.local']
#
# ALLOWED_HOSTS = os.getenv("NAUTOBOT_ALLOWED_HOSTS", "").split(" ")

# The django-redis cache is used to establish concurrent locks using Redis.
#
# CACHES = {
#     "default": {
#         "BACKEND": os.getenv(
#             "NAUTOBOT_CACHES_BACKEND",
#             "django_prometheus.cache.backends.redis.RedisCache" if METRICS_ENABLED else "django_redis.cache.RedisCache",
#         ),
#         "LOCATION": parse_redis_connection(redis_database=1),
#         "TIMEOUT": 300,
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#             "PASSWORD": "",
#         },
#     }
# }

# Number of seconds to cache ContentType lookups. Set to 0 to disable caching.
# CONTENT_TYPE_CACHE_TIMEOUT = int(os.getenv("NAUTOBOT_CONTENT_TYPE_CACHE_TIMEOUT", "0"))

# Celery Beat heartbeat file path - will be touched by Beat each time it wakes up as a proof-of-health.
# CELERY_BEAT_HEARTBEAT_FILE = os.getenv(
#     "NAUTOBOT_CELERY_BEAT_HEARTBEAT_FILE",
#     os.path.join(tempfile.gettempdir(), "nautobot_celery_beat_heartbeat"),
# )

# Celery broker URL used to tell workers where queues are located
#
# CELERY_BROKER_URL = os.getenv("NAUTOBOT_CELERY_BROKER_URL", parse_redis_connection(redis_database=0))

# Database configuration. See the Django documentation for a complete list of available parameters:
#   https://docs.djangoproject.com/en/stable/ref/settings/#databases
#
# DATABASES = {
#     "default": {
#         "NAME": os.getenv("NAUTOBOT_DB_NAME", "nautobot"),  # Database name
#         "USER": os.getenv("NAUTOBOT_DB_USER", ""),  # Database username
#         "PASSWORD": os.getenv("NAUTOBOT_DB_PASSWORD", ""),  # Database password
#         "HOST": os.getenv("NAUTOBOT_DB_HOST", "localhost"),  # Database server
#         "PORT": os.getenv("NAUTOBOT_DB_PORT", ""),  # Database port (leave blank for default)
#         "CONN_MAX_AGE": int(os.getenv("NAUTOBOT_DB_TIMEOUT", "300")),  # Database timeout
#         "ENGINE": os.getenv(
#             "NAUTOBOT_DB_ENGINE",
#             "django_prometheus.db.backends.postgresql" if METRICS_ENABLED else "django.db.backends.postgresql",
#         ),  # Database driver ("mysql" or "postgresql")
#     }
# }

# Ensure proper Unicode handling for MySQL
#
if DATABASES["default"]["ENGINE"].endswith("mysql"):
    DATABASES["default"]["OPTIONS"] = {"charset": "utf8mb4"}

# This key is used for secure generation of random numbers and strings. It must never be exposed outside of this file.
# For optimal security, SECRET_KEY should be at least 50 characters in length and contain a mix of letters, numbers, and
# symbols. Nautobot will not run without this defined. For more information, see
# https://docs.djangoproject.com/en/stable/ref/settings/#std:setting-SECRET_KEY
SECRET_KEY = os.getenv("NAUTOBOT_SECRET_KEY", "lalalalalasecretkey") #again use your own

#####################################
#                                   #
#   Optional Django core settings   #
#                                   #
#####################################

# Specify one or more name and email address tuples representing Nautobot administrators.
# These people will be notified of application errors (assuming correct email settings are provided).
#
# ADMINS = [
#     ['John Doe', 'jdoe@example.com'],
# ]

# FQDNs that are considered trusted origins for secure, cross-domain, requests such as HTTPS POST.
# If running Nautobot under a single domain, you may not need to set this variable;
# if running on multiple domains, you *may* need to set this variable to more or less the same as ALLOWED_HOSTS above.
# https://docs.djangoproject.com/en/stable/ref/settings/#csrf-trusted-origins
#
# CSRF_TRUSTED_ORIGINS = []

# Date/time formatting. See the following link for supported formats:
# https://docs.djangoproject.com/en/stable/ref/templates/builtins/#date
#
# DATE_FORMAT = os.getenv("NAUTOBOT_DATE_FORMAT", "N j, Y")
# SHORT_DATE_FORMAT = os.getenv("NAUTOBOT_SHORT_DATE_FORMAT", "Y-m-d")
# TIME_FORMAT = os.getenv("NAUTOBOT_TIME_FORMAT", "g:i a")
# SHORT_TIME_FORMAT = os.getenv("NAUTOBOT_SHORT_TIME_FORMAT", "H:i:s")
# DATETIME_FORMAT = os.getenv("NAUTOBOT_DATETIME_FORMAT", "N j, Y g:i a")
# SHORT_DATETIME_FORMAT = os.getenv("NAUTOBOT_SHORT_DATETIME_FORMAT", "Y-m-d H:i")

# Set to True to enable server debugging. WARNING: Debugging introduces a substantial performance penalty and may reveal
# sensitive information about your installation. Only enable debugging while performing testing. Never enable debugging
# on a production system.
#
# DEBUG = is_truthy(os.getenv("NAUTOBOT_DEBUG", "False"))

# If hosting Nautobot in a subdirectory, you must set this value to match the base URL prefix configured in your
# HTTP server (e.g. `/nautobot/`). When not set, URLs will default to being prefixed by `/`.
#
# FORCE_SCRIPT_NAME = None

# IP addresses recognized as internal to the system.
#
# INTERNAL_IPS = ("127.0.0.1", "::1")

# Enable custom logging. Please see the Django documentation for detailed guidance on configuring custom logs:
#   https://docs.djangoproject.com/en/stable/topics/logging/
#
# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "formatters": {
#         "normal": {
#             "format": "%(asctime)s.%(msecs)03d %(levelname)-7s %(name)s :\n  %(message)s",
#             "datefmt": "%H:%M:%S",
#         },
#         "verbose": {
#             "format": "%(asctime)s.%(msecs)03d %(levelname)-7s %(name)-20s %(filename)-15s %(funcName)30s() :\n  %(message)s",
#             "datefmt": "%H:%M:%S",
#         },
#     },
#     "handlers": {
#         "normal_console": {
#             "level": "INFO",
#             "class": "logging.StreamHandler",
#             "formatter": "normal",
#         },
#         "verbose_console": {
#             "level": "DEBUG",
#             "class": "logging.StreamHandler",
#             "formatter": "verbose",
#         },
#     },
#     "loggers": {
#         "django": {"handlers": ["normal_console"], "level": "INFO"},
#         "nautobot": {
#             "handlers": ["verbose_console" if DEBUG else "normal_console"],
#             "level": "DEBUG" if DEBUG else "INFO",
#         },
#     },
# }

# The file path where uploaded media such as image attachments are stored. A trailing slash is not needed.
#
# MEDIA_ROOT = os.path.join(NAUTOBOT_ROOT, "media").rstrip("/")

# Set to True to use session cookies instead of persistent cookies.
# Session cookies will expire when a browser is closed.
#
# SESSION_EXPIRE_AT_BROWSER_CLOSE = is_truthy(os.getenv("NAUTOBOT_SESSION_EXPIRE_AT_BROWSER_CLOSE", "False"))

# The length of time (in seconds) for which a user will remain logged into the web UI before being prompted to
# re-authenticate. (Default: 1209600 [14 days])
#
# SESSION_COOKIE_AGE = int(os.getenv("NAUTOBOT_SESSION_COOKIE_AGE", "1209600"))  # 2 weeks, in seconds

# Where Nautobot stores user session data.
#
# SESSION_ENGINE = "django.contrib.sessions.backends.db"

# By default, Nautobot will store session data in the database. Alternatively, a file path can be specified here to use
# local file storage instead. (This can be useful for enabling authentication on a standby instance with read-only
# database access.) Note that the user as which Nautobot runs must have read and write permissions to this path.
#
# SESSION_FILE_PATH = os.getenv("NAUTOBOT_SESSION_FILE_PATH", None)

# Where static files (CSS, JavaScript, etc.) are stored
#
# STATIC_ROOT = os.path.join(NAUTOBOT_ROOT, "static")

# Time zone (default: UTC)
#
# TIME_ZONE = os.getenv("NAUTOBOT_TIME_ZONE", "UTC")

###################################################################
#                                                                 #
#   Optional settings specific to Nautobot and its related apps   #
#                                                                 #
###################################################################

# URL schemes that are allowed within links in Nautobot
#
# ALLOWED_URL_SCHEMES = (
#     "file",
#     "ftp",
#     "ftps",
#     "http",
#     "https",
#     "irc",
#     "mailto",
#     "sftp",
#     "ssh",
#     "tel",
#     "telnet",
#     "tftp",
#     "vnc",
#     "xmpp",
# )

# Banners (HTML is permitted) to display at the top and/or bottom of all Nautobot pages, and on the login page itself.
#
# BANNER_BOTTOM = ""
# BANNER_LOGIN = ""
# BANNER_TOP = ""

# Branding logo locations. The logo takes the place of the Nautobot logo in the top right of the nav bar.
# The filepath should be relative to the `MEDIA_ROOT`.
#
# BRANDING_FILEPATHS = {
#     "logo": os.getenv("NAUTOBOT_BRANDING_FILEPATHS_LOGO", None),  # Navbar logo
#     "favicon": os.getenv("NAUTOBOT_BRANDING_FILEPATHS_FAVICON", None),  # Browser favicon
#     "icon_16": os.getenv("NAUTOBOT_BRANDING_FILEPATHS_ICON_16", None),  # 16x16px icon
#     "icon_32": os.getenv("NAUTOBOT_BRANDING_FILEPATHS_ICON_32", None),  # 32x32px icon
#     "icon_180": os.getenv(
#         "NAUTOBOT_BRANDING_FILEPATHS_ICON_180", None
#     ),  # 180x180px icon - used for the apple-touch-icon header
#     "icon_192": os.getenv("NAUTOBOT_BRANDING_FILEPATHS_ICON_192", None),  # 192x192px icon
#     "icon_mask": os.getenv(
#         "NAUTOBOT_BRANDING_FILEPATHS_ICON_MASK", None
#     ),  # mono-chrome icon used for the mask-icon header
#     "header_bullet": os.getenv(
#         "NAUTOBOT_BRANDING_FILEPATHS_HEADER_BULLET", None
#     ),  # bullet image used for various view headers
#     "nav_bullet": os.getenv("NAUTOBOT_BRANDING_FILEPATHS_NAV_BULLET", None),  # bullet image used for nav menu headers
# }

# Prepended to CSV, YAML and export template filenames (i.e. `nautobot_device.yml`)
#
# BRANDING_PREPENDED_FILENAME = os.getenv("NAUTOBOT_BRANDING_PREPENDED_FILENAME", "nautobot_")

# Title to use in place of "Nautobot"
#
# BRANDING_TITLE = os.getenv("NAUTOBOT_BRANDING_TITLE", "Nautobot")

# Branding URLs (links in the bottom right of the footer)
#
# BRANDING_URLS = {
#     "code": os.getenv("NAUTOBOT_BRANDING_URLS_CODE", "https://github.com/nautobot/nautobot"),
#     "docs": os.getenv("NAUTOBOT_BRANDING_URLS_DOCS", None),
#     "help": os.getenv("NAUTOBOT_BRANDING_URLS_HELP", "https://github.com/nautobot/nautobot/wiki"),
# }

# Options to pass to the Celery broker transport, for example when using Celery with Redis Sentinel.
#
# CELERY_BROKER_TRANSPORT_OPTIONS = {}

# Default celery queue name that will be used by workers and tasks if no queue is specified
# CELERY_TASK_DEFAULT_QUEUE = os.getenv("NAUTOBOT_CELERY_TASK_DEFAULT_QUEUE", "default")

# Global task time limits (seconds)
# Exceeding the soft limit will result in a SoftTimeLimitExceeded exception,
# while exceeding the hard limit will result in a SIGKILL.
#
# CELERY_TASK_SOFT_TIME_LIMIT = int(os.getenv("NAUTOBOT_CELERY_TASK_SOFT_TIME_LIMIT", str(5 * 60)))
# CELERY_TASK_TIME_LIMIT = int(os.getenv("NAUTOBOT_CELERY_TASK_TIME_LIMIT", str(10 * 60)))

# Ports for prometheus metric HTTP server running on the celery worker.
# Normally this should be set to a single port, unless you have multiple workers running on a single machine, i.e.
# sharing the same available ports. In that case you need to specify a range of ports greater than or equal to the
# highest amount of workers you are running on a single machine (comma-separated, like "8080,8081,8082"). You can then
# use the `target_limit` parameter to the Prometheus `scrape_config` to ensure you are not getting duplicate metrics in
# that case. Set this to an empty string to disable it.
# CELERY_WORKER_PROMETHEUS_PORTS = []
# if os.getenv("NAUTOBOT_CELERY_WORKER_PROMETHEUS_PORTS"):
#     CELERY_WORKER_PROMETHEUS_PORTS = [
#         int(value) for value in os.getenv("NAUTOBOT_CELERY_WORKER_PROMETHEUS_PORTS").split(",")
#     ]


# Number of days to retain changelog entries. Set to 0 to retain changes indefinitely.
#
# CHANGELOG_RETENTION = 90

# If True, all origins will be allowed. Other settings restricting allowed origins will be ignored.
# Defaults to False. Setting this to True can be dangerous, as it allows any website to make
# cross-origin requests to yours. Generally you'll want to restrict the list of allowed origins with
# CORS_ALLOWED_ORIGINS or CORS_ALLOWED_ORIGIN_REGEXES.
#
# CORS_ALLOW_ALL_ORIGINS = is_truthy(os.getenv("NAUTOBOT_CORS_ALLOW_ALL_ORIGINS", "False"))

# A list of origins that are authorized to make cross-site HTTP requests. Defaults to [].
#
# CORS_ALLOWED_ORIGINS = [
#     'https://hostname.example.com',
# ]

# A list of strings representing regexes that match Origins that are authorized to make cross-site
# HTTP requests. Defaults to [].
#
# CORS_ALLOWED_ORIGIN_REGEXES = [
#     r'^(https?://)?(\w+\.)?example\.com$',
# ]

# Device names are not guaranteed globally-unique by Nautobot but in practice they often are.
# Set this to True to use the device name alone as the natural key for Device objects.
# Set this to False to use the sequence (name, tenant, location) as the natural key instead.
#
# DEVICE_NAME_AS_NATURAL_KEY = False

# Set to True to disable rendering of the IP prefix hierarchy in the the IPAM prefix list view.
# Useful in case of poor performance when rendering this page.
#
# DISABLE_PREFIX_LIST_HIERARCHY = False

# Exempt certain models from the enforcement of view permissions. Models listed here will be viewable by all users and
# by anonymous users. List models in the form `<app>.<model>`. Add '*' to this list to exempt all models.
# Defaults to [].
#
# EXEMPT_VIEW_PERMISSIONS = [
#     'dcim.location',
#     'ipam.prefix',
# ]

# Global 3rd-party authentication settings
#
# EXTERNAL_AUTH_DEFAULT_GROUPS = []
# EXTERNAL_AUTH_DEFAULT_PERMISSIONS = {}

# Directory where cloned Git repositories will be stored.
#
# GIT_ROOT = os.getenv("NAUTOBOT_GIT_ROOT", os.path.join(NAUTOBOT_ROOT, "git").rstrip("/"))

# Prefixes to use for custom fields, relationships, and computed fields in GraphQL representation of data.
#
# GRAPHQL_COMPUTED_FIELD_PREFIX = "cpf"
# GRAPHQL_CUSTOM_FIELD_PREFIX = "cf"
# GRAPHQL_RELATIONSHIP_PREFIX = "rel"

# HTTP proxies Nautobot should use when sending outbound HTTP requests (e.g. for webhooks).
#
# HTTP_PROXIES = {
#     'http': 'http://10.10.1.10:3128',
#     'https': 'http://10.10.1.10:1080',
# }

# Send anonymized installation metrics when `nautobot-server post_upgrade` command is run.
#
INSTALLATION_METRICS_ENABLED = is_truthy(os.getenv("NAUTOBOT_INSTALLATION_METRICS_ENABLED", "False"))

# Storage backend to use for Job input files and Job output files.
#
# Note: the default is for backwards compatibility and it is recommended to change it if possible for your deployment.
#
# JOB_FILE_IO_STORAGE = os.getenv("NAUTOBOT_JOB_FILE_IO_STORAGE", "db_file_storage.storage.DatabaseFileStorage")

# Maximum size in bytes of any single file created by Job.create_file().
#
# JOB_CREATE_FILE_MAX_SIZE = 10 << 20

# Directory where Jobs can be discovered.
#
# JOBS_ROOT = os.getenv("NAUTOBOT_JOBS_ROOT", os.path.join(NAUTOBOT_ROOT, "jobs").rstrip("/"))

# Location names are not guaranteed globally-unique by Nautobot but in practice they often are.
# Set this to True to use the location name alone as the natural key for Location objects.
# Set this to False to use the sequence (name, parent__name, parent__parent__name, ...) as the natural key instead.
#
# LOCATION_NAME_AS_NATURAL_KEY = False

# Log Nautobot deprecation warnings. Note that this setting is ignored (deprecation logs always enabled) if DEBUG = True
#
# LOG_DEPRECATION_WARNINGS = is_truthy(os.getenv("NAUTOBOT_LOG_DEPRECATION_WARNINGS", "False"))

# Setting this to True will display a "maintenance mode" banner at the top of every page.
#
# MAINTENANCE_MODE = is_truthy(os.getenv("NAUTOBOT_MAINTENANCE_MODE", "False"))

# Maximum number of objects that the UI and API will retrieve in a single request.
#
# MAX_PAGE_SIZE = 1000

# Expose Prometheus monitoring metrics at the HTTP endpoint '/metrics'
#
# METRICS_ENABLED = is_truthy(os.getenv("NAUTOBOT_METRICS_ENABLED", "False"))

# Require API Authentication to HTTP endpoint '/metrics'
#
# METRICS_AUTHENTICATED = is_truthy(os.getenv("NAUTOBOT_METRICS_AUTHENTICATED", "False"))

# Credentials that Nautobot will uses to authenticate to devices when connecting via NAPALM.
#
# NAPALM_USERNAME = os.getenv("NAUTOBOT_NAPALM_USERNAME", "")
# NAPALM_PASSWORD = os.getenv("NAUTOBOT_NAPALM_PASSWORD", "")

NAPALM_SECRET = os.getenv("NAUTOBOT_NAPALM_SECRET", "")
DEVICE_SECRET = os.getenv("NAUTOBOT_DEVICE_SECRET", "")
# NAPALM timeout (in seconds). (Default: 30)
#
# NAPALM_TIMEOUT = int(os.getenv("NAUTOBOT_NAPALM_TIMEOUT", "30"))

# NAPALM optional arguments (see https://napalm.readthedocs.io/en/latest/support/#optional-arguments). Arguments must
# be provided as a dictionary.
NAPALM_ARGS = {
    "secret" : DEVICE_SECRET,
}

# Default number of objects to display per page of the UI and REST API.
#
# PAGINATE_COUNT = 50

# Options given in the web UI for the number of objects to display per page.
#
# PER_PAGE_DEFAULTS = [25, 50, 100, 250, 500, 1000]

# Enable installed plugins. Add the name of each plugin to the list.
#
PLUGINS = [
    "nautobot_device_onboarding",
    "nautobot_device_lifecycle_mgmt",
    "nautobot_bgp_models",
    "nautobot_plugin_nornir",
    "nautobot_golden_config",
    "nautobot_floor_plan"
]

# Plugins configuration settings. These settings are used by various plugins that the user may have installed.
# Each key in the dictionary is the name of an installed plugin and its value is a dictionary of settings.
#
# PLUGINS_CONFIG = {
#     'my_plugin': {
#         'foo': 'bar',
#         'buzz': 'bazz'
#     }
# }

PLUGINS_CONFIG = {
    "nautobot_device_lifecycle_mgmt": {
        "barchart_bar_width": float(os.environ.get("BARCHART_BAR_WIDTH", 0.1)),
        "barchart_width": int(os.environ.get("BARCHART_WIDTH", 12)),
        "barchart_height": int(os.environ.get("BARCHART_HEIGHT", 5)),
    },
    "nautobot_bgp_models": {
        "default_statuses": {
            "AutonomousSystem": ["active", "available", "planned"],
            "Peering": ["active", "decommissioned", "deprovisioning", "offline", "planned", "provisioning"],
        }
    },
    "nautobot_plugin_nornir": {
        "use_config_context": {"secrets": False, "connection_options": True},
        # Optionally set global connection options.
        "connection_options": {
            "napalm": {
                "extras": {
                    "optional_args": {"global_delay_factor": 1},
                },
            },
            "netmiko": {
                "extras": {
                    "global_delay_factor": 1,
                },
            },
        },
        "nornir_settings": {
            "credentials": "nautobot_plugin_nornir.plugins.credentials.env_vars.CredentialsEnvVars",
            "runner": {
                "plugin": "threaded",
                "options": {
                    "num_workers": 20,
                },
            },
        },
    },
    "nautobot_golden_config": {
        "per_feature_bar_width": 0.15,
        "per_feature_width": 13,
        "per_feature_height": 4,
        "enable_backup": True,
        "enable_compliance": True,
        "enable_intended": True,
        "enable_sotagg": True,
        "sot_agg_transposer": None,
        "platform_slug_map": None,
        # "get_custom_compliance": "my.custom_compliance.func"
    },
}
# Prefer IPv6 addresses or IPv4 addresses in selecting a device's primary IP address?
#
# PREFER_IPV4 = False

# Default height and width in pixels of a single rack unit in rendered rack elevations.
#
# RACK_ELEVATION_DEFAULT_UNIT_HEIGHT = 22
# RACK_ELEVATION_DEFAULT_UNIT_WIDTH = 220

# Sets an age out timer of redis lock. This is NOT implicitly applied to locks, must be added
# to a lock creation as `timeout=settings.REDIS_LOCK_TIMEOUT`
#
# REDIS_LOCK_TIMEOUT = int(os.getenv("NAUTOBOT_REDIS_LOCK_TIMEOUT", "600"))

# How frequently to check for a new Nautobot release on GitHub, and the URL to check for this information.
#
# RELEASE_CHECK_TIMEOUT = 24 * 3600
# RELEASE_CHECK_URL = None

# Remote auth backend settings
#
# REMOTE_AUTH_AUTO_CREATE_USER = False
# REMOTE_AUTH_HEADER = "HTTP_REMOTE_USER"

# Job log entry sanitization and similar
#
# SANITIZER_PATTERNS = [
#     # General removal of username-like and password-like tokens
#     (re.compile(r"(https?://)?\S+\s*@", re.IGNORECASE), r"\1{replacement}@"),
#     (
#         re.compile(r"(username|password|passwd|pwd|secret|secrets)([\"']?(?:\s+is.?|:)?\s+)\S+[\"']?", re.IGNORECASE),
#         r"\1\2{replacement}",
#     ),
# ]

# Configure SSO, for more information see docs/configuration/authentication/sso.md
#
# SOCIAL_AUTH_POSTGRES_JSONFIELD = False

# By default uploaded media is stored on the local filesystem. Using Django-storages is also supported. Provide the
# class path of the storage driver in STORAGE_BACKEND and any configuration options in STORAGE_CONFIG.
# These default to None and {} respectively.
#
# STORAGE_BACKEND = 'storages.backends.s3boto3.S3Boto3Storage'
# STORAGE_CONFIG = {
#     'AWS_ACCESS_KEY_ID': 'Key ID',
#     'AWS_SECRET_ACCESS_KEY': 'Secret',
#     'AWS_STORAGE_BUCKET_NAME': 'nautobot',
#     'AWS_S3_REGION_NAME': 'eu-west-1',
# }

# Reject invalid UI/API filter parameters, or discard them while logging a warning?
#
# STRICT_FILTERING = is_truthy(os.getenv("NAUTOBOT_STRICT_FILTERING", "True"))

# Custom message to display on 4xx and 5xx error pages. Markdown is supported.
#
# SUPPORT_MESSAGE = (
#     "If further assistance is required, please join the `#nautobot` channel "
#     "on [Network to Code's Slack community](https://slack.networktocode.com) and post your question."
# )

# UI_RACK_VIEW_TRUNCATE_FUNCTION
#
# def UI_RACK_VIEW_TRUNCATE_FUNCTION(device_display_name):
#     """Given device display name, truncate to fit the rack elevation view.
#
#     :param device_display_name: Full display name of the device attempting to be rendered in the rack elevation.
#     :type device_display_name: str
#
#     :return: Truncated device name
#     :type: str
#     """
#     return str(device_display_name).split(".")[0]

# Time zone (default: UTC)
TIME_ZONE = os.getenv("NAUTOBOT_TIME_ZONE", "Europe/Athens")

# Date/time formatting. See the following link for supported formats:
# https://docs.djangoproject.com/en/stable/ref/templates/builtins/#date
DATE_FORMAT = os.getenv("NAUTOBOT_DATE_FORMAT", "N j, Y")
SHORT_DATE_FORMAT = os.getenv("NAUTOBOT_SHORT_DATE_FORMAT", "Y-m-d")
TIME_FORMAT = os.getenv("NAUTOBOT_TIME_FORMAT", "g:i a")
SHORT_TIME_FORMAT = os.getenv("NAUTOBOT_SHORT_TIME_FORMAT", "H:i:s")
DATETIME_FORMAT = os.getenv("NAUTOBOT_DATETIME_FORMAT", "N j, Y g:i a")
SHORT_DATETIME_FORMAT = os.getenv("NAUTOBOT_SHORT_DATETIME_FORMAT", "Y-m-d H:i")

# A list of strings designating all applications that are enabled in this Django installation.
# Each string should be a dotted Python path to an application configuration class (preferred),
# or a package containing an application.
# https://docs.nautobot.com/projects/core/en/latest/configuration/optional-settings/#extra-applications
# EXTRA_INSTALLED_APPS = []

# Allow users to enable request profiling on their login session
# ALLOW_REQUEST_PROFILING = False
LOG_LEVEL = "DEBUG" if DEBUG else "INFO"
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "normal": {
            "format": "%(asctime)s.%(msecs)03d %(levelname)-7s %(name)s :\n  %(message)s",
            "datefmt": "%H:%M:%S",
        },
        "verbose": {
            "format": "%(asctime)s.%(msecs)03d %(levelname)-7s %(name)-20s %(filename)-15s %(funcName)30s() :\n  %(message)s",
            "datefmt": "%H:%M:%S",
        },
    },
    "handlers": {
        "normal_console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "normal",
        },
    },
    "loggers": {
        "django": {"handlers": ["normal_console"], "level": LOG_LEVEL},
        "nautobot": {
            "handlers": ["normal_console"],
            "level": LOG_LEVEL,
        },
    },
}

AUTHENTICATION_BACKENDS = [
    'django_auth_ldap.backend.LDAPBackend',
    'nautobot.core.authentication.ObjectPermissionBackend',
]

import ldap


# Server URI
AUTH_LDAP_SERVER_URI = "ldaps://yourmsadserver:636"

# The following may be needed if you are binding to Active Directory.
AUTH_LDAP_CONNECTION_OPTIONS = {
    ldap.OPT_REFERRALS: 0
}

# Set the DN and password for the Nautobot service account.
AUTH_LDAP_BIND_DN = "CN=yourldapuser,OU=bla1,OU=bla2,DC=domainname,DC=com"
AUTH_LDAP_BIND_PASSWORD = "yourldapbindpassword"

# Include this setting if you want to ignore certificate errors. This might be needed to accept a self-signed cert.
# Note that this is a Nautobot-specific setting which sets:
#     ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_NEVER)
#LDAP_IGNORE_CERT_ERRORS = True
ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_NEVER)

#AUTH_LDAP_START_TLS = False

from django_auth_ldap.config import LDAPSearch

# This search matches users with the sAMAccountName equal to the provided username. This is required if the user's
# username is not in their DN (Active Directory).
AUTH_LDAP_USER_SEARCH = LDAPSearch("OU=userou,OU=bla3,DC=domainname,dc=com",
                                    ldap.SCOPE_SUBTREE,
                                    "(sAMAccountName=%(user)s)")

# If a user's DN is producible from their username, we don't need to search.
AUTH_LDAP_USER_DN_TEMPLATE = None

# You can map user attributes to Django attributes as so.
AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail"
}

from django_auth_ldap.config import LDAPSearch, NestedGroupOfNamesType

# This search ought to return all groups to which the user belongs. django_auth_ldap uses this to determine group
# hierarchy.
AUTH_LDAP_GROUP_SEARCH = LDAPSearch("dc=domainname,dc=com", ldap.SCOPE_SUBTREE,
                                    "(objectClass=group)")
AUTH_LDAP_GROUP_TYPE = NestedGroupOfNamesType()

# Define a group required to login.
AUTH_LDAP_REQUIRE_GROUP = "CN=requiredusergroup,OU=Groups,OU=bla5,DC=domainname,DC=com"

#AUTH_LDAP_MIRROR_GROUPS = True
AUTH_LDAP_MIRROR_GROUPS = ["group1","group2","group3"] #which groups to mirror, so as not to mirror all groups

# Define special user types using groups. Exercise great caution when assigning superuser status.
AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    "is_active": "CN=requiredusergroup,OU=Groups,OU=bla5,DC=domainname,DC=com",
    "is_staff": "CN=somegroup,OU=Groups,OU=bla5,DC=domainname,DC=com",
    "is_superuser": "CN=admingroup,OU=Groups,OU=bla5,DC=domainname,DC=com"
}

# For more granular permissions, we can map LDAP groups to Django groups.
AUTH_LDAP_FIND_GROUP_PERMS = True

# Cache groups for one hour to reduce LDAP traffic
AUTH_LDAP_CACHE_GROUPS = True
AUTH_LDAP_CACHE_TIMEOUT = 3600
