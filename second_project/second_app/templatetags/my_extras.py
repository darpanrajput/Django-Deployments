from django import template

register=template.Library()


@register.filter(name='cut')
def cut_this(value,arg):
	""" this cuts out all values of arg from the strings"""
	return value.replace(arg,'')



# register.filter('cut',cut_this)
