import threading

def worker():
	"""Threading worker function"""
	print 'Worker'
	return

threads = []
for i in range(5):
	t = threading.Thread(target=worker)
	threads.append(t)
	t.start()

