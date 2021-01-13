const mongoose = require('mongoose');

const static_data = new mongoose.Schema({
  
  version: {
    type: String,
    
  },

  file_name: {
    type: String,
  },

  app_name: {
    type: String
  },

  size: {
    type: String
  },

  md5: {
    type: String,
  },
  
  sha1: {
    type: String
      
  },
  sha256:{
    type: String
  },

  main_activity: {
    type: String
      
  },


  target_sdk: {
    type: String
      
  },
  max_sdk: {
    type: String
      
  },
  min_sdk: {
    type: String
      
  },
  version_name: {
    type: String
      
  },
  version_code: {
    type: String
      
  },
 
  average_cvss: {
    type: String
      
  },
  security_score: {
    type: String
      
  },
  virus_total: {
    type: String
      
  },

  trackers: {
    type: Object
      
  },

  exported_count: {
    type: Object
      
  },

  day: {
    type: String
      
  },
  time: {
    type: String
      
  },

  static_report: {
    type: String
      
  },
  dynamic_report: {
    type: String
      
  }


},
{collection: "static_data"}
);

const Static_data = mongoose.model("Static_data", static_data);
module.exports = Static_data;