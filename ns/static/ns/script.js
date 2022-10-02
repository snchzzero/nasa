$('.slider_for').slick({
  slidesToShow: 1,
  slidesToScroll: 1,
  arrows: false, // arrows - показ стрелки
  fade: true,
  asNavFor: '.slider'
});

//$(document).ready(function(){
//  $('.slider').slick({
//        arrows: true,
//        slidesToShow: 5,
//        slidesToScroll: 1,
//        asNavFor: '.slider_for',
//        dots: true,
//        centerMode: true,
//        focusOnSelect: true
//  });
//});
$(document).ready(function(){
  $('.slider').slick({
  centerMode: true,
  centerPadding: '60px',  //'60px'
  slidesToShow: 5,
  asNavFor: '.slider_for',
  responsive: [
    {
      breakpoint: 768, //768
      settings: {
        arrows: false,
        centerMode: false,
        centerPadding: '40px',
        slidesToShow: 5
      }
    },
    {
      breakpoint: 480, //480
      settings: {
        arrows: false,
        centerMode: false,
        centerPadding: '40px', //'40px'
        slidesToShow: 1
      }
    }
  ]
  });
});
