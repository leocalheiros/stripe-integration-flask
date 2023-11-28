const button = document.querySelector('#buy_now_btn');

button.addEventListener('click', event => {
    fetch('/stripe_pay')
        .then(result => result.json())
        .then(data => {
            var stripe = Stripe(data.checkout_public_key);
            stripe.redirectToCheckout({
                sessionId: data.checkout_session_id
            }).then(result => {
                // Handle any errors during redirection
            });
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
});
