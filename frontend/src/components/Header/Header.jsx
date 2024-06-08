import React from 'react';
import { Link } from 'react-router-dom';

const Header = () => {
    const teacherLoginStatus = localStorage.getItem('teacherLoginStatus');
    const studentLoginStatus = localStorage.getItem('studentLoginStatus');

    return (
        <header>
            <nav className="navbar navbar-expand-lg navbar-light bg-light">
                <div className="container-fluid">
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
                                <Link className="nav-link" to="/courses">Courses</Link>
                            </li>
                            <li className="nav-item dropdown">
                                <a className="nav-link dropdown-toggle" href="#" id="teacherDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                                    Teacher
                                </a>
                                <ul className="dropdown-menu" aria-labelledby="teacherDropdown">
                                    {teacherLoginStatus !== 'true' ? (
                                        <>
                                            <li><Link className="dropdown-item" to="/teacher-login">Login</Link></li>
                                            <li><Link className="dropdown-item" to="/teacher-register">Register</Link></li>
                                        </>
                                    ) : (
                                        <>
                                            <li><Link className="dropdown-item" to="/teacher-dashboard">Dashboard</Link></li>
                                            <li><Link className="dropdown-item" to="/teacher-logout">Logout</Link></li>
                                        </>
                                    )}
                                </ul>
                            </li>
                            <li className="nav-item dropdown">
                                <a className="nav-link dropdown-toggle" href="#" id="studentDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                                    Student
                                </a>
                                <ul className="dropdown-menu" aria-labelledby="studentDropdown">
                                    {studentLoginStatus !== 'true' ? (
                                        <>
                                            <li><Link className="dropdown-item" to="/user-login">Login</Link></li>
                                            <li><Link className="dropdown-item" to="/user-register">Register</Link></li>
                                        </>
                                    ) : (
                                        <>
                                            <li><Link className="dropdown-item" to="/user-dashboard">Dashboard</Link></li>
                                            <li><Link className="dropdown-item" to="/user-logout">Logout</Link></li>
                                        </>
                                    )}
                                </ul>
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
