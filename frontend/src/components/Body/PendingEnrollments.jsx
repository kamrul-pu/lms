import React, { useEffect, useState } from 'react';
import axios from 'axios';

const base_url = 'http://127.0.0.1:8000/api/v1/courses/enrollments?enrolled=0';

const PendingEnrollments = () => {
    const access_token = localStorage.getItem("access_token");
    const [pendingEnrollments, setPendingEnrollments] = useState([]);
    const [totalAmount, setTotalAmount] = useState(0);

    useEffect(() => {
        fetchPendingEnrollments();
    }, []);

    useEffect(() => {
        // Calculate total amount when pendingEnrollments change
        const calculateTotalAmount = () => {
            let total = 0;
            pendingEnrollments.forEach(enrollment => {
                total += parseFloat(enrollment.course.price);
            });
            setTotalAmount(total);
        };
        calculateTotalAmount();
    }, [pendingEnrollments]);

    const fetchPendingEnrollments = async () => {
        try {
            const response = await axios.get(base_url, {
                headers: {
                    Authorization: `Bearer ${access_token}`
                }
            });
            setPendingEnrollments(response.data.results);
        } catch (error) {
            console.error('Error fetching pending enrollments:', error);
        }
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            const formData = new FormData(event.target);
            const response = await axios.post('http://127.0.0.1:8000/api/v1/payment/checkout', formData, {
                headers: {
                    Authorization: `Bearer ${access_token}`,
                    'Content-Type': 'multipart/form-data'
                }
            });
            window.open(response.data.redirect_url, '_blank');
        } catch (error) {
            console.error('Error submitting form:', error);
        }
    };

    return (
        <div className="container mt-4">
            <div className="row">
                <div className="col-lg-4 mt-5">
                    <h2>Checkout Form</h2>
                    <form onSubmit={handleSubmit}>
                        <div className="mb-3 row">
                            <label htmlFor="phone" className="col-sm-3 col-form-label">Phone</label>
                            <div className="col-sm-9">
                                <input type="text" className="form-control" id="phone" name="phone" required />
                            </div>
                        </div>
                        <div className="mb-3 row">
                            <label htmlFor="city" className="col-sm-3 col-form-label">City</label>
                            <div className="col-sm-9">
                                <input type="text" className="form-control" id="city" name="city" required />
                            </div>
                        </div>
                        <div className="mb-3 row">
                            <label htmlFor="address" className="col-sm-3 col-form-label">Address</label>
                            <div className="col-sm-9">
                                <input type="text" className="form-control" id="address" name="address" required />
                            </div>
                        </div>
                        <button type="submit" className="btn btn-primary btn-lg">Submit</button>
                    </form>
                </div>
                <div className="col-lg-8 mt-5 mt-lg-0">
                    <h2>Pending Enrollments</h2>
                    <table className="table table-striped">
                        <thead>
                            <tr>
                                <th>SL</th>
                                <th>Course</th>
                                <th>Price</th>
                                <th>Discounted Amount</th>
                                <th>Discounted Price</th>
                            </tr>
                        </thead>
                        <tbody>
                            {pendingEnrollments.map((enrollment, index) => (
                                <tr key={enrollment.id}>
                                    <td>{index + 1}</td>
                                    <td>{enrollment.course.name}</td>
                                    <td>{enrollment.course.price}</td>
                                    <td>{parseFloat(enrollment.course.price) * parseFloat(enrollment.course.discount_percentage) / 100}</td>
                                    <td>{enrollment.course.total_price}</td>
                                </tr>
                            ))}
                            <tr>
                                <td colSpan="3"></td>
                                <td>Total:</td>
                                <td>{totalAmount}</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    );
}

export default PendingEnrollments;
