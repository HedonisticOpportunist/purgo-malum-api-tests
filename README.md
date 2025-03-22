##  PurgoMalum API Tests ฅ^•ﻌ•^ฅ

### Tools of Choice

- [Pytest BDD Framework](https://pytest-bdd.readthedocs.io/en/stable/)
- [Postman Web Version](https://web.postman.co/home)
- Visual Studio Code

### Prerequisites

You have Python and `pytest-bdd` installed. While installing Python is a beast, [the installation of pytest-bdd should be relatively straightforward](https://pytest-bdd.readthedocs.io/en/stable/#install-pytest-bdd). 

### How to Run 

Ideally, you have Visual Studio [code that allows you to set up a launch.json file to run/debug tests](https://code.visualstudio.com/docs/editor/debugging). ou can find the necessary launch.json file in the `resources` folder for this project. 

If you are unwilling to go through the hassle of using Visual Studio, then go through the following steps: 

-   Navigate to the tests folder via the command `cd tests`
-   Then, run the command `pytest <testToRun>`
