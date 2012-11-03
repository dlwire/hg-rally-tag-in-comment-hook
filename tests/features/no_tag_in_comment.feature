Feature: Comments with no tags are not valid
    Comments not containing a tag are invalid

    Scenario: Comment with no tag cannot be commited
        Given the Rally tag in comment hook is enabled
        When I commit a changest with the comment 'This is my invalid comment'
        Then the commit is unsuccessful

