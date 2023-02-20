const Block= require('./block')
const cryptoHash = require('./crypto-hash')

class BlockChain{
    constructor(){
        this.chain= [Block.genesis()]
    }

    // to add the block in the chain 
    addBlock({data}){
        const newBlock= Block.mineBlock({
                        prevBlock: this.chain[this.chain.length -1],
                        data: data
                    })
        this.chain.push(newBlock)
    }

    replaceChain(chain){
        if (chain<=this.chain.length){
            console.error('The incoming chain is not longer. ')
            return
        }
        if (!BlockChain.isValidChain(chain)){
            console.error('The incoming chain is not a valid chain. ')
            return
        }
        this.chain= chain
    }


    // check validity of a block
    static isValidChain(chain){
        if (JSON.stringify(chain[0])!==JSON.stringify(Block.genesis())){
            return false
        }
        for(let i=1; i<chain.length; i++){
            const {timestamp, prevHash, hash, nonce, difficulty, data}= chain[i]
            const lastDifficulty= chain[i-1].difficulty
            // console.log(chain[i])
            // console.log('timestamp: ', timestamp)
            // console.log('prevhash: ', prevHash)
            // console.log('hash: ', hash)
            // console.log('data: ', data)
            
            const actual_last_hash= chain[i-1].hash
            if (prevHash!==actual_last_hash){
                // console.log("prevhash: ", prevHash)
                // console.log("actual_last_hash: ", actual_last_hash)
                return false
            }
            const validated_hash = cryptoHash(timestamp, prevHash, nonce, difficulty, data)
                if (hash!==validated_hash){
                    // console.log("hash: ", hash)
                    // console.log('validated_hash: ', validated_hash)
                    return false
                }
                
                if (Math.abs(lastDifficulty-difficulty)>1) {
                    return false
                }
        }
        return true
    }
}




// creating the blockchain
const blockchain= new BlockChain
blockchain.addBlock({data: 'This is block 1'})
blockchain.addBlock({data: 'This is block 2'})
// console.log(blockchain)

const result= BlockChain.isValidChain(blockchain.chain)
// console.log("Valid Blockchain? ", result)


module.exports= BlockChain