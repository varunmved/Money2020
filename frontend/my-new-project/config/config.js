var development = {
  firebase: {
    rootRefUrl: "https://baemoney2020.firebaseio.com",
    serverUID: "bae",
    secretKey: ""
  }
};

var test = {
  firebase: {
    rootRefUrl: "https://baemoney2020.firebaseio.com",
    serverUID: "bae",
    secretKey: ""
  }
};

var production = {
  firebase: {
    rootRefUrl: process.env.FB_URL,
    serverUID: process.env.FB_SERVER_UID, 
    secretKey: process.env.FB_SECRET_KEY
  }
};

var config = {
  development: development,
  test: test,
  production: production,
};
module.exports = config;