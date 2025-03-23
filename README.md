##  PurgoMalum API Tests ฅ^•ﻌ•^ฅ

### Tools of Choice

- [Pytest BDD Framework](https://pytest-bdd.readthedocs.io/en/stable/)
- [Postman Web Version](https://web.postman.co/home)

### Prerequisites

You have Python and `pytest-bdd` installed. While installing Python is a beast, [the installation of pytest-bdd should be relatively straightforward](https://pytest-bdd.readthedocs.io/en/stable/#install-pytest-bdd). 

### How to Run 

Ideally, you have Visual Studio [code that allows you to set up a launch.json file to run/debug tests](https://code.visualstudio.com/docs/editor/debugging). 

You can find the necessary launch.json file in the `resources` folder for this project. 

If you are unwilling to go through the hassle of using Visual Studio, then go through the following steps: 

-   Navigate to the tests folder via the command `cd tests`
-   Then, run the command `pytest <testToRun>`

  ### Answers to Questions. 

1. It took me about a day. If I had more time, I would have added steps that could be reused, as I am not happy with the redundancy within the `GIVEN` steps; however, the focus for this round was to get the tests working in the first place, even if the test case for returning an error is not fully implemented due to `XML` not being well-formatted -- I did what I could, though!

2. Integrating automation tools with things like `BrowserStack` is cool. I haven't had much exposure to it, but I like the idea of being able to perform cross-browser using it. Automation tools have become increasingly more sophisticated, and I like that you're no longer limited to `Selenium`. Some interesting developments are happening in [automated video game testing](https://research-portal.uu.nl/ws/portalfiles/portal/233300296/978-3-030-88106-1_5.pdf).

3. Find the [file](https://github.com/HedonisticOpportunist/purgo-malum-api-tests/blob/main/resources/silly.json) here. 

5. Manual testing is challenging because you grow tired and careless when you run the same tests repeatedly: this is where automation becomes useful, as you let a computer perform those more tedious tasks. At the same time, you can focus on more interesting tasks. 
