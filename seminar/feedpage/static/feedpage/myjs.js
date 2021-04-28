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
    $(".scroll-up").click(() => {
        $('.mdl-layout__content').scrollTop(0);
    })

    
    
  }
  )

 
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
            console.log(response);
            const str = `
                <div class="toggle-comment last-comment">
                    <p>${response.username}: ${response.content}</p>
                    <form action="/feeds/${fid}/comments/${response.id}/" class="comment-delete" method="POST" data-fid=${fid} data-cid=${response.id} data-csrfmiddlewaretoken=${csrfmiddlewaretoken}>
                    <input type="hidden" name="csrfmiddlewaretoken" value=${csrfmiddlewaretoken}>
                    <button class="mdl-button mdl-js-button mdl-button--icon">
                        <i class="material-icons">clear</i>
                    </button>
                    </form>
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

$(document).on('click', '.feed-like', function(e){
    e.preventDefault();
    const $this = $(e.currentTarget);
    const fid = $this.data('fid');
    const cid = $this.data('cid');
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
            if(response.like_count > 0) {
                console.log('in if');
                const str = `<a href="/feeds/${fid}/comments/${cid}/like/" class="material-icons mdl-badge mdl-badge--overlap toggle-comment-like"  data-badge=${count+1} data-fid=${fid}  data-cid=${cid} data-csrfmiddlewaretoken=${csrfmiddlewaretoken}>
                                <i class="material-icons heart">favorite</i>
                            </a> 
                `;
                $(str).insertBefore($this);
                $this.remove()
                
            } else {
                console.log('in else');
                const str = `<a href="/feeds/${fid}/comments/${cid}/like/" class="material-icons mdl-badge mdl-badge--overlap toggle-comment-like"  data-badge=${count-1} data-fid=${fid}  data-cid=${cid} data-csrfmiddlewaretoken=${csrfmiddlewaretoken}>
                                <i class="material-icons heart">favorite_border</i>
                            </a> 
                `;
                $(str).insertBefore($this);
                $this.remove()
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

$(".toggle-comment-like").click((e) => {
    e.preventDefault();
    const $this = $(e.currentTarget);
    const fid = $this.data('fid');
    const cid = $this.data('cid');
    const csrfmiddlewaretoken = $this.data('csrfmiddlewaretoken');
    $.ajax({
        url: `/feeds/${fid}/comments/${cid}/like/`,
        type: "POST",
        data: {
            cid: cid,
            fid: fid,
            csrfmiddlewaretoken: csrfmiddlewaretoken,
        },
        dataType: "json",
        success: function(response) {
            console.log(response); 
           
            const count = parseInt($this.attr('data-badge'));
            if(response.like_count > 0){
                $this.attr('data-badge', count+1);
                
            } else {
                $this.attr('data-badge' , count-1);
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



$(document).on('submit', '.comment-delete', function(e)  {
    e.preventDefault();
    const $this = $(e.currentTarget);
    const fid = $this.data('fid');
    const cid = $this.data('cid');
    const csrfmiddlewaretoken = $this.data('csrfmiddlewaretoken');

    $.ajax({
        type: 'POST',
        url: `/feeds/${fid}/comments/${cid}/`,
        data: {
            fid: fid,
            csrfmiddlewaretoken: csrfmiddlewaretoken,
        },
        dataType: 'json',
        success: function(response) {
            console.log(response);
            $this.parent().remove(); // 이 부분에서 삭제가 이루어짐 
        },
        error: function(response, status, error) {
            console.log(response, status, error);
        },
        complete: function(response) {
            console.log(response);
        },
    })
})