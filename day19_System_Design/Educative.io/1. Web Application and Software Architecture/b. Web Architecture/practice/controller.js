exports.getHelloWorld = (req, res) => {
    console.log("Headers: ", req.headers);
    console.log("Method: ", req.method);
    res.send("Hello world from GET Method");
};

exports.postHelloWorld = (req, res) => {
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
};
