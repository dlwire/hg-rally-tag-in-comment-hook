Feature: Comments with story tags are valid
    Comments containing an id with the following format are valid:
    US followed by any number of numbers is a valid comment

    Scenario: Comment with US1 can be committed
        Given the rally tag in comment hook is enabled
        When I commit a changest with the comment 'US1'
        Then the commit is successful   

    Scenario: Comment with US6893 can be committed
        Given the rally tag in comment hook is enabled
        When I commit a changest with the comment 'US6893'
        Then the commit is successful 
