const WebSocket = require('isomorphic-ws');
const { connect } = require('nats.ws');

// Connect to the NATS server over WebSocket
const nc = connect({
  url: 'ws://localhost:4222',
  WebSocket: WebSocket,
  onConnect: () => {
    console.log('Connected to NATS server via WebSocket');

    // Subscribe to the topic
    const subscription = nc.subscribe('client.odds.live.*', { callback: handleMessage });

    // Event handler for subscription messages
    function handleMessage(msg) {
      console.log('Received message:', msg.subject, msg.data);
      // Process the message here
    }

    // Event handler for subscription errors
    subscription.on('error', (err) => {
      console.error('Subscription error:', err);
    });
  },
  onError: (err) => {
    console.error('NATS error:', err);
  }
});
