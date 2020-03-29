$(document).ready(function(){
    $('.sidenav').sidenav();


    

  });
  var url = "http://whateverorigin.com/go?url=" + encodeURIComponent("https://www.google.com/search?q=weather") + "&callback=?";

  $.get(url, function(response) {  
    console.log($(response).find("#wob_tci"));
});