import React, { useEffect } from 'react';
import { useLocation } from 'react-router-dom';
import axios from 'axios';

const PaymentSuccess = () => {
    const location = useLocation();

    useEffect(() => {
        const successData = location.state; // Assuming SSLCommerz redirects with state data
        console.log("success data", successData);
        if (successData) {
            // Make POST request to your backend with success data
            axios.post('http://localhost:8000/api/v1/payment/success', successData)
                .then(response => {
                    console.log('Transaction details:', response.data);
                    // Handle success response from backend if needed
                })
                .catch(error => {
                    console.error('Error posting success data to backend:', error);
                    // Handle error if needed
                });
        }
    }, [location]);

    return (
        <div>
            <h2>Payment Success</h2>
            {/* You can add additional UI elements here */}
        </div>
    );
}

export default PaymentSuccess;
