const express = require("express");
const app = express();
const port = 5050;
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
        message: `Success fetched data for userId : ${req.body.id}`
    });
});