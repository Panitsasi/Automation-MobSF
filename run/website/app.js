const express = require('express');
const Router = require('./routes/domains.js');
const exphbs = require('express-handlebars');
require('dotenv').config()
const mongoose = require('mongoose');
const app = express();
var session = require('express-session')
const MongoStore = require('connect-mongo')(session);


const dbOptions ={
  useNewUrlParser: true, 
  useUnifiedTopology: true  
}

const connection = mongoose.createConnection(process.env.CLOUD,dbOptions);

const sessionStore = new MongoStore({
  mongooseConnection: connection,
  collection: 'sessions'
});


app.use(session({
  name:'Cookie',
  secret: process.env.SECRET_KEY,
  resave: false,
  saveUnitialized: true,
  store: sessionStore,
  cookie: {
    maxAge: 1000 * 60 * 60  
  }
}));


app.engine('hbs', exphbs({
  defaultLayout: 'main',
  extname: '.hbs',
  runtimeOptions:{
    allowProtoPropertiesByDefault:true,
    allowProtoMethodsByDefault:true

  }
}));

app.use(express.static('public'))

app.set('view engine', 'hbs');

app.use('/',Router);

app.listen(process.env.PORT || 8080,()=>{console.log('Server Started at port:'+process.env.PORT) });