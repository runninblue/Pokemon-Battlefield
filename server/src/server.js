const express = require('express');
const dotenv = require('dotenv');
const app = express();
const routes = require('./routes');
dotenv.config({ path: `${__dirname}/.env` });
const PORT = process.env.PORT || 5000;

/* Initializing express app */
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use('/', routes);

app.listen(PORT, () => {
    /* Server initialization */
    console.log(`Server running on port ${PORT}`);
});