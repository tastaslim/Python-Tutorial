const express = require("express");
const router = express.Router();
const controller = require("./controller");
router.get('/hello', controller.getHelloWorld);
router.post("/hello", controller.postHelloWorld);
module.exports = router;