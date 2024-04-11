#!/bin/bash

wake svm use 0.5.0
wake-solc --bin -o bin 'AlienCodex.old-sol' \
    Ownable-05.old-sol \
    --allow-paths "" --optimize --overwrite
