const express = require("express");
const app = express();
const fs = require("fs");
app.use(express.json());
const port = process.env.PORT || 5050;
const hashTable = {};

//////////////////////// MEMORY /////////////////////////////
app.post('/memory/:key', (req, res) => {
    hashTable[req.params.key] = req.body.data;
    res.send();
});

app.get('/memory/:key', (req, res) => {
    const ans = hashTable[req.params.key];
    if (ans) res.send(ans);
    else res.send('null');
});

//////////////////////// DISK //////////////////////////////
app.post('/disk/:key', (req, res) => {
    try {
        fs.writeFileSync(`data/${req.params.key}`, req.body.data)
        res.send();
    } catch (err) {
        console.log(err);
        res.send(err);
    }
});

app.get('/disk/:key', (req, res) => {
    try {
        const ans = fs.readFileSync(`data/${req.params.key}`);
        res.send(ans);
    } catch (err) {
        console.log(err);
        res.send('null');
    }
});


app.listen(port, () => {
    console.log(`Server is listening on ${port}`);
})

/* STEPS to follow
1. Create above 4 endpoints
2. create a data folder
3. RUN these 4 commands in same order:
 a. curl --header 'content-type:application/json' http://localhost:5050/memory/foo --data '{"data":"This is data in memory"}'
 b. curl http://localhost:5050/memory/foo  ==> Should give: This is data in memory
 c. curl --header 'content-type:application/json' http://localhost:5050/disk/foo --data '{"data":"This is data in disk"}'
 d. curl http://localhost:5050/disk/foo  ==> Should give: This is data in disk

 --- Now restart the server, and again query get for memory and disk: Changes of memory will be gone while disk changes will be there.
*/


//
// const ids = [1, 2, 3, 4, 5]
// const arr = [{
//     "A": 12,
//     "id": 1,
//     "name": "Account"
// },
//     {
//         "A": 112,
//         "id": 2,
//         "name": "Account"
//     },
//     {
//         "A": 29,
//         "id": 3,
//         "name": "Account"
//     },
//     {
//         "A": 41,
//         "id": 4,
//         "name": "Account"
//     },
//     {
//         "A": 32,
//         "id": 5,
//         "name": "Account"
//     }]
// const _ = require("lodash")
// _.each(ids, id => {
//     const count = _.filter(arr, a => a.id === id);
//     console.log(count);
// });
