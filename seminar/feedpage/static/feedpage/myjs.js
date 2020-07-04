$(document).ready(() => {
    $(".more-comment-btn").on('click', function(event) {
      $(this).toggleClass("showing-comment");
  
      if ($(this).hasClass("showing-comment")) {
        $(this).text("HIDE COMMENTS");
        $(this).parent().children().find(".toggle-comment").not(".last-comment").show();
      } else {
        $(this).text("MORE COMMENTS");
        $(this).parent().children().find(".toggle-comment").not(".last-comment").hide();
      }
    });
})

$(".scroll-up").click(() => {
    $('.mdl-layout__content').scrollTop(0);
})

$('.comment-submit').on('click', function(e) {
    e.preventDefault();
    console.log('form submitted');
    const $this = $(this);
    const fid = $this.data('fid');
    const csrfmiddlewaretoken = $this.data('csrfmiddlewaretoken');

    $.ajax({
        type: 'POST',
        url: `/feeds/${fid}/comments/`, 
        data: { 
            fid: fid,
            csrfmiddlewaretoken: csrfmiddlewaretoken,
            content: $this.siblings('.mdl-textfield__input').val(),
        },
        dataType: 'json',
        success: function(data) { 
            console.log(data);
        const str = `
<div class="toggle-comment last-comment">
  <p>${data.comment.username}: ${data.comment.content}</p>
  <form action="/feeds/${fid}/comments/${data.comment.fid}/" method="POST">
    <input type="hidden" name="csrfmiddlewaretoken" value=${csrfmiddlewaretoken}>
    <button class="mdl-button mdl-js-button mdl-button--icon">
      <i class="material-icons">clear</i>
    </button>
  </form>
</div>
`;
        const $commentBtn = $this.parent().parent().siblings('.more-comment-btn')
        const $commentList = $this.parent().parent().siblings('.comment-list');

        if ($commentBtn.hasClass('showing-comment')) {
            $commentList.children('.last-comment').removeClass('last-comment');
          } else {
            $commentList.children('.last-comment').removeClass('last-comment').hide();
          }

        $commentList.append(str);
        },
        error: function(response, status, error) {
            console.log('fail');
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
