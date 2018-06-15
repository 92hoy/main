$( document ).ready(function() {
  $( ".login100-form-btn" ).click(function() {
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
      else{
        alert("error");
      }
    });
  });
});
