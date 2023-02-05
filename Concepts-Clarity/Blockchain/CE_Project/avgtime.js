const BlockChain= require('./blockchain')
const blockchain= new BlockChain()

blockchain.addBlock({data: 'new data'})
// console.log(blockchain.chain[blockchain.chain.length -1])

let prevTimestamp, nextTimestamp, nextBlock, timeDifference, averageTime

const times= []

for (let i = 0; i<1000; i++) {
    prevTimestamp= blockchain.chain[blockchain.chain.length - 1].timestamp
    blockchain.addBlock({data: `block ${i}`})
    nextBlock= blockchain.chain[blockchain.chain.length -1]
    nextTimestamp= nextBlock.timestamp
    
    timeDifference= nextTimestamp- prevTimestamp
    times.push(timeDifference)

    averageTime= times.reduce((total, num)=> (total+num))/times.length

    
    console.log(
                `Time to mine block: ${timeDifference}ms, \tDifficulty: ${nextBlock.difficulty},\t\tAverage Time: ${averageTime} ms`
            )
        


}