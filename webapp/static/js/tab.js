//This enabled Smooth-Scroll via Click
$(".navbar a").on('click', function(event){
  // Prevent default anchor click behavior
  event.preventDefault();
  var hash = this.hash;
//Uses Animate to Allow the Smooth Scrolling
  $('html, body').animate({
    scrollTop: $(hash).offset().top
  }, 500, function(){
    window.location.hash = hash;
  });
});
//End-SmoothScroll Script
//WIP Modifying thumbnail hover
  $('.thumbnail').hover(
        function(){
            $(this).find('.caption').animate({opacity: 0.7}, 400); 
        },
        function(){
            $(this).find('.caption').animate({opacity: 0}, 400); 
        }
    );
//Enable #.active move when clicked
$(".nav a").on("click", function(){
   $(".nav").find(".active").removeClass("active");
   $(this).parent().addClass("active");
});
//End .active move script
//Twitter Script
!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+"://platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");
//End of Twitter Script