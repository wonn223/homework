//$():wrapper?,factory?// 
$(document).ready(function() {
  //css선택자를 그대로 쓴다.li 배열이 담겨 있다. 
  var menu = $('.main-menu > li');
  var span = $('.main-menu span');
  var sub_menu = $('.sub-menu li:last-child a');
  var mainMenu = $('.main-menu > li > span')
  console.log(mainMenu);
  menu.hover(function() {
    // 예약어는 묶지 않는다. submenu 안 모든 구x 조를 찾는다. 메소드를 연결한다는 뜻의 메소드 체인 
    $(this).find('.sub-menu').toggleClass('sub-menu-active');
  });
  span.focusin(function() {
    //siblings에 인자 없으면 모든 형제요소가 선택됨.
    $(this).siblings('.sub-menu').addClass('sub-menu-active');
  })
  sub_menu.focusout(function() {
    //sub-menu클래스 삭제 parents도 가능.
    $(this).parents('.sub-menu').removeClass('sub-menu-active');
  })

  mainMenu.focusout(function() {
    //
    $(this).siblings().removeClass('sub-menu-active');
  })

});