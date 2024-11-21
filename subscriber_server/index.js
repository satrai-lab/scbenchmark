const express = require("express");
var bodyParser = require("body-parser");
const app = express();
const http = require("http").createServer(app);

// parse application/json
app.use(bodyParser.json());

var bus_position_state = {};

app.post("/hook", (req, res) => {
	// console.log("received something")

	const requestData = req.body;
	console.log(requestData);
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
	return res.status(200).send();
});

http.listen(8888, () => {
	console.log("listening on *:8888");
});
