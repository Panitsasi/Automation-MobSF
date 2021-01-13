
$(document).ready(function(){
    $("input.upload-apk").change(function () {
      $("p.file-info").text(this.files.length +" file selected!");
    });
  });