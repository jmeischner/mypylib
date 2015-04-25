#######################################################################################
#				Module with code especially for shell scripts						#
#######################################################################################

class help_option(object):
	'''
		Basis Decorator for Shell Scripts with built-in "--help" for given Dictionary Elements.
		All Options should start with "-" char. The arguments should be given in the following way:
		{
			"-s": ("some random string", "varname", "default value"),
			...
			"info": "Info text beneath the options"
		}
	'''
	help = ["--help", "--h"]
	arguments = dict()
	additional_text_key = "info"
	additional_text = str()
	_all_have_defaults = True
	_printed_help = False
	
	def __init__(self, arg):
		'''
			Init function for decorator
		'''
		self.arguments = dict(**arg)
		if self.additional_text_key in self.arguments.keys():
			self.additional_text = self.arguments[self.additional_text_key]
			del self.arguments[self.additional_text_key]
		
		for _, value in self.arguments.items():
			assert isinstance(value, tuple) and len(value) >= 2, "'shell.help_option': There is a mistake in your decorator definition. Try looking in the documentation"
			if self._all_have_defaults:
				self._all_have_defaults = len(value) == 3
		
	def __call__(self, fn):
		'''
			When Function called, these Function will be returned
		'''
		def func_wrapper(*args):
			'''
				Function looks for "--help" or command line parameter
			'''
			params = list(args)[0]
			keys = self.arguments.keys()
			if len(params) == 0 and not self._all_have_defaults:
				print "You should give at least one argument, try '--help' for more information."
				return
				
			elif len(params) > 0:
				if params[0] not in self.help and params[0] not in keys and not params[0].startswith('-'):
					del params[0]	
		
			if len(params) > 0 and params[0] in self.help:
				self._printed_help = True
				print "Options:"
				for (key, value) in self.arguments.items():
					print " ", key + ",\t\t", value[0], "  [required]" if len(value) == 2 else "[default: " + value[2] + "]"
				if self.additional_text != str():
					print "\n" + self.additional_text
				
			if not self._printed_help:
				parameter = dict()
				if len(params) > 0 or self._all_have_defaults:
					for _, value in self.arguments.items():
						if len(value) == 3:
							parameter[value[1]] = value[2]
					for i in range (0, len(params), 2):
						if params[i] in self.arguments.keys():
							parameter[self.arguments[params[i]][1]] = params[i+1] 
						else:
							print "'" + params[i] + "' is no accepted option, use '--help' to see all possible options."
							return
					
					if len(self.arguments) == len(parameter):
						return fn(**parameter)
						
					else:
						print "You miss some arguments, use '--help' for more informations."
						return
						
				else:
					print "You miss some arguments, use '--help' for more informations."
					return
					
		return func_wrapper