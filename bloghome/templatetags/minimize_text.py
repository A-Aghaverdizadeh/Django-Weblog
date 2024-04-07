from django import template

register = template.Library()

@register.filter
def minimize_text(text, max_length=100):
	"""
		Truncate the text to the specified max_length and add '...' at the end if truncated.
	"""
	if len(text) <= max_length:
		return text
	else:
		return text[:max_length] + '...'

