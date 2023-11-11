"""
Author: masakokh
Year: 2023
Note:
Version: 1.0.0
"""
import json
import os
import platform
import sys


#
def getJson(filename: str) -> dict | None:
	"""

	:param filename:
	:return:
	"""
	# found file
	if os.path.exists(filename):
		# open file
		with open(filename, 'r') as fo:
			return json.load(fo)

	# unreadable
	print('File not found!')
	return None


#
def getPlatformName() -> str:
	"""

	:return:
	"""
	return sys.platform


def getThemeName(theme: list, home: str= '~') -> str | None:
	"""

	:param theme:
	:param home:
	:return:
	"""
	name    = ''
	for n in theme:
		themeName   = f'{os.path.expanduser(home)}/.{n}'
		# found
		if os.path.exists(themeName):
			return themeName
	# not found
	return None


#
def exportValue(filename: str, theme: list) -> None:
	"""

	:param filename:
	:param theme:
	:return:
	"""
	# init
	foundTheme  = ''
	foundOS     = False
	isSuccessful= False
	obj         = getJson(filename)

	# possible
	if obj:
		# get platform name or OS name
		OSName  = getPlatformName()

		#
		match OSName:
			case 'ubuntu':
				foundOS = True
				print('The current OS is ' + obj.get('os').get(OSName).get('note'))

			case 'darwin':
				foundOS = True
				print('The current OS is ' + obj.get('os').get(OSName).get('note'))

			case _:
				print('Unidentified os')

	#
	if foundOS:
		content = ''
		theme   = getThemeName(theme)
		print(theme)
		#
		for c in obj.get('alias'):
			content += f'{c}\n'

		# found fie
		if theme:
			# append to theme file
			with open(theme, 'a+') as fo:
				# write content
				fo.write(content)
				isSuccessful    = True

	# success
	if isSuccessful:
		print('Everything is going good.')
	# fail
	else:
		print('Something went wrong.')


# execute function
exportValue(
	filename= 'env.json'
	, theme =[
		'bashrc'
		, 'zshrc'
	]
)
