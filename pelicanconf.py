AUTHOR = 'sm4x'                                 # Site Author
SITENAME = 'Pelican Minimal'                       # Your Sitename
SITESUBTITLE = 'A Pelican basic theme.'
SITEURL = 'http://maxschattauer.de'
'''
    Base URL of your web site. Not defined by default, so it is best to specify your SITEURL; if you do not, feeds will not be generated with properly-formed URLs. If your site is available via HTTPS, this setting should begin with https:// — otherwise use http://. Then append your domain, with no trailing slash at the end. Example: SITEURL = 'https://example.com'
'''

THEME = 'themes/minimal'

PATH = 'content'
'''
    Path to content directory to be processed by Pelican. If undefined, and content path is not specified via an argument to the pelican command, Pelican will use the current working directory.
'''

TIMEZONE = 'Europe/Berlin'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

########################## ADDITIONAL SETTINGS ######################

RELATIVE_URLS = True
'''
Defines whether Pelican should use document-relative URLs or not. Only set this to True when developing/testing and only if you fully understand the effect it can have on links/feeds.
'''

# GITHUB_URL = 'http://github.com/sm4x/'
# DISQUS_SITENAME = ''
# REVERSE_CATEGORY_ORDER = True
# LOCALE = "C"

USE_FOLDER_AS_CATEGORY = True

'''
    When you don’t specify a category in your post metadata, set this setting to True, and organize your articles in subfolders, the subfolder will become the category of your post. If set to False, DEFAULT_CATEGORY will be used as a fallback.
'''

DEFAULT_CATEGORY = 'misc'
'''
    The default category to fall back on.
'''

DISPLAY_PAGES_ON_MENU = True
'''
    Whether to display pages on the menu of the template. Templates may or may not honor this setting.
'''

DISPLAY_CATEGORIES_ON_MENU = True
'''
    Whether to display categories on the menu of the template. Templates may or not honor this setting.
'''

DOCUTILS_SETTINGS = {}
'''
    Extra configuration settings for the docutils publisher (applicable only to reStructuredText). See Docutils Configuration settings for more details.
'''

DELETE_OUTPUT_DIRECTORY = True
'''
    Delete the output directory, and all of its contents, before generating new files. This can be useful in preventing older, unnecessary files from persisting in your output. However, this is a destructive setting and should be handled with extreme care.
'''

OUTPUT_RETENTION = []
'''
    A list of filenames that should be retained and not deleted from the output directory. One use case would be the preservation of version control data.

    Example:

    OUTPUT_RETENTION = [".hg", ".git", ".bzr"]
'''

JINJA_ENVIRONMENT = {'trim_blocks': True, 'lstrip_blocks': True}
'''
    A dictionary of custom Jinja2 environment variables you want to use. This also includes a list of extensions you may want to include. See Jinja Environment documentation.
'''

JINJA_FILTERS = {}
'''
    A dictionary of custom Jinja2 filters you want to use. The dictionary should map the filtername to the filter function.

    Example:

    import sys
    sys.path.append('to/your/path')

    from custom_filter import urlencode_filter
    JINJA_FILTERS = {'urlencode': urlencode_filter}

    See: Jinja custom filters documentation.
'''

JINJA_GLOBALS = {}
'''
    A dictionary of custom objects to map into the Jinja2 global environment namespace. The dictionary should map the global name to the global variable/function. See: Jinja global namespace documentation.
'''

JINJA_TESTS = {}
'''
    A dictionary of custom Jinja2 tests you want to use. The dictionary should map test names to test functions. See: Jinja custom tests documentation.
'''

LOG_FILTER = []
'''
    A list of tuples containing the logging level (up to warning) and the message to be ignored.

    Example:

    LOG_FILTER = [(logging.WARN, 'TAG_SAVE_AS is set to False')]
'''

READERS = {}
'''
    A dictionary of file extensions / Reader classes for Pelican to process or ignore.

    For example, to avoid processing .html files, set:

    READERS = {'html': None}

    To add a custom reader for the foo extension, set:

    READERS = {'foo': FooReader}
'''

IGNORE_FILES = ['.#*']
'''
    A list of glob patterns. Files and directories matching any of these patterns will be ignored by the processor. For example, the default ['.#*'] will ignore emacs lock files, and ['__pycache__'] would ignore Python 3’s bytecode caches.
'''

# MARKDOWN = {}

'''
    Extra configuration settings for the Markdown processor. Refer to the Python Markdown documentation’s Options section for a complete list of supported options. The extensions option will be automatically computed from the extension_configs option.

    Defaults to:

    MARKDOWN = {
        'extension_configs': {
            'markdown.extensions.codehilite': {'css_class': 'highlight'},
            'markdown.extensions.extra': {},
            'markdown.extensions.meta': {},
        },
        'output_format': 'html5',
    }

    Note

    The dictionary defined in your settings file will replace this default one.
'''

OUTPUT_PATH = 'output/'
'''
    Where to output the generated files. This should correspond to your web server’s virtual host root directory.
'''

PAGE_PATHS = ['pages']
'''
    A list of directories and files to look at for pages, relative to PATH.
'''

PAGE_EXCLUDES = []
'''
    A list of directories to exclude when looking for pages in addition to ARTICLE_PATHS.
'''

ARTICLE_PATHS = ['']
'''
    A list of directories and files to look at for articles, relative to PATH.
'''

