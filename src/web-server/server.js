const express = require("express");
const bodyParser = require('body-parser');
const path = require('path');

const PORT = 3002;
const app = express();

app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', 'http://localhost:3002'); // Remplacez par votre domaine React
  res.header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE');
  res.header('Access-Control-Allow-Headers', 'Content-Type, Authorization');
  next();
});

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

var current_emotion = "joy"

app.use(express.static(path.resolve(__dirname, './interface-web/build')));

app.post('/emotion', (req, res) => {
  console.log("POST :",req.body.emotion)
  current_emotion = req.body.emotion;
  res.end()
});

app.get('/emotion', (req, res) => {
  res.json({ emotion: current_emotion });
});

app.get('*', (req, res) => {
  res.sendFile(path.resolve(__dirname, './interface-web/build', 'index.html'));
});

app.listen(PORT, () => {
  console.log(`Server listening on ${PORT}`);
});