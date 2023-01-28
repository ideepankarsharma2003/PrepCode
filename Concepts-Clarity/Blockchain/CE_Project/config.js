const INITIAL_DIFFICULTY= 2
const MINE_RATE= 1000 // in milliseconds(1 sec)

const GENESIS_DATA= {
    timestamp: 1, 
    prevHash: '0x000',
    hash: '01234abcd',
    difficulty: INITIAL_DIFFICULTY,
    nonce: 0,
    data: []
};

module.exports= {GENESIS_DATA, MINE_RATE};