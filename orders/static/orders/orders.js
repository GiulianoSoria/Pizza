document.addEventListener('DOMContentLoaded', () => {
    $("#RegularPizzaModalButton1").on('click', function(e) {
        e.preventDefault();
        $('#RegularPizzaModal1').modal('show');
    });
    $("#RegularPizzaModalButton2").on('click', function(e) {
        e.preventDefault();
        $('#RegularPizzaModal2').modal('show');
    });
    $("#RegularPizzaModalButton3").on('click', function(e) {
        e.preventDefault();
        $('#RegularPizzaModal3').modal('show');
    });
    $("#RegularPizzaModalButton4").on('click', function(e) {
        e.preventDefault();
        $('#RegularPizzaModal4').modal('show');
    });
    $("#RegularPizzaModalButton5").on('click', function(e) {
        e.preventDefault();
        $('#RegularPizzaModal5').modal('show');
    });

    // $('#RegularPizzaPriceSmall').hide();
    $('#RegularPizzaPriceLarge1').hide();
    $('#RegularPizzaPriceLarge2').hide();
    $('#RegularPizzaPriceLarge3').hide();
    $('#RegularPizzaPriceLarge4').hide();
    $('#RegularPizzaPriceLarge5').hide();

    $('#RegularPizzaSizeSelection1').on('change', function() {
        
        if (this.value === 'S') {
            $('#RegularPizzaPriceSmall1').show();
            $('#RegularPizzaPriceLarge1').hide();
        }
        else if (this.value === 'L') {
            $('#RegularPizzaPriceSmall1').hide();
            $('#RegularPizzaPriceLarge1').show();
        }
    });
    $('#RegularPizzaSizeSelection2').on('change', function() {
        
        if (this.value === 'S') {
            $('#RegularPizzaPriceSmall2').show();
            $('#RegularPizzaPriceLarge2').hide();
        }
        else if (this.value === 'L') {
            $('#RegularPizzaPriceSmall2').hide();
            $('#RegularPizzaPriceLarge2').show();
        }
    });
    $('#RegularPizzaSizeSelection3').on('change', function() {
        
        if (this.value === 'S') {
            $('#RegularPizzaPriceSmall3').show();
            $('#RegularPizzaPriceLarge3').hide();
        }
        else if (this.value === 'L') {
            $('#RegularPizzaPriceSmall3').hide();
            $('#RegularPizzaPriceLarge3').show();
        }
    });
    $('#RegularPizzaSizeSelection4').on('change', function() {
        
        if (this.value === 'S') {
            $('#RegularPizzaPriceSmall4').show();
            $('#RegularPizzaPriceLarge4').hide();
        }
        else if (this.value === 'L') {
            $('#RegularPizzaPriceSmall4').hide();
            $('#RegularPizzaPriceLarge4').show();
        }
    });
    $('#RegularPizzaSizeSelection5').on('change', function() {
        
        if (this.value === 'S') {
            $('#RegularPizzaPriceSmall5').show();
            $('#RegularPizzaPriceLarge5').hide();
        }
        else if (this.value === 'L') {
            $('#RegularPizzaPriceSmall5').hide();
            $('#RegularPizzaPriceLarge5').show();
        }
    });

});