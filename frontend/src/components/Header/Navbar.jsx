import React from 'react';
import { Link } from 'react-router-dom';

const Header = () => {
    return (
        <header>
            <nav className="navbar navbar-expand-lg navbar-light bg-light">
                <div className="container">
                    <Link className="navbar-brand" to="/">Edu Learning</Link>
                    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                        <span className="navbar-toggler-icon"></span>
                    </button>
                    <div className="collapse navbar-collapse" id="navbarNav">
                        <ul className="navbar-nav ms-auto">
                            <li className="nav-item">
                                <Link className="nav-link active" to="/">Home</Link>
                            </li>
                            <li className="nav-item">
                                <Link className="nav-link" to="/category">Category</Link>
                            </li>
                            <li className="nav-item">
                                <Link className="nav-link" to="/all-courses">Courses</Link>
                            </li>
                            <li className="nav-item">
                                <Link className="nav-link" to="/teacher-login">Teacher</Link>
                            </li>
                            <li className="nav-item">
                                <Link className="nav-link" to="/user-login">Student</Link>
                            </li>
                            <li className="nav-item">
                                <Link className="nav-link" to="/pending-enrollment">Pending (0)</Link>
                            </li>
                            <li className="nav-item">
                                <a className="nav-link" href="http://localhost:8000/admin/login/?next=/admin/" target="_blank" rel="noopener noreferrer">Admin</a>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
        </header>
    );
}

export default Header;
