const { ApolloGateway } = require('@apollo/gateway');
const { ApolloServer } = require('@apollo/server');
const { expressMiddleware } = require('@apollo/server/express4');
const express = require('express');
const path = require('path');
const fs = require('fs');

const gateway = new ApolloGateway({
  serviceList: [
    { name: 'users', url: 'http://localhost:8001/graphql' },
    { name: 'products', url: 'http://localhost:8002/graphql' },
    { name: 'orders', url: 'http://localhost:8003/graphql' },
  ],
});

const app = express();
const server = new ApolloServer({
  gateway,
  subscriptions: false,
});

async function startServer() {
  await server.start();
  app.use('/graphql', express.json(), expressMiddleware(server));
  app.use(express.static(__dirname));
  app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
  });

  app.listen(4000, () => {
    console.log(`Server running at http://localhost:4000`);
    console.log(`GraphQL endpoint: http://localhost:4000/graphql`);
  });
}

startServer().catch(err => {
  console.error('Failed to start server:', err);
});