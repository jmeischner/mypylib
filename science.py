import numpy as np

def autocorrelation_function_of(x):	
	''' 
		Bestimmt die Autokorrelationsfunktion eines numpy arrays
	'''
	x = x-np.mean(x)
	r = np.fft.ifft(np.fft.fft(x)*np.conjugate(np.fft.fft(x)))
	r = r/r[0];
	return r[0:len(r)/2]

def integ_acorr_func_of(series):
	'''
		Bestimmt die integrierte Autokorrelationsfunktion
	'''
	a_series = autocorrelation_function_of(series)
	return np.cumsum(a_series)

def autocorrelation_time_of(integrated_acorr_func):
	'''
		Selbstkonsistente Bestimmung der Autokorrelationszeit
	'''
	time = 0
	integ_func = integrated_acorr_func.real
	tau_int = 0.5 + integ_func[time]

	while (time < 8*tau_int):
		tau_int = 0.5 + integ_func[time]
		time += 1

	return time