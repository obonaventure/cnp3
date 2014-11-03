# -*- coding: utf-8 -*-
# Extension by Lionel Chalet

from docutils import nodes
from docutils.parsers.rst import Directive
from sphinx.errors import SphinxError
import os, sys, copy, hashlib, random

__version__ = '0.1'

question_number = 0
alternative_number = 0
language = 'en'

translations = {
	'fr': {
		'verify_title': u'Verifiez vos réponses',
		'verify': u'Vérifier'
	},
	'en': {
		'verify_title': 'Verify your answers',
		'verify': 'Verify'
	}
}

def setup(app):
	app.add_config_value('mcq_nb_prop', -1, '')
	app.add_config_value('mcq_nb_rows', 7, '')
	app.add_config_value('mcq_upload_url', '', '')
	app.add_config_value('mcq_inginious_url', '', '')

	app.add_node(Question, html=(html_visit_question, html_depart), latex=(latex_visit_question, pass_visit))
	app.add_node(Query, html=(html_visit_query, html_depart), latex=(pass_visit, pass_visit))
	app.add_node(Positive, html=(html_visit_positive, html_depart_alternative), latex=(latex_visit_posneg, latex_depart_posneg))
	app.add_node(Negative, html=(html_visit_negative, html_depart_alternative), latex=(latex_visit_posneg, latex_depart_posneg))
	app.add_node(Textbox, html=(html_visit_textbox, html_depart), latex=(latex_visit_textbox, None))
	app.add_node(Comment, html=(html_visit_comment, html_depart), latex=(skip_visit, None))

	app.add_directive('question', QuestionDirective)
	app.add_directive('positive', PositiveDirective)
	app.add_directive('negative', NegativeDirective)
	app.add_directive('textbox', TextboxDirective)
	app.add_directive('comment', CommentDirective)

	app.connect('builder-inited', add_dependencies)
	app.connect('doctree-resolved', verify_structure)
	app.connect('doctree-resolved', html_add_content)
	app.connect('doctree-resolved', latex_add_content)
	app.connect('doctree-resolved', latex_shuffle)
	app.connect('doctree-resolved', epub_add_javascript)

class CopyableNode(nodes.General, nodes.Element):
	def deepcopy(self):
		"""
			Nodes attributes aren't available with the LaTeX builder after the 'doctree-read' event
			This is some kind of patch I suppose ...
		"""
		return copy.copy(self)

class Question(CopyableNode):
	id = None
	nb_pos = 1
	nb_prop = -1

class Alternative(CopyableNode):
	pass

class Query(Alternative):
	pass

class Positive(Alternative):
	pass

class Negative(Alternative):
	pass

class Textbox(Alternative):
	nb_rows = 7

class Comment(CopyableNode):
	pass

def html_visit_question(self, node):
	global question_number, alternative_number
	question_number += 1
	alternative_number = 0
	classes = 'question'
	if not node.id:
		node.id = 'questionId' + str(question_number)
	else:
		classes += ' inginious'
	self.body.append(self.starttag(node, 'div', CLASS=classes, IDS=[str(node.id)]))
	self.body.append("<input type='hidden' class='nb_pos' value='" + str(node.nb_pos) + "' />")
	self.body.append("<input type='hidden' class='nb_prop' value='" + str(node.nb_prop) + "' />")

def html_visit_query(self, node):
	self.body.append(self.starttag(node, 'div', CLASS='query'))

def html_visit_positive(self, node):
	global alternative_number
	self.body.append(self.starttag(node, 'div', CLASS='positive', IDS=[str(alternative_number)]))
	html_visit_alternative(self, node)
	alternative_number += 1

def html_visit_negative(self, node):
	global alternative_number
	self.body.append(self.starttag(node, 'div', CLASS='negative', IDS=[str(alternative_number)]))
	html_visit_alternative(self, node)
	alternative_number += 1

