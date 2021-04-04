 $(document).ready(function(){
    $('.sidenav').sidenav({edge:'right'});
    $('.slider').slider({ fullWidth: true});
    $(".copyright").text(new Date().getFullYear())
    $('select').formSelect();

  });

// Close flash message

   function close_flash_message(){  
        document.all.alertmessage.style.display='none';
        return false;  
        }  