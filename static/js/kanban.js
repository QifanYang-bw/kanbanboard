$( function() {
    var dragItem, dragTarget;
    $( "#todo, #doing, #done, #remove" ).sortable({
        items: '.card',
        connectWith: ".section",
        placeholder: "placeholder myPlaceholder",
        greedy: true,
        over: function( event, ui ) {
            $(this).addClass("droppable");
        },
        out: function( event, ui ) {
            $(this).removeClass("droppable");
        },
        receive: function( event, ui ) {
            dragItem = ui.item.attr("id");
            dragTarget = this.id;
            if (this.id != 'remove') {
                $.ajax({
                    url: '/updatestat',
                    data: {
                        'card_id': dragItem, 
                        'section': dragTarget
                    },
                    type: 'POST',
                    success: function(response) {
                        console.log(response);
                    },
                    error: function(error) {
                        console.log(error);
                    }
                });
            } else {
                $.ajax({
                    url: '/remove',
                    data: {'card_id': dragItem},
                    type: 'POST',
                    success: function(response) {
                        $("#" + dragItem).fadeOut(function(){
                            $("#" + dragItem).remove();
                        });
                        console.log(response);
                    },
                    error: function(error) {
                        console.log(error);
                    }
                });
            }
        },
    }).disableSelection();

    // Can't submit form here since it would result in name and
    // value being separately inserted.
    // e.g. [{'name': 'todoitem', 'value': 'test'}]
    $("#add_item").submit(function(e){
        e.preventDefault();
        $.ajax({
            url: '/add',
            type: 'POST',
            data: $("#add_item").serialize(),
            success: function(data) {
                console.log(data);
                $('#' + data.session).append(
                    "<div id=\'" + 
                    data.card_id +
                    "\' class=\'card\'>" +
                    data.text +
                    "</div>"
                );
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
} );