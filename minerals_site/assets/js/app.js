function filter_group()
        {
           document.write('hi there')
            current=document.getElementById("group_choice_field");
            if(current.value!="-1")
            $.ajax({
                    type: 'POST',
                    url: 'minerals:filter_group_minerals',
                    data: document.getElementsByName("group_choice_field")
                })
        }
        
