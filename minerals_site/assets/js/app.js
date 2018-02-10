
// using jQuery
function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });



$(document).ready(function() {
        $("#id_group_choice_field").change(function () { 
                var vGroupItem = document.getElementById('id_group_choice_field');
                var vGroupItemText = vGroupItem.options[vGroupItem.selectedIndex].innerHTML;    
                alert(vGroupItemText + " ajax")
                var form = $(this).closest("form");
                $.ajax({
               
                        url: form.attr("action"), // the endpoint
                        type : "GET", // http method
                        data: {'group': vGroupItemText}, // data sent via GET
                        dataType: 'json',
                        success : function(data) {
                                console.log(data); // log the returned json to the console
                                console.log("success"); // another sanity check
                        },

                        // handle a non-successful response
                        error : function(xhr,errmsg,err) {
                                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                        }
                });        
        });
});
