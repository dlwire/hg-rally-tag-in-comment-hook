import unittest
import re
from mercurial import util

def hook_entry_point(ui, repo, node=None, **kwargs):
    print("Executing comment_hook")
    hg = MercurialWrapper(repo, node)

    if not is_rally_tag_present(hg):
        ui.warn("Commit comments should contain Rally tags of the form [US | DE]#####\n")
        return True

    return False

def is_rally_tag_present(hg):
    tagPresent = False
    for comment in hg.get_incoming_comments():
        tagPresent |= None != re.search(r'([US|DE][0-9]+)', comment, re.I)
    return tagPresent

class MercurialWrapper():
    def __init__(self, repo, node):
       if node == None:
           self.changesets = [repo[None]]
       else:
           self.changesets = [repo[changeset] for changeset in xrange(repo[node], len(repo))]

    def get_incoming_comments(self):
       return [changeset.description() for changeset in self.changesets]        


class MockMercurial():
    def __init__(self):
        self.incomingComments = []

    def get_incoming_comments(self):
        return self.incomingComments

    def add_incoming_comment(self, comment):
        self.incomingComments.append(comment)

class is_rally_tag_present_test(unittest.TestCase):
    def test_when_user_story_tag_present_return_true(self):
        hg = MockMercurial()
	hg.add_incoming_comment('US123')

        self.assertTrue(is_rally_tag_present(hg))

    def test_user_story_tag_is_not_case_sensitive(self):
        hg = MockMercurial()
	hg.add_incoming_comment('us123')

	self.assertTrue(is_rally_tag_present(hg))

    def test_when_us_present_return_false(self):
        hg = MockMercurial()
        hg.add_incoming_comment('this is for US')

        self.assertFalse(is_rally_tag_present(hg))
	
    def test_when_defect_tag_present_return_true(self):
        hg = MockMercurial()
	hg.add_incoming_comment('DE123')

	self.assertTrue(is_rally_tag_present(hg))

		
if __name__ == "__main__":
    unittest.main()
