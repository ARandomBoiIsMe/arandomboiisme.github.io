AUTHOR = 'Abah Olotuche Gabriel'
SITENAME = "arandomboiisme.github.io"
SITEURL = ""

PATH = "content"

TIMEZONE = 'Africa/Lagos'

DEFAULT_LANG = 'en'

DRAFT_SAVE_AS='{category}/drafts/{slug}.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

LOAD_CONTENT_CACHE = False

DELETE_OUTPUT_DIRECTORY = True

PLUGINS = ['read_more']

SUMMARY_MAX_LENGTH = 20
SUMMARY_END_SUFFIX = "... "
READ_MORE_LINK = '<span>Read more</span>'

ARCHIVES_SAVE_AS=''
AUTHOR_SAVE_AS=''
AUTHORS_SAVE_AS=''
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'blog'
CATEGORY_SAVE_AS=''
CATEGORIES_SAVE_AS=''
TAGS_SAVE_AS=''
ARTICLE_PATHS = ['blog']
ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'

DISPLAY_PAGES_ON_MENU = True

DIRECT_TEMPLATES = ['index', 'projects']
BLOG_URL = 'blog/'
BLOG_SAVE_AS = 'blog/index.html'
PROJECT_URL = 'projects/'
PROJECT_SAVE_AS = 'projects/index.html'