let variable1;

for (var x = 1; x < 96; x++) {
    let cloned_element = $(".sunbed").first().clone();
    cloned_element.attr("id", "clon_" + x);
    cloned_element.find(".sunbed_name").html(x);

    $(".beach_wrapper").append(cloned_element);
}

$("#clon_1,#clon_2,#clon_3,#sunbed").addClass('especiales');
$("#clon_10,#clon_11,#clon_22,#clon_23,#clon_34,#clon_35,#clon_46,#clon_47,#clon_58,#clon_59,#clon_70,#clon_71").addClass('desconectados');
$("#clon_72,#clon_73,#clon_74,#clon_75,#clon_76,#clon_77,#clon_78,#clon_79,#clon_80,#clon_81,#clon_82,#clon_83,#clon_84,#clon_85,#clon_86,#clon_87,#clon_88,#clon_89,#clon_90,#clon_91,#clon_92,#clon_93,#clon_94,#clon_95").addClass('primerafila');


//Clicking function
function handle_shopping_cart_amount(amount) {
    shopping_cart = shopping_cart + amount;
    localStorage.setItem('shopping_cart', shopping_cart);
    SunbedController.update_prices();
}

function reset_shopping_cart_amount() {
    shopping_cart = 0;
    localStorage.setItem('shopping_cart', 0);
    SunbedController.update_prices();
}


function enviarcesta() {
    var actual_value = localStorage.getItem('shopping_cart');
    total_sold = parseInt(total_sold) + parseInt(actual_value);

    console.log(actual_value);
    $("#totalcesta").html(total_sold);
    reset_shopping_cart_amount();
    SunbedController.update_prices();
}


function handle_cart_to_total_sold() {
    total_sold = total_sold + shopping_cart;
    reset_shopping_cart_amount();
    SunbedController.update_prices();
}


//clear localstorage
function clearClick(number) {
    localStorage.clear();
    window.location.reload();
}


var SunbedController = function() {
    return {
        init: function() {
            this.bind_listeners();
            this.restore_customers_name();
            this.restore_sunbeds_colors();
            this.retreive_prices();
            this.restore_comments();
        },

        bind_listeners: function() {
            $("input.customer_name").keyup(function () {
                var text = $(this).val();
                var target_id = $(this).closest(".sunbed").attr('id');
                let target_key = 'customer_name' + target_id;
                localStorage.setItem(target_key, text);
            });

            $("#comments").keyup(function() {
               let actual_value = $(this).val();
               localStorage.setItem('comments', actual_value);
            });

            //bucle de colores
            $('.toggle').dblclick(function () {
                let arr_steps = [1, 2, 3, 4, 5, 6],
                    step = parseInt($(this).data('actual-step')) || 0,
                    nuevo_step = (step === arr_steps.length) ? 1 : step + 1;

                $(this).removeClass('step' + step);
                $(this).addClass('step' + nuevo_step);
                $(this).data('actual-step', nuevo_step);

                let actual_id = $(this).attr('id'),
                    target_key = 'sunbed_color' + actual_id;

                localStorage.setItem(target_key, nuevo_step);
            });
        },

        restore_customers_name: function() {
            $("input.customer_name").each(function () {
                let actual_id = $(this).closest(".sunbed").attr('id');
                let target_key = 'customer_name' + actual_id;

                let target_value = localStorage.getItem(target_key);

                if (target_value) {
                    $(this).val(target_value);
                }
            });
        },

        restore_sunbeds_colors: function() {
            $(".sunbed").each(function() {
                let actual_id = $(this).attr('id'),
                    target_key = 'sunbed_color' + actual_id;

                let target_step = localStorage.getItem(target_key);
                if (target_step) {
                    $(this).addClass('step' + target_step);
                    $(this).data('actual-step', target_step);
                }
            });
        },

        retreive_prices: function() {
            shopping_cart = 0;
            total_sold = 0;

            var saved_total = localStorage.getItem('total_sold');
            if (saved_total) {
                total_sold = parseInt(saved_total);
            }

            var saved_shopping_cart = localStorage.getItem('shopping_cart');
            if (saved_shopping_cart) {
                shopping_cart = parseInt(saved_shopping_cart);
            }

            this.update_prices();
        },

        update_prices: function() {
            $("#shopping_cat_value").html(shopping_cart);
            $("#total_price_value").html(total_sold);
        },

        reset_local_storage_except_customers: function () {           
            Object.keys(localStorage).forEach(function (local_key) {
                if (local_key.indexOf('customer_name') === -1) {
                    localStorage.removeItem(local_key);
                }
            });

            window.location.reload();
        },

        restore_comments: function () {
            var old_comments = localStorage.getItem('comments');
            if (old_comments) {
                $("#comments").val(old_comments);
            }
        }
    };
}();

SunbedController.init();

//exportar 

function exportHistory() {  
    console.log("started"); 
    var _myArray = JSON.stringify(localStorage , null, 4); //indentation in json format, human readable


    //Note: We use the anchor tag here instead button.
    var vLink = document.getElementById('exportHistoryLink');

    var vBlob = new Blob([_myArray], {type: "octet/stream"});
    vName = 'working_history_' + todayDate() + '.json';
    vUrl = window.URL.createObjectURL(vBlob);
    console.log(vLink);

    vLink.setAttribute('href', vUrl);
    vLink.setAttribute('download', vName );

    //Note: Programmatically click the link to download the file
    vLink.click();

    console.log("finished");    
}
