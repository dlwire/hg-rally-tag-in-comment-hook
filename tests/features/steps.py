from lettuce import *
from subprocess import call
from subprocess import check_call
from subprocess import check_output
from subprocess import STDOUT
from subprocess import CalledProcessError

@step(u'Given the rally tag in comment hook is enabled')
def enable_rally_tag_in_comment_hook(step):
    with open('.hg/hgrc', 'w') as f:
        f.writelines('[hooks]\npretxncommit.rally_tag_in_comment = python:~/workspace/hg-comment-hook/source/rally-tag-in-comment-hook.py:hook_entry_point\n')

@step(u'When I commit a changest with the comment \'([^\']*)\'')
def when_i_commit_a_changest_with_the_comment(step, tag):
    check_output(['touch', 'myfile'])
    check_output(['hg', 'add'])
    assert 'myfile' in check_output(['hg', 'status'])

    try:
        check_output(['hg', 'commit', '-u"temp"', '-m"' + tag + '"'], stderr=STDOUT)
    except:
        pass

@step(u'Then the commit is successful')
def then_the_commit_is_successful(step):
    assert 'myfile' not in check_output(['hg', 'status']), "File not committed"

@step(u'Then the commit is unsuccessful')
def then_the_commit_is_unsuccessful(step):
    assert 'myfile' in check_output(['hg', 'status']), "File was committed"
