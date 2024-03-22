from pathlib import Path

# Route:
BASE_DIR = Path(__file__).parent.parent
LOG_DIR = BASE_DIR / 'logs'
LOG_FILE = LOG_DIR / 'main.log'

RESULTS_DIR = BASE_DIR / 'results'
DATA_DIR = BASE_DIR / 'data'

# Format logging:
LOG_FORMAT = '%(asctime)s - [%(levelname)s] - %(message)s'
DT_FORMAT = '%d.%m.%Y %H:%M:%S'
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

# Format date:
DATE_FORMAT_ONE = '%Y-%m-%d %H:%M'
DATE_FORMAT_TWO = '%Y-%m-%d %H:%M:%S'
DATE_FORMATS = (DATE_FORMAT_ONE, DATE_FORMAT_TWO)
