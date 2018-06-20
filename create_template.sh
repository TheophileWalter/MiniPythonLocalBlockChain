#!/bin/bash

# check if "nodes" folder exists
# if so, it's removed
[ -d nodes ] && rm -rf nodes

# create template architecture
_create_template () {
    
    for i in {1..4}; do
        mkdir -p nodes/nodes_${i}/${1}s/
        
        for j in {1..4}; do
            touch nodes/nodes_${i}/${1}s/${1}_${j}
        done
    done
}

# main function
_main () {

    _create_template block
    _create_template transaction
    _create_template pendingTransaction
    _create_template account

}

_main