$('#feed-create').submit((event) => {
    event.preventDefault();

    $.ajax({
        url: '/feeds/',
        method: 'POST',
        data: {
            title: $(`input#title`).val(),
            content: $(`textarea#content`).val(),
            csrfmiddlewaretoken: $(event.currentTarget).data('csrfmiddlewaretoken')
        },
        dataType: "json", 
        success(response) {
            console.log(response);
            window.location.href = '/feeds/'
        },
        error(response, status, error) {
            console.log(response, status, error);
            console.log('error 오류가 나요');
        }
    })
})

$('#signup-form').submit((event) => {
    event.preventDefault();

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
            major: $(`input#major`).val(),
        },
        success(response) {
            console.log(response);
            window.location.href = "/feeds/"
        },
        error(response, status, error) {
            console.log(response, status, error)
        }
    })
})

// $('#login-form').submit((event) => {
//     event.preventDefault();

//     $.ajax({
//         url:
//     })
// })

