import React from 'react';
import { Link } from 'react-router-dom';

const Footer = () => {
    return (
        <footer className="footer fixed-bottom bg-primary text-light text-center py-3">
            <div className="container">
                <div className="row">
                    <div className="col-lg-4 col-md-6 mb-4">
                        <h4 className="text-light mb-4">Quick Links</h4>
                        <ul className="list-unstyled">
                            <li><Link className="text-light" to="/aboutus">About Us</Link></li>
                            <li><Link className="text-light" to="/policy">Privacy Policy</Link></li>
                            <li><Link className="text-light" to="/policy">Terms & Conditions</Link></li>
                            <li><Link className="text-light" to="/faq">FAQs & Help</Link></li>
                        </ul>
                    </div>
                    <div className="col-lg-4 col-md-6 mb-4">
                        <h4 className="text-light mb-4">Contact</h4>
                        <ul className="list-unstyled">
                            <li><i className="fas fa-map-marker-alt me-2"></i>Bonani, Dhaka, Bangladesh</li>
                            <li><i className="fas fa-phone-alt me-2"></i>+8801981234567</li>
                            <li><i className="fas fa-envelope me-2"></i>learning.edu007@example.com</li>
                        </ul>
                        <div className="mt-3">
                            <a className="btn btn-outline-light btn-social me-2" target='_blank' href="https://twitter.com/home?lang=en"><i className="fab fa-twitter"></i></a>
                            <a className="btn btn-outline-light btn-social me-2" target='_blank' href="https://www.facebook.com/https://www.facebook.com/"><i className="fab fa-facebook-f"></i></a>
                            <a className="btn btn-outline-light btn-social me-2" target='_blank' href="https://www.youtube.com/channel/UCWBZgfmIVxElVuTxsboMGNg"><i className="fab fa-youtube"></i></a>
                            <a className="btn btn-outline-light btn-social" target='_blank' href="https://www.linkedin.com/feed/"><i className="fab fa-linkedin-in"></i></a>
                        </div>
                    </div>
                    <div className="col-lg-4 text-center text-lg-end">
                        <p className="text-muted mb-0">&copy; 2024 <Link className="text-light text-decoration-none" to="/">Edu Learning</Link> | All Rights Reserved</p>
                    </div>
                </div>
            </div>
        </footer>
    );
}

export default Footer;
