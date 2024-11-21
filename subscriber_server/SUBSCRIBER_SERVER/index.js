const express = require("express");
var bodyParser = require("body-parser");
const app = express();
const http = require("http").createServer(app);
const io = require("socket.io")(http);

// parse application/json
app.use(bodyParser.json());

var bus_position_state = {};

app.post("/hook_bus", (req, res) => {
	// console.log("received something")

	const requestData = req.body;
	//console.log(requestData);
	io.emit("Observation::bus::update", requestData);
	return res.status(200).send();
});

app.post("/hook_station", (req, res) => {
	// console.log("received something")

	const requestData = req.body;
	//console.log(requestData);
	const targetStation = requestData.data[0].id;
	//console.log(targetStation)
	if (
		targetStation ===
		"urn:ngsild:Observation_Occupancy_S1_station415"
	) {
		const now = new Date();
		console.log(now);
	}
	io.emit("Observation::station::update", requestData);
	return res.status(200).send();
});

app.get("/bus_position_state", (req, res) => {
	return res.status(200).send(bus_position_state);
});

app.post("/hook_position", (req, res) => {
	const requestData = req.body;
	if(bus_position_state[requestData.id] === undefined){
		bus_position_state[requestData.id] = {}
	}
	bus_position_state[requestData.id] = req.body;
	// Update bus position state
	//
	io.emit("BusPosition::update", requestData);
	return res.status(200).send();
});

io.on("connection", (socket) => {
	console.log("a user connected");
});

http.listen(8888, () => {
	console.log("listening on *:8888");
});
