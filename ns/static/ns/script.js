$('.slider_for').slick({
  slidesToShow: 1,
  slidesToScroll: 1,
  arrows: false,
  fade: true,
  asNavFor: '.slider'
});

$(document).ready(function(){
  $('.slider').slick({
        slidesToShow: 3,
        slidesToScroll: 1,
        asNavFor: '.slider_for',
        dots: true,
        centerMode: true,
        focusOnSelect: true
  });
});