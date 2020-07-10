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
});

$(".scroll-up").click(() => {
  $('.mdl-layout__content').scrollTop(0);
});

$(document).on('submit', '.comment-submit', function(e) {
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
            <div class="toggle-comment last-comment cid:${response.cid}">
                <p>↳${response.username}- ${response.content}</p>
                <form action="/feeds/${fid}/comments/${response.cid}/" method="POST" class="comment-delete"
                data-fid='${fid}' data-cid='${response.cid}' data-csrfmiddlewaretoken="${csrfmiddlewaretoken}">
                  <input type="hidden" name="csrfmiddlewaretoken" value=${csrfmiddlewaretoken}>
                  <button type="submit" class="mdl-button mdl-js-button mdl-button--icon">
                    <i class="material-icons">clear</i>
                  </button>
                </form>
                <a  href="/feeds/${fid}/comment_like/${response.cid}/"  class="material-icons mdl-badge mdl-badge--overlap comment-like" 
                  data-badge='${response.like_count}' data-fid= "${fid}" data-cid="${response.cid}"  data-csrfmiddlewaretoken="${csrfmiddlewaretoken}">
                  <i class="material-icons mdl-badge mdl-badge--overlap unlike">favorite_border</i>
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

        /* add "more comment" button */
        if($this.prevAll().length > 1) {
          console.log($commentBtn, "more comment button");
          $commentBtn.removeAttr('style');
          $commentBtn.show();
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


$(document).on('submit', '.comment-delete', function(e) {
  e.preventDefault();
  console.log('comment deleted');
  const $this = $(e.currentTarget);
  const fid = $this.data('fid');
  const cid = $this.data('cid');
  const csrfmiddlewaretoken = $this.data('csrfmiddlewaretoken');

  const $removedComment = $this.parent();
  const $lastComment = $this.parent().siblings().last().prev().prev().prev();
  const $commentBtn = $this.parent().siblings('.more-comment-btn');
  const cmtCount = $lastComment.prevAll().length;
  /* 
    const $lastCommetn = $this.parent().prev();
    const cmtCount = $lastComment.prevAll().length + $currComment.nextAll().length-2;
    // -2를 하는 이유는 last comment와 form element가 nextAll()에 count되기 때문..ㅎㅎ 
    => 이 버전을 사용하지 않는 이유는 앞 뒤로 comment를 더하는 귀찮음 때문 ㅎ
    => $this.parent().siblings().last().prev()는 마지막 comment 의미~~
    => showing button 사용 시에도 delete가 가능하도록 함! 
  */


  $.ajax({
    type: 'POST',
    url: `/feeds/${fid}/comments/${cid}/`, 
    data: { 
      fid: fid,
      cid: cid, 
      csrfmiddlewaretoken: csrfmiddlewaretoken,
    },
    dataType: 'json',

    success: function(response) { 
      console.log(response);
      console.log(cmtCount, "comment count");
      console.log($lastComment, "last comment");
      console.log($commentBtn, "more comment button");

      /* set last Comment */
      $lastComment.addClass('last-comment');
      $lastComment.removeAttr('style');
      $lastComment.show();

      /* delete the target comment */
      $removedComment.remove();

      /* remove "more-comment" button if only one comment left*/
      if(cmtCount < 1) {
        $commentBtn.css('style','display:none');
        $commentBtn.hide();
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

$(document).on('click', '.feed-like', function(e) {
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
            // 요청이 끝난 후 눈에 보이는 값도 변경해주는 것 그래서 +1
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
  });
});

$(document).on('click', '.comment-like', function(e) {
  e.preventDefault();
  const $this = $(e.currentTarget);
  const fid = $this.data('fid');
  const cid = $this.data('cid');
  const csrfmiddlewaretoken = $this.data('csrfmiddlewaretoken');
  $.ajax({
      url: `/feeds/${fid}/comment_like/${cid}/`,
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
            // 요청이 끝난 후 눈에 보이는 값도 변경해주는 것 그래서 +1
            $(`<i class="material-icons mdl-badge mdl-badge--overlap like">favorite</i>`).insertAfter($this.children());
            $this.children('.unlike').remove();
        } else {
            $this.attr('data-badge', count-1);
            $(`<i class="material-icons mdl-badge mdl-badge--overlap unlike">favorite_border</i>`).insertAfter($this.children());
            $this.children('.like').remove();        
        }  
      },
      error: function(response, status, error) {
          console.log(response, status, error);
      },
      complete: function(response) {
          console.log(response);
      }
  });
});