import collections
import re

LIBRARY_DATA = """
TITLE: Hitchhiker's Guide to the Galaxy
AUTHOR: Douglas Adams
DESCRIPTION: Seconds before the Earth is demolished to make way for a galactic freeway,
Arthur Dent is plucked off the planet by his friend Ford Prefect, a researcher for the
revised edition of The Hitchhiker's Guide to the Galaxy who, for the last fifteen years,
has been posing as an out-of-work actor.

TITLE: Dune
AUTHOR: Frank Herbert
DESCRIPTION: The troubles begin when stewardship of Arrakis is transferred by the
Emperor from the Harkonnen Noble House to House Atreides. The Harkonnens don't want to
give up their privilege, though, and through sabotage and treachery they cast young
Duke Paul Atreides out into the planet's harsh environment to die. There he falls in
with the Fremen, a tribe of desert dwellers who become the basis of the army with which
he will reclaim what's rightfully his. Paul Atreides, though, is far more than just a
usurped duke. He might be the end product of a very long-term genetic experiment
designed to breed a super human; he might be a messiah. His struggle is at the center
of a nexus of powerful people and events, and the repercussions will be felt throughout
the Imperium.

TITLE: A Song Of Ice And Fire Series
AUTHOR: George R.R. Martin
DESCRIPTION: As the Seven Kingdoms face a generation-long winter, the noble Stark family
confronts the poisonous plots of the rival Lannisters, the emergence of the
White Walkers, the arrival of barbarian hordes, and other threats.

"""

class Book(object):
    def __init__(self, title, auth):
        self.title = title
        self.auth = auth

    def __str__(self):
    	return self.title

class Library:
    def __init__(self, data):
        self.inv_indx = collections.defaultdict(set)
        cur_title, cur_auth, cur_book = '','',None
        for line in data.splitlines():
            if line == "\n": continue
            if line.startswith("TITLE"):
                cur_title = line.split(": ")[1]
            elif line.startswith("AUTHOR"):
                cur_auth = line.split(": ")[1]
                cur_book = Book(cur_title, cur_auth)
            else:
                for word in re.sub("[^\w]", " ",  line).split():
                    self.inv_indx[word].add(cur_book)
        print(self.inv_indx)

    def search(self, word):
        if word in self.inv_indx:
            return list(self.inv_indx[word])
        else:
            return []


if __name__ == '__main__':
    library = Library(LIBRARY_DATA)
    
    # Search for "Arrakis".
    first_results = library.search("Arrakis")
    print(len(first_results) > 0 and first_results[0].title == "Dune")
    
    # Search for "winter".
    second_results = library.search("winter")
    print(len(second_results) > 0 and second_results[0].title == "A Song Of Ice And Fire Series")
    
    # # Search for "demolished".
    third_results = library.search("demolished")
    print (len(third_results) > 0 and third_results[0].title == "Hitchhiker's Guide to the Galaxy")
    
    # # Search for "the".
    fourth_results = library.search("the")
    print len(fourth_results)
    titles = [result.title for result in fourth_results]
    print "Dune" in titles
    print "A Song Of Ice And Fire Series" in titles
    print "Hitchhiker's Guide to the Galaxy" in titles
