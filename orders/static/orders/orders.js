document.addEventListener('DOMContentLoaded', function() {
    $('.topping-select').hide();
    $('#NumberOfToppings').on('change', function(){
        if (this.value === 'ToppingSelection0') {
            $('#ToppingSelection1').hide();
            $('#ToppingSelection2').hide();
            $('#ToppingSelection3').hide();
            $('#ToppingSelection4').hide();
            $('#ToppingSelection5').hide();
        }
        else if (this.value === 'ToppingSelection1') {
            $('#ToppingSelection1').show();
            $('#ToppingSelection2').hide();
            $('#ToppingSelection3').hide();
            $('#ToppingSelection4').hide();
            $('#ToppingSelection5').hide();
        }
        else if (this.value === 'ToppingSelection2') {
            $('#ToppingSelection1').show();
            $('#ToppingSelection2').show();
            $('#ToppingSelection3').hide();
            $('#ToppingSelection4').hide();
            $('#ToppingSelection5').hide();
        }
        else if (this.value === 'ToppingSelection3') {
            $('#ToppingSelection1').show();
            $('#ToppingSelection2').show();
            $('#ToppingSelection3').show();
            $('#ToppingSelection4').hide();
            $('#ToppingSelection5').hide();
        }
        else if (this.value === 'ToppingSelection4') {
            $('#ToppingSelection1').show();
            $('#ToppingSelection2').show();
            $('#ToppingSelection3').show();
            $('#ToppingSelection4').show();
            $('#ToppingSelection5').show();
        }
    });
});