def html_visit_alternative(self, node):
	if node.parent.nb_pos > 1:
		self.body.append("<input type='checkbox' class='choice' name='" + str(question_number) + "' />")
	else:
		self.body.append("<input type='radio' class='choice' name='" + str(question_number) + "' />")
	self.body.append(self.starttag(node, 'div', CLASS='content'))

def html_visit_textbox(self, node):
	self.body.append(self.starttag(node, 'div', CLASS='textbox'))
	self.body.append('<textarea rows="' + str(node.nb_rows) + '" cols="65"></textarea>')

def html_visit_comment(self, node):
	self.body.append(self.starttag(node, 'div', CLASS='comment', STYLE='display:none'))

def html_depart(self, node):
	self.body.append('</div>')

def html_depart_alternative(self, node):
	for x in range(2):
		html_depart(self, node)

def skip_visit(self, node):
	raise nodes.SkipNode

def pass_visit(self, node):
	pass

def latex_visit_question(self, node):
	pass

def latex_visit_posneg(self, node):
	latex_visit_posneg.count += 1
	self.body.append('\n\\needspace{3\\baselineskip}'
		'\n\\CheckBox[name=' + str(latex_visit_posneg.count) + ',bordercolor=0 0 0]{}'
		'\n\\vspace{-0.7cm}'
		'\n\\begin{addmargin}[0.8cm]{0cm}')
latex_visit_posneg.count = 0

def latex_depart_posneg(self, node):
	self.body.append('\\end{addmargin}\n')

def latex_visit_textbox(self, node):
	self.body.append('\n\TextFieldFill[multiline=true,height=' + str(node.nb_rows) + '\\baselineskip,bordercolor=0 0 0]{}')
	raise nodes.SkipNode

class BaseDirective(Directive):
	has_content = True

	# This has to be replaced in subclasses
	node_class = None

	def run(self):
		node = self.node_class()
		self.state.nested_parse(self.content, self.content_offset, node)
		return [node]

class QuestionDirective(BaseDirective):
	optional_arguments = 1
	option_spec = {
		'nb_pos': int,
		'nb_prop': int
	}

	node_class = Question

	def run(self):
		node = super(QuestionDirective, self).run()[0]
		if len(self.arguments) > 0:
			node.id = self.arguments[0]
		query = Query()
		for child in node.children[:]: # Must make a copy to remove while iterating
			if not isinstance(child, Alternative):
				node.remove(child)
				query += child
		node.insert(0, query)
		app = self.state.document.settings.env.app
		node.nb_prop = app.config.mcq_nb_prop
		for option, value in self.options.items():
			setattr(node, option, value)
		validate_question_options(app, node)
		return [node]

class PositiveDirective(BaseDirective):
	node_class = Positive

class NegativeDirective(BaseDirective):
	node_class = Negative

class TextboxDirective(BaseDirective):
	option_spec = {
		'nb_rows': int
	}

	node_class = Textbox

	def run(self):
		node = super(TextboxDirective, self).run()
		app = self.state.document.settings.env.app
		if 'nb_rows' in self.options:
			node[0].nb_rows = validate_nb_rows(app, self.options['nb_rows'])
		else:
			node[0].nb_rows = validate_nb_rows(app, app.config.mcq_nb_rows)
		return node

class CommentDirective(BaseDirective):
	node_class = Comment

def add_dependencies(app):
	global language
	if app.config.language == 'fr':
		language = 'fr'

	preamble = ('\\usepackage{scrextend}'
		'\n\\usepackage{hyperref}'
		'\n\\usepackage{needspace}'
		'\n\n\\newlength\\TextFieldLength'
		'\n\\newcommand\\TextFieldFill[2][]{%'
		'\n\t\\setlength\\TextFieldLength{\\linewidth}%'
		'\n\t\\settowidth{\\dimen0}{#2 }%'
		'\n\t\\addtolength\\TextFieldLength{-\\dimen0}%'
		'\n\t\\addtolength\\TextFieldLength{-2.22221pt}%'
		'\n\t\\TextField[#1,width=\\TextFieldLength]{\\raisebox{2pt}{#2 }}%'
		'\n}')
	if 'preamble' in app.config.latex_elements:
		app.config.latex_elements['preamble'] += '\n' + preamble
	else:
		app.config.latex_elements['preamble'] = preamble

	app.add_javascript('jquery-shuffle.js')
	app.add_javascript('rst-form.js')
	app.add_stylesheet('ext.css')

