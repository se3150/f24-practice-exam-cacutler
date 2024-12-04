# Practice Exam

This is the practice exam for SE3150. It is very close to the actual final exam and should give you a good idea about where you need to study or work to get your environment ready so that you can actually do the final on your computer.

For this practice, you will write two test suites, a **unit test suite** and a **functional test suite**, then you will implement a CI workflow using github actions for both. Begin by using the code provided at the start of the this practice.

## Part 1

Create a unit test suite using Python, **pytest**, **pytest-describe**, **pytest-spec**, and **pytest-mock**. The program under test is the **Battery** class (**battery.py**), a simple battery simulator.

Design and implement unit test cases in a program called **test_battery.py** that thoroughly verify the functionality of the methods. For all but the parts of **recharge** and **drain** that interact with the '**external monitor**' do not use test doubles - just write asserts to ensure that the functions correctly change the state of the battery. 

For the external monitor portion of **recharge** and **drain**, implement test doubles for the **notify_recharge** and **notify_drain** methods as you deem appropriate.  Use stubs to force the desired test outcomes, and use mocks to verify correct implementation details. (That the function was called correctly as a part of recharge and drain.)

Be sure to verify both success and failure outcomes for the methods under test.

## Part 2

Create a functional test suite using **Python**, **behave**, **behave-webdriver**, and **ChromeDriver**.   The application under test is page that helps you calculate the area of a triangle. Design and implement the scenario outlined in the **HeronsCalculator.feature**. You may use built-in step definitions, custom step definitions, or a combination of both.

## Part 3

Configure a continuous integration workflow that automates test runners for the two test suites above using GitHub Actions.

Create a single workflow that includes one job for each of the two test runners.

When finished, demonstrate your exam progress to the instructor via the GitHub Actions web interface. Show the test runner output for each of the two jobs. 