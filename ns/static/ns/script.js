$('.slider_for').slick({
  slidesToShow: 1,
  slidesToScroll: 1,
  arrows: false, // arrows - показ стрелки
  fade: true,
  asNavFor: '.slider'
});

$('.slider').slick({
  infinite: true,
  slidesToShow: 5,
  slidesToScroll: 1,
  centerMode: true,
  asNavFor: '.slider_for',
  nextArrow: '.arrow_next',
  prevArrow: '.arrow_prev',
});
