const express = require('express');
const app = express();
const router = express.Router();
const controller= require('../controllers/control.js');
const  bodyParser= require('body-parser');
app.use(bodyParser.urlencoded({ extended: true }));
var  urlencodedParser=bodyParser.urlencoded({extended: true});
var session = require('express-session')
const multer = require('multer');


var storage = multer.diskStorage({
    destination: function (req, file, cb) {
      cb(null, './uploads/')
    },
    filename: function (req, file, cb) {
        const{originalname}=file;
      cb(null, originalname) 
    }
  })

const upload = multer({storage:storage});

const redirectLogin=(req,res,next)=>{
  if(!req.session.username){
      res.redirect('/');
  }
  else{
      next();
  }
}



const redirectHome=(req,res,next)=>{
  if(req.session.username){
      res.redirect('/home');
  }
  else{
      next();
  }
}


router.get('/recent_scans',redirectLogin,controller.recent_scans);
router.get('/',redirectHome,controller.login);
router.get('/sign_up',redirectHome,controller.sign_up);
router.get('/home',redirectLogin,controller.home);
router.get('/information',redirectLogin,controller.info);
router.post('/sign_up',redirectHome,urlencodedParser,controller.sign_up_post);
router.post('/',redirectHome,urlencodedParser,controller.login_post);
router.post('/logout',redirectLogin,urlencodedParser,controller.logout);
router.post('/home',upload.single('fileUpload'),urlencodedParser,controller.home_post);
router.post('/search',urlencodedParser,controller.search);

module.exports=router;