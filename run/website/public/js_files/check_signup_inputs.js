function checkInputs(username,email,password,repeat_password){

    if(username==""||email==""|| password==""||repeat_password=="") return 0;
    
    else return 1 ;

}

module.exports.checkInputs=checkInputs;