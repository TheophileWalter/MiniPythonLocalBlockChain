#!/bin/bash

# check if "nodes" folder exists
# if so, it's removed
[ -d nodes ] && rm -rf nodes

randomStringOld=""
randomStringNew=""

# create template architecture
_create_template () {

    fileName=${1}
    
    mkdir -p nodes/nodes_1/${fileName}s/
    
    for j in {1..4}; do
        randomStringNew=$(openssl rand -hex 8)
        [ -z ${randomStringOld} ] && randomStringOld=${randomStringNew}

        filePath=nodes/nodes_1/${fileName}s/${j}.${randomStringNew}

        # create file content
        _create_content ${fileName} ${filePath} ${randomStringOld} ${randomStringNew} ${j}

        randomStringOld=${randomStringNew}
    done

    mkdir ./nodes/nodes_1/accounts
}

# create right file content
_create_content () {

    fileName=${1}
    filePath=${2}
    randomStringOld=${3}
    randomStringNew=${4}
    j=$((${5}-1))

    case "${fileName}" in
    block)
        echo "previous ${j}.${randomStringOld}"     >> ${filePath}
        echo "miner mbc-blockchains-master-1-isd"   >> ${filePath}
        echo "pow 16"                               >> ${filePath}
        echo "date Mon-Jun-18--07:33:57--+00-2018"  >> ${filePath}
        echo "nonce 19984"                          >> ${filePath}
        echo "transactions "                        >> ${filePath}
        ;;
    transaction)
        echo "from ${j}.${randomStringOld}"         >> ${filePath}
        echo "to ${j}.${randomStringNew}"           >> ${filePath}
        echo "amount $(echo $RANDOM) units"         >> ${filePath}
        echo "fees $(echo $RANDOM) units"           >> ${filePath}
        ;;
    pendingTransaction)
        echo "from ${j}.${randomStringNew}"         >> ${filePath}
        echo "to ${j}.${randomStringOld}"           >> ${filePath}
        echo "amount $(echo $RANDOM) units"         >> ${filePath}
        echo "fees $(echo $RANDOM) units"           >> ${filePath}
        ;;
    *)
        echo ""                                     >> ${filePath}
        ;;
    esac

    
}

# main function
_main () {

    _create_template block
    _create_template transaction
    _create_template pendingTransaction

    cp -R ./nodes/nodes_1 ./nodes/nodes_2
    cp -R ./nodes/nodes_1 ./nodes/nodes_3
    cp -R ./nodes/nodes_1 ./nodes/nodes_4

}

_main