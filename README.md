# Ethernaut in Wake

To run this repository, you need to install [Wake](https://ackeeblockchain.com/wake/docs/latest/installation/) framework.

## What is Ethernaut?

The Ethernaut is a Web3/Solidity based wargame inspired by [overthewire.org](https://overthewire.org/wargames/), played in the Ethereum Virtual Machine. Each level is a smart contract that needs to be 'hacked'.

Original source of this game can be found on [ethernaut.openzeppelin.com](https://ethernaut.openzeppelin.com) website.

## What is wake?

Wake is a Python-based Solidity development and testing framework with built-in vulnerability detectors and printers.

You can get more information about Wake on [getwake.io](https://getwake.io/) website.

## How to run?

To compile this repository do:
```bash
wake compile
```

To turn on autocompile in current window do:
```bash
wake compile -w
```

To run individual level (for example level-0) do:

```bash
wake test tests/i00_test.py
```

To run all levels in this repository do:

```bash
wake test
```

For more information, refer to the original [Wake documentation](https://ackeeblockchain.com/wake/docs/latest/testing-framework/overview/).
