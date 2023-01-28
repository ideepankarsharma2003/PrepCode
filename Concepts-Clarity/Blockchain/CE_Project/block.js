const { GENESIS_DATA, MINE_RATE } = require("./config");
const cryptoHash= require('./crypto-hash')

class Block{
    constructor({ timestamp, prevHash, hash, nonce, difficulty, data }){
        this.timestamp= timestamp;
        this.prevHash=prevHash;
        this.hash= hash;
        this.data= data;
        this.nonce= nonce
        this.difficulty= difficulty
    }

    static genesis(){
        return new this(GENESIS_DATA);
    }

    static mineBlock({prevBlock, data}){
        // const timestamp= Date.now()
        let hash, timestamp;
        const prevHash= prevBlock.hash
        // const {difficulty}= prevBlock;
        let {difficulty}= prevBlock

        let nonce= 0;
        do{
            nonce++
            timestamp=Date.now()
            difficulty= Block.adjustDifficulty({originalBlock:prevBlock, timestamp:timestamp})
            hash= cryptoHash(timestamp, prevHash, data, nonce, difficulty)
        }while(hash.substring(0, difficulty)!=='0'.repeat(difficulty))

        return new this({
            timestamp: timestamp,
            prevHash: prevHash,
            data: data,
            hash: hash,
            difficulty: difficulty,
            nonce: nonce
        })
    }


    static adjustDifficulty({originalBlock, timestamp}){
        const {difficulty}= originalBlock
        if(difficulty<1) return 1
        const difference= timestamp-originalBlock.timestamp
        if (difference>MINE_RATE) return difficulty-1
        return difficulty+1
    }
}

/*

const genesis_block= Block.genesis();
console.log(genesis_block);


const block1= new Block({
                hash:"01x2c",
                prevHash: "12xcv",
                timestamp: "2/09/2023",
                data: "This is the data"
            });
// console.log(block1);

const result= Block.mineBlock({
                prevBlock:block1,
                data: "This is block 2"
            })
// console.log(result)


*/


module.exports= Block