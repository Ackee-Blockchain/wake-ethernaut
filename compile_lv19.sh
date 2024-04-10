#!/bin/bash

wake svm use 0.5.0
wake-solc --bin -o bin 'contracts/lv19_alien_code.sol' \
    contracts/lib/Ownable-05.sol \
    --allow-paths "" --optimize --overwrite
