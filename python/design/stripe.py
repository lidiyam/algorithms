
import datetime
import time

class RateLimited(object):

	def __init__(self, K, Q):
		self.K = K
		self.Q = Q
		self.user_counts = {}	# name: (t0, counts)

	def endpoint(self, username, inputs):

		ts_now = int(time.time())
		# ts_now = datetime.datetime.now()

		if username in self.user_counts:
			[t0, counts] = self.user_counts[username]

			if t0 + self.Q < ts_now:
				#  exceeded time limit
				print 'exceeded'
				self.user_counts[username] = [ts_now, 1]
			else:
				self.user_counts[username][1] = counts + 1
				if self.user_counts[username][1] > self.K:
					raise Exception

		else:
			self.user_counts[username] = [ts_now, 1]

		print username, ', ts: ', self.user_counts[username][0], ', counts: ', self.user_counts[username][1],': hello word'



if __name__ == '__main__':
	rateLimiter = RateLimited(5, 2)
	rateLimiter.endpoint('lidiya',[])
	rateLimiter.endpoint('joe',[])
	rateLimiter.endpoint('lidiya',[])
	rateLimiter.endpoint('lidiya',[])
	rateLimiter.endpoint('lidiya',[])
	rateLimiter.endpoint('lidiya',[])
	rateLimiter.endpoint('joe',[])
	rateLimiter.endpoint('lidiya',[]) # not printed