def validate_question_options(app, node):
	if node.nb_pos < 1:
		app.warn('The number of positive answers to display must be greater than 0.')
		node.nb_pos = 1
	if node.nb_prop < node.nb_pos:
		app.warn('The number of propositions to display in a question ('+str(node.nb_prop)+') must be greater or equal than the number of positive answers ('+str(node.nb_pos)+') to display.')
		nb_prop = app.config.mcq_nb_prop
		if nb_prop < node.nb_pos:
			node.nb_prop = sys.maxint
		else:
			node.nb_prop = nb_prop
	if node.nb_prop == node.nb_pos:
		app.warn('The number of positive answers shouldn\'t be the same as the number of propositions. It\'s like giving the answer.')

def validate_nb_rows(app, nb_rows):
	if nb_rows < 1:
		app.warn('The number of rows in a textbox must be greater than 0.')
		return 1
	return nb_rows

class StructureError(SphinxError):
	category = 'Wrong document structure'

def verify_structure(app, doctree, docname):
	verify_alternatives(app, doctree)
	verify_comments(app, doctree)
	verify_textbox(app, doctree)
	verify_questions(app, doctree)

def verify_alternatives(app, doctree):
	for node in doctree.traverse(Alternative):
		if type(node.parent) != Question:
			raise StructureError('Every "positive", "negative" and "textbox" directives must be direct children to a "question" directive.')
		if type(node) != Textbox and len(node.children) < 1:
			raise StructureError('Every "question", "positive" and "negative" directives must have content.')

def verify_comments(app, doctree):
	for node in doctree.traverse(Comment):
		parent_type = type(node.parent)
		if len(parent_type.__bases__) < 1 or parent_type.__bases__[0] != Alternative:
			raise StructureError('Every "comment" directive must be a direct child of a "question", "positive", "negative" or "textbox" directive.')
		if len(node.children) < 1:
			raise StructureError('Every "comment" directive must have content.')
		if len(node.traverse(condition=Comment, descend=False, siblings=True)) > 1:
			raise StructureError('A "comment" directive cannot have a "comment" directive sibling.')

def verify_textbox(app, doctree):
	for node in doctree.traverse(Textbox):
		if len(node.children) > 1:
			raise StructureError('A "textbox" directive can only contain one directive (of type "comment").')

def verify_questions(app, doctree):
	for node in doctree.traverse(Question):
		if len(node.children) < 2:
			raise StructureError('A question must have some content and (a "textbox" or at least one "positive" directive).')
		if len(node.children[0].traverse(Question)) > 0:
			raise StructureError('A question cannot contain another question, you fool!')
		query_count, positive_count, negative_count, textbox_count = count_children(node)
		if len(node.children) == 2:
			if query_count != 1 or positive_count != 1 and textbox_count != 1:
				raise StructureError('A "question" directive must have at least some content and (a "positive" or "textbox" directive).')
		else:
			if query_count != 1:
				raise StructureError('Internal error. This should never happen. This is a huge bug in this program.')
			if positive_count < 1:
				raise StructureError('A "question" directive must contain at least one "positive" directive. (or only one "textbox" directive)')
			if positive_count < node.nb_pos:
				raise StructureError('A "question" directive must have at least the given number of "positive" directives children.')
			if negative_count < 1:
				app.warn('Not giving any negative proposition in a question is the same as giving the answer.')

