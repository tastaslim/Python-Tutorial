const express = require("express");
const app = express();
const router = require("./route");
const port = process.env.PORT || 5050;
app.use(express.json());
app.use(router);
app.listen(port, () => {
    console.log(`Server is listening on ${port}`)
});
