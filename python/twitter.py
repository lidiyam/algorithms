"""
Given a List<String> sentences and a List<String> queries return 
indices of all sentences that have each word in query string.

E.g.

List<String> sentences = ["bob and alice like to text each other", "bob does not like to ski", "alice likes to ski"]
List<String> queries = ["bob alice", "alice", "to ski"]

Result:

0 (Query string "bob alice", all words found in sentence index 0)

0 2 (Query string "alice", all words found in sentence index 0 and 2)

1 2 (Query string "to ski", all words found in sentence index 1 and 2)
"""
import collections

def containAll(sentences, queries):
	hashMap = {}
	# sentenceMap = {}
	for i, sentence in enumerate(sentences):
		for word in sentence.split(" "):
			# if i in sentenceMap:
			# 	sentenceMap[i].add(word)
			# else:
			# 	sentenceMap[i] = set(word)
			if word in hashMap:
				hashMap[word].add(str(i))
			else:
				hashMap[word] = set()
				hashMap[word].add(str(i))

	for query in queries:
		res = set()
		words = query.split(" ")
		for word in words:
			if word in hashMap:
				indices = hashMap[word]
				if not res:
					res = indices
				else:
					res = res.intersection(indices)
			else:
				break
		print ' '.join(res)


s = ["bob and alice like to text each other", "bob does not like to ski", "alice likes to ski"]
q = ["bob alice", "alice", "to ski"]
containAll(s, q)
