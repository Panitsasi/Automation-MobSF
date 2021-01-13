const mongoose = require('mongoose');
require('dotenv').config()

db=mongoose.connect(process.env.CLOUD, {
    useNewUrlParser: true, 
    useUnifiedTopology: true  
  }).then(() => {console.log('MongoDB Connected' )}).catch(err => console.log(err));

  module.exports = db;