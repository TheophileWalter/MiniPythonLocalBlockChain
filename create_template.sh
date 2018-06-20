#!/bin/bash

# check if "nodes" folder exists
# if so, it's removed
[ -d nodes ] && rm -rf nodes

randomStringOld=""
randomStringNew=""

# create template architecture
_create_template () {
    
    for i in {1..4}; do
        mkdir -p nodes/nodes_${i}/${1}s/
        
        for j in {1..4}; do
            randomStringNew=$(openssl rand -hex 8)
            [ -z ${randomStringOld} ] && randomStringOld=${randomStringNew}

            filePath=nodes/nodes_${i}/${1}s/${j}.${randomStringNew}
            
            echo "previous ${j}.${randomStringOld}"     >> ${filePath}
            echo "miner mbc-blockchains-master-1-isd"   >> ${filePath}
            echo "pow 16"                               >> ${filePath}
            echo "date Mon-Jun-18--07:33:57--+00-2018"  >> ${filePath}
            echo "nonce 19984"                          >> ${filePath}
            echo "transactions"                         >> ${filePath}

            randomStringOld=${randomStringNew}
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