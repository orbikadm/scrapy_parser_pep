from pathlib import Path


BASE_DIR = Path(__file__).parent.parent
BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

ROBOTSTXT_OBEY = True

FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 5,
}

TIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

SPIDER_NAME = 'pep'
SPIDER_PEP_URL = 'peps.python.org'

START_NAME = 'PEP '
MID_SEP = ' – '
END_NAME = '| peps.python.org'
