(function($){
  $(function(){

    $('.sidenav').sidenav();
    $('.parallax').parallax();

  }); // end of document ready
})(jQuery); // end of jQuery name space


$(document).ready(function(event){
  $(document).on('click', '#like', function(event){
    event.preventDefault();
    let pk = $(this).attr('value');
    $.ajax({
      type: 'POST',
      url: '{% url "like_event" %}',
      data: {'id': pk, 'csrfmiddlewaretoken':'{{csrf_token}}'},
      dataType: 'json',
      success: function(response){
        console.log($('#like-section').html(response['form']));
      },
      error: function(rs,e){
        console.log(rs.responseText);
      }
    })
  });
});
