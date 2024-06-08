import React, { useEffect } from 'react';
import axios from 'axios';

const PaymentCancelled = () => {
    useEffect(() => {
        // Make any necessary POST requests or handle post cancellation actions here
    }, []);

    return (
        <div className="container mt-4">
            <div className="alert alert-warning" role="alert">
                <h4 className="alert-heading">Payment Cancelled</h4>
                <p>Your payment has been cancelled. If you have any questions or concerns, please contact support for assistance.</p>
            </div>
        </div>
    );
}

export default PaymentCancelled;
