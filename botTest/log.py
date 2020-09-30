import logging



LOGGING = {
    'dusable_existing_loggers': True,
    'version': 1,
    'formatters': {
                'verbose': {
                    'format': '%(levelname)s %(module)s.%(funcNume)s | %(asctime)s | %(message)s',
                    'datefmt': '%Y-%m-%d %H:%M:%S',
                    },
            },
    'handlers': {
        'console': {
            'claaa': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'verbose',
            },
        },
    'loggers': {
        '':{
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
          },
        
        },

}
logging.config.dictConfig(LOGGING)

# logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
# logging.warning('This will get logged to a file')