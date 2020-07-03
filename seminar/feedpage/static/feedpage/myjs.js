$(document).ready(() => {
    $(".more-comment-btn").on('click', function (event) {
        $(this).toggleClass("showing-comment");

        if ($(this).hasClass("showing-comment")) {
            $(this).text("Hide");
            $(this).parent().find(".toggle-comment").not(".last-comment").show();
        } else {
            $(this).text("Load more");
            $(this).parent().find(".toggle-comment").not(".last-comment").hide();
        }
    });
}
)

$('.scroll-up').on('click', function (event) {
    $('.mdl-layout__content').scrollTop(0);
});

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
        success: function (response) {
            console.log(response);
            console.log(`This is count like!!! : ${response.like_count}`);
            const str = `
                <div class="toggle-comment last-comment cid-${response.id}">
                    <p>${response.username}: ${response.content}</p>
                    <form action="/feeds/${fid}/comments/${response.id}/" method="POST" class='cmt-delete' data-fid='${ fid }' data-cid='${response.id}' data-csrfmiddlewaretoken="${csrfmiddlewaretoken}">
                    <input type="hidden" name="csrfmiddlewaretoken" value=${csrfmiddlewaretoken}>
                        <button type ='submit' class="mdl-button mdl-js-button mdl-button--icon" data-upgraded=",MaterialButton">
                            <i class="material-icons">clear</i>
                        </button>
                    </form>
                    <a  href="/feeds/${fid}/comments/${response.id}/like/"  class="material-icons comment-like" data-badge='${ response.like_count }' data-fid= "${ fid }" data-cid="${ response.id }"  data-csrfmiddlewaretoken="${csrfmiddlewaretoken}">
                        <i  class="material-icons cmt-unfavorite">favorite_border</i>
                    </a>
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
        error: function (response, status, error) {
            console.log(response, status, error);
        },
        complete: function (response) {
            console.log(response);
        },
    });
});

$(".feed-like").click((e) => {
    e.preventDefault();
    const dom = e.target
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
        success: function (response) {
            console.log(response);
            const count = parseInt($this.attr('data-badge'));
            if (response.like_count > 0) {
                $this.attr('data-badge', count + 1);
            } else {
                $this.attr('data-badge', count - 1);
            }
        },
        error: function (response, status, error) {
            console.log(response, status, error);
        },
        complete: function (response) {
            console.log(response);
        }
    })
});

$('.comment-like').click((e) => {
    e.preventDefault();
    const $this = $(e.currentTarget);
    const fid = $this.data('fid');
    const cid = $this.data('cid');
    const csrfmiddlewaretoken = $this.data('csrfmiddlewaretoken');

    $.ajax({
        url: `/feeds/${fid}/comments/${cid}/like/`,
        type: 'POST',
        data: {
            fid: fid,
            cid: cid,
            csrfmiddlewaretoken: csrfmiddlewaretoken,
        },
        dataType: 'json',

        success: function (response) {
            console.log(response);
            const count = parseInt($this.attr('data-badge'));
            const select1 = $this.children('.cmt-favorite');
            const select2 = $this.children('.cmt-unfavorite');
            const str1 =`
            <i  class="material-icons cmt-favorite">favorite</i>
            `;
            const str2 =`
            <i  class="material-icons cmt-unfavorite">favorite_border</i>
            `

            if (response.like_count > 0) {
                $this.attr('data-badge', count + 1);
                $(str1).insertAfter($this.children());
                select2.remove();
            } else {
                $this.attr('data-badge', count - 1);
                $(str2).insertAfter($this.children());
                select1.remove();
            }
        },

        error: function (response, status, error) {
            console.log(response, status, error);
        },

        complete: function (response) {
            console.log(response)
        }

    });
});

$('.cmt-delete').submit((e) => {
    e.preventDefault();
    const $this = $(e.currentTarget);
    const fid = $this.data('fid');
    const cid = $this.data('cid');
    const csrfmiddlewaretoken = $this.data('csrfmiddlewaretoken');


    $.ajax({
        url: `/feeds/${fid}/comments/${cid}/`,
        type: 'POST',
        data: {
            fid: fid,
            cid: cid,
            csrfmiddlewaretoken: csrfmiddlewaretoken,
        },
        dataType: 'json',

        success: function(response) {
            console.log(response); 
            const $lastComment = $this.parent();
            const cid2 = response.cid2;
            console.log($lastComment.siblings(`.cid-${cid2}`))

            if($lastComment.hasClass('last-comment')){
                $lastComment.siblings(`.cid-${cid2}`).addClass('last-comment')
                $lastComment.siblings(`.cid-${cid2}`).removeAttr('style')
                $lastComment.remove();
            } else {
                $lastComment.remove();
            }
        },

        error: function(response, status, error) {
            console.log(response, status, error);
        },

        complete: function(response) {
            console.log(response);
        },
        
    })
})