const model = require('../model/mongodb_operations.js');
const express=require('express')
const exphbs = require('express-handlebars');
var session = require('express-session')
const app = express()
const  bodyParser= require('body-parser');
const bcrypt = require('bcrypt');
const handlebars = require('handlebars');
var SecureInputs = require('../public/js_files/check_signup_inputs.js')
var SecurePasswords = require('../public/js_files/check_signup_passwords.js')



exports.recent_scans = function (req, res) {

    try{

        var username = req.session.username;
        model.find_static_data(function(err,data){    
          
            if(err) res.send(err);
            if(data!=null){
                res.render('recent_scans',{data:data,username:username})

            }
        });
    }

    catch(err){
        res.send(err);
    }
}


exports.login = function (req, res) {

    try{
        res.render('login')
    }

    catch(err){
        res.send(err);
    }
}



exports.login_post = function (req, res) {

    try{

        var user={};
        model.findUsername(req.body.username,function(err,data){
    
            if(err) res.send(err);
            if(data.length!=0){
                user=data[0];   
        
                bcrypt.compare(req.body.password, user.password, function(err, response) {
                    if(response) {
                        req.session.username=req.body.username;
                        let message=[{"message":""}];
                        res.render('home',{data:message,username:req.body.username});
                    } 
                    else{
                        res.render('login_with_errors')
                    }
                });
           }

           else {
                res.render('login_with_errors')
           }
        });

    }

    catch(err){
        res.send(err);
    }
    
}


exports.sign_up = function (req, res) {

    try{
        res.render('sign_up')
    }

    catch(err){
        res.send(err);
    }
}


exports.sign_up_post = function (req, res) {

    try{
            if(!(SecurePasswords.checkSamePassword(req.body.password,req.body.repeat_password)) || !(SecureInputs.checkInputs(req.body.username,req.body.email,req.body.password,req.body.repeat_password))){
                res.render('sign_up_with_errors')
            }
            else{

                let personal_info_user ={}
                personal_info_user.username=req.body.username;
                personal_info_user.email=req.body.email;
                personal_info_user.password = bcrypt.hashSync(req.body.password, 10);
              
                model.signup(personal_info_user,function(err,data_from_database){
    
                        if(err) res.send(err);
                        if(data_from_database==null){
                            res.render('sign_up_with_errors') 
                        }
                        else{
                            res.render('login')  
                        }
                }); 
            }

       }

    catch(err){

            res.send(err);
    }
}


exports.home = function (req, res) {

    try{
        let username = req.session.username;
        
        let message=[{"message":""}];
        res.render('home',{data:message , username:username})

    }

    catch(err){
        res.send(err);
    }
}



exports.home_post= function (req, res) {
  
  if(req.file){

        try{
            let message=[{"message":"The transfer was successful!"}];
            res.render('home',{data:message,username:req.session.username});
        }
        catch(err){
            res.send(err);
        }
  }

  else { 
         try{

            let message=[{"message":"The transfer failed!"}];
            let username = req.session.username;
            res.render('home',{data:message,username:username});
         }
         catch(err){

            res.send(err);

         }

      }
  
}



exports.info = function (req, res) {

    try{
        let username = req.session.username;
        res.render('information',{username:username})
    }

    catch(err){
        res.send(err);
    }
}



exports.logout = function (req, res) {

    try{
        req.session.destroy(err=>{
            if(err) return res.redirect('/home')
            res.clearCookie('Cookie')
            res.redirect('/')
        });

    }

    catch(err){
        res.send(err);
    }
}


exports.search = function (req, res) {

        try{
                var username = req.session.username;
                model.findApp(req.body.searchbox,function(err,data){
                    
                    if(err) res.send(err);
                    if(data.length==0){
                        res.render('search_error',{username:username})
                    }
                    else{
                        res.render('recent_scans',{data:data,username:username})

                    }
                }); 

        }
    
        catch(err){
            res.send(err);
        }

}

