const express = require("express");
const app = express();
const port = process.env.PORT || 5050;
app.use(express.json());
app.listen(port, () => {
    console.log(`Server is listening on ${port}`)
})

app.get('/hello', (req, res) => {
    console.log("Headers: ", req.headers);
    console.log("Method: ", req.method);
    res.send("Hello world from GET Method");
});

app.post("/hello", (req, res) => {
    console.log("Headers: ", req.headers);
    console.log("Method: ", req.method);
    console.log("Body: ", req.body);
    res.send({
        status: res.status,
        body: {
            "id": 1,
            "name": "Taslim",
            "age": 22,
            "address": "NPP"
        },
        message: `Successfully fetched data for userId : ${req.body.id}`
    });
});

// const _ = require("lodash");
// const a = [1234, 5322, 1222, 4567, 8996, 3321, 2789]; // ('1234','5322','1222','4567','8996', '3321', '2789')
// const x = `(${_.map(a, ele => `'${ele}'`).join(',')})`;
// console.log(x);
//
// const z = `${_.map(a, ele => `s3o.${ele}`).join(',')}`
// console.log(z)