
import tinkerer
import tinkerer.paths        

# **************************************************************
# TODO: Edit the lines below
# **************************************************************

# Change this to the name of your blog
project = u'Computer Networking : Principles, Protocols and Practice'                   

# Change this to the tagline of your blog
#tagline = u'recent updates to the online book'                  
tagline =u'Open-source networking ebook'
# Change this to your name
author = u'Olivier Bonaventure'

# Change this to your copyright string
copyright = u'2012-2014, ' + author +u' and collaborators'        

# Change this to your blog root URL (required for RSS feed)
website = u'http://sites.uclouvain.be/CNP3/blog/html'
#http://cnp3blog.info.ucl.ac.be/'                              

# **************************************************************
# More tweaks you can do
# **************************************************************

# Add your Disqus shortname to enable comments powered by Disqus
#disqus_shortname = 'cnp3'                                  

# Change your favicon (new favicon goes in _static directory)
html_favicon = 'tinkerer.ico'           

# Pick another Tinkerer theme or use your own
html_theme = "modern5"
#html_theme = "boilerplate"

# Theme-specific options, see docs
html_theme_options = { }                                  

# Link to RSS service like FeedBurner if any, otherwise feed is
# linked directly
rss_service = None

# Number of blog posts per page
posts_per_page = 2

# **************************************************************
# Edit lines below to further customize Sphinx build
# **************************************************************

# Add other Sphinx extensions here
extensions = [ 'sphinxcontrib.bibtex', 'tinkerer.ext.blog', 'tinkerer.ext.disqus', 'sphinx.ext.pngmath', 'sphinxcontrib.mscgen','sphinx.ext.graphviz']

# Add other template paths here
templates_path = ['_templates']

# Add other static paths here
html_static_path = ['_static', tinkerer.paths.static]

# Add other theme paths here
html_theme_path = [tinkerer.paths.themes]                 
# Add file patterns to exclude from build
exclude_patterns = ["drafts/*"]                                     

# Add templates to be rendered in sidebar here
html_sidebars = {
    "**": ["recent.html", "searchbox.html"]
}


# added

language = u"en"

# **************************************************************
# Do not modify below lines as the values are required by 
# Tinkerer to play nice with Sphinx
# **************************************************************

source_suffix = tinkerer.source_suffix
master_doc = tinkerer.master_doc
version = tinkerer.__version__
release = tinkerer.__version__
html_title = project
html_use_index = False
html_show_sourcelink = False
html_add_permalinks = None
