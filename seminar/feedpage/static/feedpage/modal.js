$('#signup-form').submit((event) => {
  event.preventDefault()
  $.ajax({
      url: '/accounts/signup/',
      method: 'POST',
      dataType: 'json',
      data: {
          csrfmiddlewaretoken: $(event.currentTarget).data('csrfmiddlewaretoken'),
          username: $(`input#username`).val(),
          email: $(`input#email`).val(),
          password1: $(`input#password1`).val(),
          password2: $(`input#password2`).val(),
          college: $(`input#college`).val(),
          major: $(`input#major`).val()
      },
      success(response) {
          console.log(response)
          window.location.href='/feeds/'
      },
      error(response, status, error) {
          console.log(response, status, error)
      }
  })

  
})


$('#login-form').submit((event) => {
  event.preventDefault()
  $.ajax({
      url: '/accounts/login/?next{{request.path}}',
      method: 'POST',
      data: {
          login: $(`input#login-username`).val(),
          password: $(`input#password`).val(),
          csrfmiddlewaretoken: $(event.currentTarget).data('csrfmiddlewaretoken')
      },
      dataType: "json",
      success(res) {
          console.log(res)
          window.location.href='/feeds/'
      },
      error(response, status, error) {
          console.log(response, status, error)
      }
  })
})


$('#feed-create').submit((event) => {
  event.preventDefault() 
  
  // await에 의해서 뒤에 오는 함수는 차례를 기다힌다-> 비동기 처리 
  // 여기서는 await 없어도 지금은 괜춘 ㅎㅅㅎ 
  $.ajax({
    url: '/feeds/',  // feed create을 POST 받는 url과, view함수는 "/feeds/"였습니다. 
    method: 'POST',
    data: {  // 요청(request)로 함께 보낼 데이터 정의
      title: $(`input#title`).val(),
      content: $(`textarea#content`).val(),
      csrfmiddlewaretoken: $(event.currentTarget).data('csrfmiddlewaretoken')   // 장고 security와 관련해서 아무나 feed를 생성하지 못하도록 form 액션을 할 때는, csrf_token이 필요
    },
    dataType: "json",  // json => "javascript object notation"
    success(response) {
      console.log(response)
      window.location.href = '/feeds/'   //** redirect
    },
    error(response, status, error) {
      console.log(response, status, error);
    }
  })
})