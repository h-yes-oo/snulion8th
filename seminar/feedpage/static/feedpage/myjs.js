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
    e.preventDefault();
    console.log('form submitted');
    const $this = $(e.currentTarget);
    const fid = $this.data('fid');
    const cid = $this.data('cid');
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
                    <form action="/feeds/${fid}/comments/${response.id}/" method="POST">
                    <input type="hidden" name="csrfmiddlewaretoken" value=${csrfmiddlewaretoken}>
                    <a href="/feeds/${fid}/comments/${response.id}/clike/" class="comment-like" data-fid=${fid} data-cid=${response.id} data-csrfmiddlewaretoken="${csrfmiddlewaretoken}" > ${response.like_count} likes </a> 
                    <a href="/feeds/${fid}/comments/${response.id}/" class="comment-delete" data-fid=${fid} data-cid=${response.id} data-csrfmiddlewaretoken="${csrfmiddlewaretoken}" >
                    <button class="mdl-button mdl-js-button mdl-button--icon">
                        <i class="material-icons">clear</i>
                    </button>
                    </a>
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


            const count = parseInt($this.attr('data-badge'));
                if(response.like_count > 0) {
                    $this.attr('data-badge', count+1);
                    // response.like_count--;
                } else {
                    $this.attr('data-badge', count-1);
                    // response.like_count++;
                }  
            
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

$(".comment-like").click((e) => {
    e.preventDefault();
    const $this = $(e.currentTarget);
    const fid = $this.data('fid');
    const cid = $this.data('cid');
    const csrfmiddlewaretoken = $this.data('csrfmiddlewaretoken');
    $.ajax({
        url: `/feeds/${fid}/comments/${cid}/clike/`,
        type: "POST",
        data: {
            fid: fid,
            cid: cid,
            csrfmiddlewaretoken: csrfmiddlewaretoken,
        },
        dataType: "json",
        success: function(response) {
            console.log(response);
        const count = parseInt($this.attr('data-like'));
        if(response.like_count > 0) {
            $this.attr('data-like', count+1);

            $(`#${fid}and${cid}`).remove();
            const string = `<div id="${fid}and${cid}"> ${count+1} likes </div> `;
            $(string).prependTo($this);

        } else {
            $this.attr('data-like', count-1);
            
            $(`#${fid}and${cid}`).remove();
            const string = `<div id="${fid}and${cid}"> ${count-1} likes </div> `;
            $(string).prependTo($this);
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

$(".comment-delete").click((e) => {
    e.preventDefault();
    const $this = $(e.currentTarget);
    const fid = $this.data('fid');
    const cid = $this.data('cid');
    const csrfmiddlewaretoken = $this.data('csrfmiddlewaretoken');
    $.ajax({
        url: `/feeds/${fid}/comments/${cid}/`,
        type: "POST",
        data: {
            fid: fid,
            cid: cid,
            csrfmiddlewaretoken: csrfmiddlewaretoken,
        },
        dataType: "json",
        success: function(response) {
            console.log(response); 
            $(`#${cid}`).remove();
        },
        error: function(response, status, error) {
            console.log(response, status, error);
        },
        complete: function(response) {
            console.log(response);
        }
    })
});
