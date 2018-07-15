$( document ).ready(function() {

  $("input[name=idBox]").keydown(function (key) {
    if(key.keyCode == 13){
        loginClick();
    }
  });

  $("input[name=pwBox]").keydown(function (key) {
    if(key.keyCode == 13){
        loginClick();
    }
  });

  login();

  function login(){
    $( ".login100-form-btn" ).click(function() {
      loginClick();
    });
  }

  function loginClick(){
    var inputId = $('#inputId').val();
    var inputPw = $('#inputPw').val();
    var hidden_csrftoken = $('.hidden_csrftoken').text();

    console.log("inputId = ", inputId);
    console.log("inputPw = ", inputPw);
    console.log("hidden_csrftoken = ", hidden_csrftoken);

    $.post( "/login", {
      inputId: inputId,
      inputPw: inputPw,
      csrfmiddlewaretoken: hidden_csrftoken
    })
    .done(function( data ) {
      if(data.result == 'success'){
        $(location).attr('href', '/')
      }
      else if(data.result == 'error0'){
        $('.info').show();
        $('.info').text('아이디와 비밀번호를 입력해주세요');
      }
      else if(data.result == 'error1'){
        $('.info').show();
        $('.info').text('아이디가 존재하지 않습니다');
      }
      else if(data.result == 'error2'){
        $('.info').show();
        $('.info').text('비밀번호가 일치하지 않습니다');
      }
      else if(data.result == 'invalidLicense'){
        $('.info').show();
        $('.info').text('라이센스가 유효하지 않습니다');
      }
      else{
        alert("알 수 없는 오류");
      }
    });
  }
});
