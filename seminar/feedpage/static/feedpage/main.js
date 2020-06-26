// 추가(jquery-scrollup)
$(".scroll-up").click(() => {
    $('.mdl-layout__content').scrollTop(0);
    // console.log('up');
})

// 추가(ajax-feedlike)
$(".feed-like").click((e) => {
    e.preventDefault();
    const $this = $(e.currentTarget);
    const fid = $this.data('fid');
    const csrfmiddlewaretoken = $this.data('csrfmiddlewaretoken');
    // console.log(count);
    $.ajax({
        url: `/feeds/${fid}/like/`,
        type: "POST",
        data: {
            fid: fid,
            csrfmiddlewaretoken: csrfmiddlewaretoken,
        },
        dataType: "json",
        success: function(response) {
            console.log(response);
            const count = parseInt($this.attr('data-badge'));
            if(response.like_count > 0) {
                $this.attr('data-badge', count+1);
            } else {
                $this.attr('data-badge', count-1);
            }  
        },
        error: function(response, status, error) {
            console.log(response, status, error);
        },
        complete: function(response) {
            console.log(response);
        }
    })
});

// 추가(ajax-commentsubmit)
$('.comment-submit').submit((e) => {
    e.preventDefault();
    console.log('form submitted');
    const $this = $(e.currentTarget);
    const fid = $this.data('fid');
    const csrfmiddlewaretoken = $this.data('csrfmiddlewaretoken');

    $.ajax({
        type: 'POST',
        url: `/feeds/${fid}/comments/`, 
        data: { 
            fid: fid,
            csrfmiddlewaretoken: csrfmiddlewaretoken,
            content: $(`input#${fid}[name=content]`).val(),
        },
        dataType: 'json',
        success: function(response) { 
            console.log(response.content);
            const str = `
                <p>${response.content}</p>
                <form action="/feeds/${fid}/comments/${response.id}/" method="POST">
                    <input type="hidden" name="csrfmiddlewaretoken" value=${csrfmiddlewaretoken}>
                    <button class="mdl-button mdl-js-button mdl-button--icon">
                    <i class="material-icons">clear</i>
                    </button>
                </form>
                <br />
            `

            $(str).insertBefore($this);
            $(`input#${fid}[name=content]`).val('');
        },
        error: function(response, status, error) {
            console.log(response, status, error);
        },
        complete: function(response) {
            console.log(response);
        },
    });
});