 $(document).ready(function(){
    $('.sidenav').sidenav({edge:'right'});
    $('.slider').slider({ fullWidth: true});
    $(".copyright").text(new Date().getFullYear())
  });