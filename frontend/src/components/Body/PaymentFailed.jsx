// import React, { useEffect } from 'react';
// import axios from 'axios';

// const PaymentFailed = () => {
//     useEffect(() => {
//         // Make any necessary POST requests or handle post failure actions here
//     }, []);

//     return (
//         <div className="container mt-4">
//             <div className="alert alert-danger" role="alert">
//                 <h4 className="alert-heading">Payment Failed</h4>
//                 <p>Unfortunately, your payment could not be processed. Please try again later or contact support for assistance.</p>
//             </div>
//         </div>
//     );
// }

// export default PaymentFailed;


import React, { useEffect } from 'react';
import { useLocation } from 'react-router-dom';
import axios from 'axios';

const PaymentFailed = () => {
    const location = useLocation();

    useEffect(() => {
        const postData = location.state; // Assuming SSLCommerz sends data in location state
        console.log('Data from SSLCommerz:', postData);

        // Process the data or send it to your backend
        // For example, you can make a POST request to your backend with the received data
        axios.post('http://localhost:8000/api/v1/payment-failed', postData)
            .then(response => {
                console.log('Response from backend:', response.data);
                // Handle response if needed
            })
            .catch(error => {
                console.error('Error posting data to backend:', error);
                // Handle error if needed
            });
    }, [location]);

    return (
        <div>
            <h2>Payment Failed</h2>
            {/* Add any UI elements you need */}
        </div>
    );
}

export default PaymentFailed;
