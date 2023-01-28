const crypto = require("crypto");

const cryptoHash = (...inputs) => {
    const hash = crypto.createHash("sha256");
    hash.update(inputs.sort().join(''))
    return hash.digest("hex")
}

// result= cryptoHash("Hello", "Deepankar")
// console.log(result)
// result= cryptoHash("Hello", "deepankar")
// console.log(result)


module.exports= cryptoHash