def count_children(node):
	query_count, positive_count, negative_count, textbox_count = 0, 0, 0, 0
	for child in node.children:
		child_type = type(child)
		if len(child_type.__bases__) < 1 or child_type.__bases__[0] != Alternative:
			raise StructureError('Internal error. This should never happen. This is a huge bug in this program.')
		if child_type == Query:
			query_count += 1
		elif child_type == Positive:
			positive_count += 1
		elif child_type == Negative:
			negative_count += 1
		else:
			textbox_count += 1
	return query_count, positive_count, negative_count, textbox_count

def html_add_content(app, doctree, docname):
	field_list = doctree.next_node(nodes.field_list)
	task_id = ''
	if field_list:
		for field in field_list.traverse(nodes.field):
			field_name = field.next_node(nodes.field_name).astext()
			if field_name == 'task_id':
				task_id = field.next_node(nodes.field_body).astext()
				field_list.parent.remove(field_list)
	builder = app.builder
	if not hasattr(builder, 'format') or builder.format != 'html':
		return
	h = hashlib.md5(str(doctree)).hexdigest()
	title = ''
	node = doctree
	for t in doctree.traverse(nodes.title):
		title = t.children[0].astext()
		node = t.parent
		break
	section = nodes.section(ids=["checker"], name=["checker"])
	section += nodes.title(text=translations[language]['verify_title'])
	text = u'<div id="results" style="display: none;"></div>'
	if app.config.mcq_inginious_url and task_id:
		text += '<input type="submit" value="' + translations[language]['verify'] + '" id="submit" />'
	section += nodes.raw(format='html', text=text)
	node += section
	js = nodes.raw(format='html')
	js += nodes.Text(u'\n<script type="text/javascript">var language = "' + unicode(language) + '";'
				u' var upload_url = "' + unicode(app.config.mcq_upload_url) + '";'
				u' var hash = "' + unicode(h) + '"; var title = "' + unicode(title) + '";'
				u' var html_title = "' + unicode(app.config.html_title) + '";')
	if app.config.mcq_inginious_url and task_id:
				js += nodes.Text(u' var task_id = "' + unicode(task_id) + '"; var inginious_url = "' + unicode(app.config.mcq_inginious_url) + '";')
	js += nodes.Text(u'</script>');
	doctree += js

def latex_add_content(app, doctree, docname):
	node_begin = nodes.raw(format='latex')
	node_end = nodes.raw(format='latex')
	node_begin += nodes.Text('\n\\begin{Form}')
	node_end += nodes.Text('\n\\end{Form}')
	doctree.insert(0, node_begin)
	doctree.append(node_end)

	for q in doctree.traverse(Question):
		q.parent.children.insert(0, nodes.raw(format='latex', text='\n\\needspace{6\\baselineskip}\n'))

def latex_shuffle(app, doctree, docname):
	builder = app.builder
	if not hasattr(builder, 'format') or builder.format != 'latex':
		return # The rest of this function is done in JS with the HTML writer
	for q in doctree.traverse(Question):
		query_node = None
		pos_nodes = []
		neg_nodes = []
		textbox_node = None
		for node in q.children:
			node_type = type(node)
			if node_type == Negative:
				neg_nodes.append(node)
			elif node_type == Positive:
				pos_nodes.append(node)
			elif node_type == Query:
				query_node = node
			else:
				textbox_node = node
		children = []
		random.shuffle(pos_nodes)
		random.shuffle(neg_nodes)
		children += pos_nodes[:q.nb_pos]
		children += neg_nodes[:q.nb_prop - q.nb_pos]
		random.shuffle(children)
		children.insert(0, query_node)
		if textbox_node:
			children.append(textbox_node)
		q.children = children

def epub_add_javascript(app, doctree, docname):
	builder = app.builder
	if not hasattr(builder, 'name') or not builder.name.startswith('epub'):
		return
	# Current epub3 builders does not include .js files in the .epub
	builder.media_types.update({'.js': 'text/javascript'})
	# The page.html template used does not include javascript if embedded
	builder.globalcontext['embedded'] = False