ARTICLE_EXCLUDES = []
'''
    A list of directories to exclude when looking for articles in addition to PAGE_PATHS.
'''

OUTPUT_SOURCES = False
'''
    Set to True if you want to copy the articles and pages in their original format (e.g. Markdown or reStructuredText) to the specified OUTPUT_PATH.
'''

OUTPUT_SOURCES_EXTENSION = '.text'
'''
    Controls the extension that will be used by the SourcesGenerator. Defaults to .text. If not a valid string the default value will be used.
'''

PLUGINS = None
'''
    The list of plugins to load. See Plugins.
'''

PLUGIN_PATHS = []
'''
    A list of directories where to look for plugins. See Plugins.
'''

STATIC_PATHS = ['images']
'''
    A list of directories (relative to PATH) in which to look for static files. Such files will be copied to the output directory without modification. Articles, pages, and other content source files will normally be skipped, so it is safe for a directory to appear both here and in PAGE_PATHS or ARTICLE_PATHS. Pelican’s default settings include the “images” directory here.
'''
STATIC_EXCLUDES = []
'''
    A list of directories to exclude when looking for static files.
'''

STATIC_EXCLUDE_SOURCES = True
'''
    If set to False, content source files will not be skipped when copying files found in STATIC_PATHS. This setting is for backward compatibility with Pelican releases before version 3.5. It has no effect unless STATIC_PATHS contains a directory that is also in ARTICLE_PATHS or PAGE_PATHS. If you are trying to publish your site’s source files, consider using the OUTPUT_SOURCES setting instead.
'''

STATIC_CREATE_LINKS = False
'''
    Create links instead of copying files. If the content and output directories are on the same device, then create hard links. Falls back to symbolic links if the output directory is on a different filesystem. If symlinks are created, don’t forget to add the -L or --copy-links option to rsync when uploading your site.
'''

STATIC_CHECK_IF_MODIFIED = False
'''
    If set to True, and STATIC_CREATE_LINKS is False, compare mtimes of content and output files, and only copy content files that are newer than existing output files.
'''

TYPOGRIFY = False
'''
    If set to True, several typographical improvements will be incorporated into the generated HTML via the Typogrify library, which can be installed via: python -m pip install typogrify
'''

TYPOGRIFY_IGNORE_TAGS = []
'''
    A list of tags for Typogrify to ignore. By default Typogrify will ignore pre and code tags. This requires that Typogrify version 2.0.4 or later is installed
'''

TYPOGRIFY_DASHES = 'default'
'''
    This setting controls how Typogrify sets up the Smartypants filter to interpret multiple dash/hyphen/minus characters. A single ASCII dash character (-) is always rendered as a hyphen. The default setting does not handle en-dashes and converts double-hyphens into em-dashes. The oldschool setting renders both en-dashes and em-dashes when it sees two (--) and three (---) hyphen characters, respectively. The oldschool_inverted setting turns two hyphens into an em-dash and three hyphens into an en-dash.
'''

SUMMARY_MAX_LENGTH = 50
'''
    When creating a short summary of an article, this will be the default length (measured in words) of the text created. This only applies if your content does not otherwise specify a summary. Setting to None will cause the summary to be a copy of the original content.
'''

SUMMARY_END_SUFFIX = '…'
'''
    When creating a short summary of an article and the result was truncated to match the required word length, this will be used as the truncation suffix.
'''

WITH_FUTURE_DATES = True
'''
    If disabled, content with dates in the future will get a default status of draft. See Reading only modified content for caveats.
'''

INTRASITE_LINK_REGEX = '[{|](?P<what>.*?)[|}]'
'''
    Regular expression that is used to parse internal links. Default syntax when linking to internal files, tags, etc., is to enclose the identifier, say filename, in {} or ||. Identifier between { and } goes into the what capturing group. For details see Linking to internal content.
'''

PYGMENTS_RST_OPTIONS = []
'''
    A list of default Pygments settings for your reStructuredText code blocks. See Syntax highlighting for a list of supported options.
'''

CACHE_CONTENT = False
'''
    If True, saves content in caches. See Reading only modified content for details about caching.
'''

CONTENT_CACHING_LAYER = 'reader'
'''
    If set to 'reader', save only the raw content and metadata returned by readers. If set to 'generator', save processed content objects.
'''

CACHE_PATH = 'cache'
'''
    Directory in which to store cache files.
'''

GZIP_CACHE = True
'''
    If True, use gzip to (de)compress the cache files.
'''

CHECK_MODIFIED_METHOD = 'mtime'

'''
    Controls how files are checked for modifications.

        If set to 'mtime', the modification time of the file is checked.

        If set to a name of a function provided by the hashlib module, e.g. 'md5', the file hash is checked.
'''

LOAD_CONTENT_CACHE = False
'''
    If True, load unmodified content from caches.
'''

WRITE_SELECTED = []
'''
    If this list is not empty, only output files with their paths in this list are written. Paths should be either absolute or relative to the current Pelican working directory. For possible use cases see Writing only selected content.
'''

# FORMATTED_FIELDS = ['summary']
'''
    A list of metadata fields containing reST/Markdown content to be parsed and translated to HTML.
'''

PORT = 8000
'''
    The TCP port to serve content from the output folder via HTTP when pelican is run with –listen
'''
BIND = ''

'''
    The IP to which to bind the HTTP server.
'''

