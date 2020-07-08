$(document).ready(() => {
    $(".more-comment-btn").on('click', function(event) {
      $(this).toggleClass("showing-comment");
  
      if ($(this).hasClass("showing-comment")) {
        $(this).text("HIDE COMMENTS");
        $(this).parent().find(".toggle-comment").not(".last-comment").show();
      } else {
        $(this).text("MORE COMMENTS");
        $(this).parent().find(".toggle-comment").not(".last-comment").hide();
      }
    });
  }
)

$(".scroll-up").click(() => {
    $('.mdl-layout__content').scrollTop(0);
})

$('.comment-submit').submit((e) => {
    e.preventDefault();//이거 없으면 context에 들어있는 것들이 뜬다. 주석 처리하고 댓글 달면 확인 가능
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
            console.log(response);
            const str = `
                <div class="toggle-comment last-comment ${response.id}">
                    <p>${response.username}: ${response.content}</p>
                    <form action="/feeds/${fid}/comments/${response.id}/" method="POST">
                        <input type="hidden" name="csrfmiddlewaretoken" value=${csrfmiddlewaretoken}>
                        <a href="/feeds/${ fid }/comments/${ response.id }/delete/" class="comment-delete">
                            <i class="material-icons" style="color:black">clear</i>
                        </a>
                        <a href= "/feeds/${ fid }/comments/${ response.id }/like/" class="material-icons mdl-badge mdl-badge--overlap comment-like" data-badge="{{ c.like_users.count }}" data-fid={{ feed.id }} data-cid={{c.id}} data-csrfmiddlewaretoken="{{ csrf_token }}">
                            <i class="fas fa-heart" style="color:red"></i>
                        </a> 
                    </form>
                  <br/>
                </div>
            `;

            const $commentBtn = $this.siblings('.more-comment-btn');
            const $lastComment = $this.siblings('.last-comment');

            if ($commentBtn.hasClass('showing-comment')) {
                $lastComment.removeClass('last-comment');
            } else {
                $lastComment.removeClass('last-comment').hide();
            }

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

$(".feed-like").click((e) => {
    e.preventDefault();
    const $this = $(e.currentTarget);
    const fid = $this.data('fid');
    const csrfmiddlewaretoken = $this.data('csrfmiddlewaretoken');
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
            if(response.like_count > 0) {// view와는 작동 로직이 다르다. 요청이 끝나고 나서라고 생각
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

$(".comment-like").click((e) => {
    e.preventDefault();
    const $this = $(e.currentTarget);
    const fid = $this.data('fid');
    const cid = $this.data('cid');
    const csrfmiddlewaretoken = $this.data('csrfmiddlewaretoken');
    $.ajax({
        url: `/feeds/${fid}/comments/${cid}/like/`,
        type: "POST",
        data: {
            fid: fid,
            cid: cid,
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
            console.log(data-badge);
        },
        error: function(response, status, error) {
            console.log(response, status, error);
        },
        complete: function(response) {
            console.log(response);
        }
    })
});

$(".comment-delete").click((e) => {
    e.preventDefault();
    const $this = $(e.currentTarget);
    const fid = $this.data('fid');
    const cid = $this.data('cid');

    console.log($this);

    const csrfmiddlewaretoken = $this.data('csrfmiddlewaretoken');
    const last_comment=$this.closest('div');

    console.log(last_comment)

    $.ajax({
        url: `/feeds/${fid}/comments/${cid}/delete/`,
        type: "POST",
        data: {
            fid: fid,
            cid: cid,
            csrfmiddlewaretoken: csrfmiddlewaretoken,
        },
        dataType: "json",
        success: function(response) {
            console.log(response);
            if ($(this).hasClass('last-comment')){
                $(last_comment).remove();
            }else{
                $(last_comment).remove();
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
