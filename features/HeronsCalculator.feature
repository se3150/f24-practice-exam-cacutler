Feature: calculate the area of a triangle
As an aspiring mathematician
I should be able to calculate the area of a triangle
So that I can chat with my math friends like a pro
    Scenario: I can calculate the area of a triangle
        Given I open the url "https://byjus.com/herons-calculator/"
        # write your steps here
        When I add "3" to the inputfield "#a"
        And I add "4" to the inputfield "#b"
        And I add "5" to the inputfield "#c"
        And I click on the element "input.clcbtn"
        Then I expect that element "#_d" is not empty