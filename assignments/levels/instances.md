Greetings, trainee! This level is designed to walk you through the very basics of how to play this game.


## 1. Set up the environment

If you don't have it already - install the essential tools for this repository - Wake framework and Python. There are more possible ways how to install these, which you can find at [Wake docs/installation](https://ackeeblockchain.com/wake/docs/latest/installation/).

Not only for Ethernaut but also for Solidity development, we recommend using [VS Code](https://code.visualstudio.com/) with extension [Tools for Solidity (Wake)](https://marketplace.visualstudio.com/items?itemName=AckeeBlockchain.tools-for-solidity). This extension installs Wake automatically (most of the time). Since Wake is a testing framework based on [pytest](https://docs.pytest.org/en) this [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) will be useful as well.


## 2. Compile the project

If you successfully installed Wake and Python, you will be able to run:
```bash
wake compile pytypes
```

This command compiles all the solidity files (= level and helper files) and generates pytypes which are solidity smart contracts handles for the Wake framework.

On some levels, you will need to write your solidity smart contract(s). Put these inside the `contracts/attacker/` directory and run the compile again. If you are forgetting about this or want to save some work, you can set up auto compile in the current console window using:
```bash
wake compile pytypes -w
```


## 3. Levels organization

Each level has its test file inside the directory `tests/`. In every file, there are two functions:

1. `test_lvXX()`
    - is run by wake automatically, because it starts with `test_`.
    - does just 3 things: deploys the level contracts, calls the exploit method, and checks the solution.

2. `exploit_lvXX(...)`
    - is your playground for your exploit or in other words, solution for a given level.


## 4. Solving levels

To solve levels, you need to write Python code that will interact with contracts deployed in a given level.

Sometimes, as mentioned in "2. Compile the project", you will need to write some solidity smart contracts too. Their pytypes handles must be imported into the test file to allow you to interact with them.

You will need this first in level 3, so feel free to return here later.

For example for the mentioned level 3:

If you write your custom `FlipOracle` smart contract in file `contracts/attacker/flip_oracle.sol` you can import it inside the `lv03_coinflip_test.py` using this code:

```python
from pytypes.contracts.attacker.flip_oracle import FlipOracle 
```


## 5. Rules

To get the most out of this game and learn something, you should follow these rules:

1. Write your Python code only inside `exploit_lvXX(...)` functions or in your own function(s) you call from here.
2. Do not change the code inside `test_lvXX()` functions.
3. Do not change the code inside the `contracts/` folder excluding the `contracts/attacker/` folder, but feel free to look at any code in this directory.
4. Do not change the code inside `ethernaut_deployer.py`. If you want to make the game easier or you don't know what to do (based on the assignment), take a look in `ethernaut_deployer.py` on how is the given level deployed and checked.
5. Do not break the deployment configuration or check the configuration in any other way.
6. First try to exploit the level on your own, since this way, you will learn most but ...
7. If you struggle for a long time with a particular level, you can find a solution on the branch [solution](https://github.com/Ackee-Blockchain/wake-ethernaut/tree/solution/tests). Also, you can find online a lot of recipes and hints on how to solve the Ethernaut levels.


## 6. Run the first test

After compiling the project, run the first test with:

```bash
wake test tests/lv00_hello_test.py
```

This test should fail since the file contains no solution (yet) to the first level.


## 7. Interact with the contract to complete the level

Look into the result of what `contract.info()` printed (before the test failure) and follow the instructions.

You should have all you need to complete the level within the contract.


## 8. Verifying the solutions

When you know you have completed a level, re-run the level's test. If your solution is correct, the test will end up passing, otherwise will end with a failure in the form of `AssertionError` and a short explanation of what you need to do.


## GL and HF with hacking B^)

(Scroll up, the first one is long :)
