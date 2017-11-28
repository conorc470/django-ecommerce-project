$(function() {
    $("#payment-form").submit(function() {
      var form = this;
      var card = {
        number:   $("#id_credit_card_number").val(),
        expMonth: $("#id_expiry_month").val(),
        expYear:  $("#id_expiry_year").val(),
        cvc:      $("#id_cvv").val()
      };


    Stripe.createToken(card, function(status, response) {
        if (status === 200) {
          $("#credit-card-errors").hide();
          $("#id_stripe_id").val(response.id);
          
          // Prevent the Credit Card Details from being submitted to our server.
          $("#id_credit_card_number").removeAttr('name');
          $("#id_cvv").removeAttr('name');
          $("#id_cvv").removeAttr('name');
          $("#id_expiry_month").removeAttr('name');
          $("#id_expiry_year").removeAttr('name');

          form.submit();
        } else {
          $("#stripe-error-message").text(response.error.message);
          $("#credit-card-errors").show();
          $("#validate_card_btn").attr("disabled", false);
        }
    });
    return false;
  });
});