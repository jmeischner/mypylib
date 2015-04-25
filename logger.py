from file import write_string
from datetime import datetime

class log(object):
	'''
		Class for logging function calls
	'''
	log_file = "log.txt"
	
	
	def __init__(self, log):
		'''
			Function which inits the message for this logger
		'''
		self.message = log
	
	def __call__(self, fn):
		'''
			Function which is called everytime the function to log is called
		'''
		def func_wrapper(*args):
			now = datetime.today().strftime("%d.%m.%Y; %H:%M")
			write_string(now + ";" + self.message, self.log_file)
			return fn(*args)
		return func_wrapper