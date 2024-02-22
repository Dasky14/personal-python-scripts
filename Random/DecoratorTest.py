from time import perf_counter, sleep

def timer(func):
	def wrapper(*args, **kwargs):
		start_time = perf_counter()
		func(*args, **kwargs)
		end_time = perf_counter()
		total_time = round(end_time - start_time, 2)
		print("Function \"" + func.__name__ + "\" took", total_time, "seconds")
	return wrapper

@timer
def do_something(sleep_time):
	sleep(sleep_time)
	print("something has been done")

do_something(0.25)
do_something(0.5)
do_something(0.75)
do_something(1.00)