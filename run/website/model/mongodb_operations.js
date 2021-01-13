const Static_data = require('./static_data.js');
const User = require('./user.js');
const mongoose = require('mongoose');
const mongodb=require('./connection_mongodb.js') 


exports.find_static_data = function (callback) {

    Static_data.find({},(err, data) => {
        
        if (err) callback(err, null)
        else callback(null,data)
    })
    
  }

exports.signup=function(user,callback){
  
    
    User.find({ $or:[{'username': user.username},{'email':user.email}]}, function (err, data_from_database) {

      if (err) callback(err, null);
        let user_data=data_from_database;
        if(user_data.length!=0){
          callback(err, null)
          }
        else{
         
          let new_user = {username:user.username,email:user.email,password:user.password};
          var save_user= new User(new_user);
          save_user.save(function (err, save) {
  
              if (err) return console.error(err);
              console.log( "Saved to database .");
  
              callback(null,save)
            });
        }
    });
  }


exports.findUsername = function (username_info, callback) {
    
    User.find({ username: username_info }, (err, data) => {
  
        if (err) {
            callback(err, null)
        }
        else{
            callback(null,data)
        }
    })
  }



exports.findApp = function (app, callback) {
    
    Static_data.find({app_name:app}, (err, data) => {

        if (err) {
            callback(err, null)
        }
        else{
            callback(null,data)
        }
    })
  }
  

