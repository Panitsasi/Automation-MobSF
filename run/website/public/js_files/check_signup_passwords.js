function checkSamePassword(password,repeat_password){

    var str = 0 ;
    var num = 0 ;
    var types = ['number','string']
  
    if(password!==repeat_password){
      return 0 ;
    }
  
    if (password.length<7){
      return 0;
    }
  
    
    for (let i =0 ; i <password.length;i++){
     
          var integer =parseInt(password[i]);
          var string =password[i];
          if(!isNaN(integer)) num++ ;
          else str++ ;
    }
     if (num==0 || str==0){

      return 0 ;
      
     }
  
     return 1 ;
  }

  module.exports.checkSamePassword=checkSamePassword;


